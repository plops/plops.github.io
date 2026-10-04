# Implementierungsplan: Übersichts-Diagramm der GitHub-Repositories aktualisieren

Datum: 2026-10-04 · Auftrag: wol pumba (wolpumba@gmail.com) · Repo: `plops.github.io`

## 1. Ziel und Kontext

Auf der GitHub-Pages-Seite (Repo `plops.github.io`) wird ein Übersichts-Diagramm
aller Repositories von `github.com/plops` als SVG gerendert. Das Diagramm ist
veraltet: Es bildet nur einen Bruchteil der Repositories ab.

Datengrundlage ist ein aktueller GitHub-Export, entpackt unter:

```
/workspace/src/github/repositories/plops/   # 335 *.git Bare Repositories
```

Aktuelle Generierungskette (funktioniert, ist aber veraltet/portierungsbedürftig):

```
gen00.lisp  (*graphs*-Datenstruktur)
    │  sbcl + quicklisp (alexandria, spinneret, cl-py-generator)
    ▼
gen_graphviz.py   (generiert)
    │  python + graphviz-Paket + graphviz-Binary (dot)
    ▼
graph0.svg … graph3.svg  → eingebettet in index.html
```

Aufgabe: Alle Repositories analysieren, thematisch clustern, `*graphs*` in
`gen00.lisp` erweitern, SVGs neu generieren, zusätzlich eine Textübersicht mit
Klassifizierung schreiben.

## 2. Befund der Sondierung (2026-10-04)

| Befund | Details |
|---|---|
| Anzahl Repos | 335 `*.git`-Ordner |
| Wiki-Repos | 6 (`*.wiki.git`, reine Doku-Abspaltungen, kein eigener Code) |
| Leere Repos (kein einziger Commit, `HEAD` ungültig) | 3: `dwm`, `learn-cl-object-orient`, `thesis` |
| Analysefähige Repos | 326 |
| Branch-Namen | gemischt `main`/`master`, aber `HEAD` löst überall korrekt auf (außer den 3 leeren) |
| SBCL | 2.6.0 vorhanden, Quicklisp unter `~/quicklisp` installiert |
| Python | 3.14, `uv` 0.12.22 verfügbar; **kein** `graphviz`-Paket installiert |
| Graphviz-Binary (`dot`) | **nicht** installiert |
| `git user.name/email` | **nicht** gesetzt (für Commits setzen: wol pumba / wolpumba@gmail.com) |
| Harte Altlast | `gen00.lisp` enthält absolute Pfade `/home/martin/stage/plops.github.io/…` (Zeilen 27, 139) — auf dieser Maschine ungültig, müssen portabel gemacht werden |

### Offene Requirements (im Prompt nicht geregelt, hier entschieden)

1. **Leere Repos (3):** werden im Diagramm nicht als Knoten geführt (kein Inhalt,
   keine Sprache erkennbar), aber in der Textübersicht unter „Leere/unlesbare
   Repos" dokumentiert.
2. **Wiki-Repos (6):** keine eigenen Knoten (Doku gehört zum Haupt-Repo), in der
   Textübersicht erwähnt.
3. **Absolute Pfade in `gen00.lisp`:** werden auf relative Pfade (Repo-Root)
   umgestellt, damit `sbcl --load gen00.lisp` überall läuft.
4. **Ablageorte:** Textübersicht → `repos_overview.md` (Repo-Root, verlinkbar);
   Abhängigkeiten → `deps.md` (Repo-Root); Analyse-Skripte → `tools/`
   (`01_scan_repos.py`, `02_cluster_data.py`), je < 600 Zeilen, committed.
5. **Helper-Artefakte:** Scan-Rohdaten als `tools/repo_scan.json` committen
   (Reproduzierbarkeit ohne Re-Scan).
6. **`index.html`:** wird mit regeneriert, aber der `presentations`-Pfad zeigt
   auf ein nicht vorhandenes Verzeichnis — tolerant behandeln (leere Liste statt
   Fehler).

## 3. Architektur der Lösung

```
tools/01_scan_repos.py
    │ liest jedes Bare-Repo NUR mit git-Bordmitteln:
    │   ls-tree (Dateiliste) → Sprach-Score aus Dateiendungen + Markerdateien
    │   show HEAD:README.*    → erste ~40 Zeilen als Beschreibung
    │   log -1 (Datum, Subject), ls-remote-freie Metriken (Dateianzahl)
    ▼
tools/repo_scan.json          # Rohdaten: ein Objekt pro Repo
    │
tools/02_cluster_data.py
    │ regelbasiert: Sprache + Namenspräfix (cl-*, cl-gen*, *-generator, sb-*)
    │   + README-Stichwörter → Themencluster (s.u.)
    ▼
tools/clusters.json + Konsolen-Report (Verteilung, Anomalien)
    │
    │ manuelle Kuratierung (Stichprobe + deepwiki für ≤5 unklare Repos)
    ▼
gen00.lisp (*graphs* erweitert, Pfade portabel)
    │  sbcl --load gen00.lisp   → gen_graphviz.py + index.html
    │  uv run python gen_graphviz.py  → graphN.svg
    ▼
graph0..N.svg, index.html, repos_overview.md, deps.md, walkthrough.md
```

### Geplante Cluster (Startvermutung, wird durch Scan verfeinert)

- `sexpr-generators`: `cl-*-generator`-Familie (rust, cpp, python, js, …)
- `lisp-libs`: sonstige `cl-*`/`sb-*`/ASDF-Bibliotheken
- `optics-microscopy`: Mikroskopie, Optik, Bildverarbeitung, Kalibrierung
- `sdr-radio`: SDR, Pluto, FM/RDS, SAR, Radar
- `embedded-arduino`: Arduino, STM32, ESP32/RP2350, FPGA
- `gpu-compute`: CUDA, OpenCL, Vulkan, OptiX, Shader
- `ml-ai`: ML/LLM/Vision-Projekte (mnist, sam, summarizer, …)
- `rust-apps`, `python-apps`, `web`, `science-misc`, `thesis-docs`, `meta`

Jeder Graph in `*graphs*` bleibt ein flacher Kanten-Block (`a b a c …`);
Themen werden eigene Graphen (eigene SVGs), damit `index.html` sie als Galerie
einbetten kann. Knoten mit Repo-Link werden blau (bestehende Konvention).

## 4. Risiken und Gegenmaßnahmen

| Risiko | Maßnahme |
|---|---|
| Klammerfehler in `gen00.lisp` | Nach jeder Änderung: `sbcl --non-interactive --load gen00.lisp`; nach 2 Fehlversuchen anhalten und fragen (Prompt-Regel) |
| `dot` fehlt | `apt-get install -y graphviz` (als neue Abhängigkeit in `deps.md`) |
| Lisp-Libs fehlen (`cl-py-generator` aus lokalem quicklisp-dist?) | zuerst `ql:quickload` versuchen; bei Fehlern `~/quicklisp/local-projects`-Symlink auf `cl-cl-generator`-Checkout prüfen |
| Repos ohne README/spärlich | Fallback: Sprach-Statistik + Name; Flag `low_confidence` im Scan |
| SVG zu groß/unleserlich bei 326 Knoten | Aufteilung auf ~6–10 Graphen/SVGs statt 4; keine Kanten zwischen Graphen nötig |

## 5. Validierung (Definition of Done)

1. `01_scan_repos.py` läuft fehlerfrei; `repo_scan.json` enthält 335 Einträge
   (davon 326 mit Sprachdaten, 3 `empty`, 6 `wiki`).
2. `ruff check` + `ruff format --check` für alle Python-Dateien grün.
3. `sbcl --non-interactive --load gen00.lisp` erzeugt `gen_graphviz.py`
   und `index.html` ohne Fehler.
4. `uv run python gen_graphviz.py` erzeugt alle `graphN.svg` (valide SVG,
   > 1 KB, referenzieren `https://github.com/plops/…` nur für existierende Repos).
5. Jedes analysefähige Repo kommt in Diagramm **oder** begründet in der
   Textübersicht vor (Abdeckungs-Check per Skript).
6. Commits im Conventional-Commit-Format mit ausführlicher Beschreibung.
7. `walkthrough.md` auf Deutsch nach den strikten Regeln aus dem Prompt.
