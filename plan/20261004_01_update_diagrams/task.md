# Tasks: Diagramm-Update (seriell abarbeiten, nach jedem Schritt validieren)

Arbeitsverzeichnis: Repo-Root (`/workspace/src/plops.github.io`).
Daten: `/workspace/src/github/repositories/plops/` (335 Bare-Repos, read-only behandeln).
Python: ausschließlich via `uv` (Projekt-`.venv`, `uv run …`).

## T1 — Umgebung herstellen

1. `uv venv` (falls kein `.venv`), `uv pip install graphviz ruff`.
2. `apt-get update && apt-get install -y graphviz` (liefert `dot`).
3. `git config user.name "wol pumba"`, `git config user.email "wolpumba@gmail.com"` (lokal).
4. Quicklisp-Pakete prüfen: `sbcl --non-interactive --eval '(ql:quickload "alexandria")' --eval '(ql:quickload "spinneret")' --quit`.
   Falls `cl-py-generator` nicht per quicklispdist kommt: `~/quicklisp/local-projects/` auf Symlink/Copy von `/workspace/src/cl-cl-generator` prüfen und ggf. anlegen.
- **Validierung:** `uv run python -c "import graphviz"`, `dot -V`, `sbcl --version`, alle drei grün.
- **Artefakt/Notiz:** Installiertes in `deps.md` (Repo-Root) eintragen.

## T2 — `tools/01_scan_repos.py` schreiben und laufen lassen

Skript (< 600 Zeilen, dokumentiert, `ruff`-sauber), das pro Bare-Repo sammelt:

- `git ls-tree -r HEAD --name-only` → Top-Dateiendungen (Top-10 mit Counts),
  Markerdateien (`Cargo.toml`, `*.asd`, `pyproject.toml`, `*.ino`, `CMakeLists.txt`, …)
- `git show HEAD:<README-Variante>` (README.md/org/txt/rst, readme.*) → erste 40 Zeilen
- `git log -1 --format=%ci|%s` → letztes Commit-Datum + Subject
- Sonderfälle: kein `HEAD` → `status: "empty"`; `*.wiki.git` → `status: "wiki"`
- Keine Voll-Clones; nur `git --git-dir=…` Plumbing-Befehle.

Ausgabe: `tools/repo_scan.json` (ein Eintrag pro Repo).
- **Validierung:** Einträge = 335; `empty` = 3 (dwm, learn-cl-object-orient, thesis);
  `wiki` = 6; Rest hat `extensions`/`markers`. `ruff check tools/` + `ruff format --check tools/` grün.

## T3 — `tools/02_cluster_data.py` schreiben und laufen lassen

Regelbasiertes Clustering aus `repo_scan.json`:

1. Primärsprache aus Extensions + Markern ableiten (Gewichtung: Marker > Extensions).
2. Themencluster aus Namenspräfixen (`cl-*-generator`, `cl-gen*`, `sb-*`, `arduino*`, `matlab*`, …) + README-Stichwörtern (optics, SDR, CUDA, …) zuweisen.
3. Report: Clustergrößen, `low_confidence`-Liste (Repos mit wenig Signal).
4. Ausgabe: `tools/clusters.json` (`{repo: {lang, cluster, confidence, reason}}`).

- **Validierung:** Summe aller Cluster = 326; `low_confidence`-Anteil < 15 %,
  sonst Regeln nachschärfen. `ruff` grün.

## T4 — Cluster kuratieren (Stichprobe + deepwiki)

1. Aus jedem Cluster ≥ 2 Repos stichprobenartig prüfen (`git show HEAD:README.*` lesen).
2. Maximal ~5 unklare/faszinierende Repos via deepwiki-MCP (`plops/<name>`) befragen,
   z. B. `plops/cl-rust-generator` als Referenz.
3. Anomalien (falsche Sprache, überraschende Themen) in `clusters.json`
   (`override`-Feld) oder direkt in den Regeln von `02_cluster_data.py` fixieren,
   Skript erneut laufen lassen.
- **Validierung:** `clusters.json` regeneriert, `ruff` grün, Kuratierungsnotizen
  für `walkthrough.md` (Abschnitt 3) festgehalten.

## T5 — `gen00.lisp` erweitern (Pfade portabel + `*graphs*` neu)

1. Absolute Pfade (`/home/martin/stage/plops.github.io/…`) durch repo-relative
   Pfade ersetzen (`*default-pathname-defaults*`-basiert); `presentations`-Verzeichnis
   tolerant behandeln (fehlt → leere Liste).
2. `*graphs*` neu aufbauen: pro Themencluster ein Graph-Block, jede Kante
   `thema (kurzlabel repo-pfad)` für verlinkte Knoten; reine Strukturknoten ohne Link.
   Formatierung übersichtlich halten (ein Knoten pro Zeile wie bisher).
3. Darauf achten, dass keine Klammern verloren gehen. Bei Klammerfehlern:
   maximal 2 Fix-Versuche, danach anhalten und fragen.
- **Validierung:** `sbcl --non-interactive --load gen00.lisp` läuft ohne Fehler
  und schreibt `gen_graphviz.py` + `index.html` neu. Abdeckung: alle 326 Repos
  kommen als Knoten vor (per `grep -c` gegen `clusters.json` prüfen).

## T6 — SVGs generieren und prüfen

1. `uv run python gen_graphviz.py` ausführen.
2. Prüfen: alle `graphN.svg` existieren, sind > 1 KB, enthalten `<svg`,
   blaue Knoten-URLs zeigen auf `https://github.com/plops/<repo>` und jedes
   verlinkte `<repo>` existiert im Export (Skript-Check, kein toter Link).
3. `index.html` im Browser-Kontext sichten (SVG-Einbettungen vorhanden).
- **Validierung:** Check-Skript meldet 0 tote Links, 0 leere SVGs.

## T7 — `repos_overview.md` + `deps.md` schreiben

1. `repos_overview.md` (Repo-Root): Textübersicht, gruppiert nach Themenclustern,
   je Repo ein Satz (Name + Link + Kurzbeschreibung aus README/log); eigene
   Abschnitte für leere Repos und Wiki-Repos.
2. `deps.md` (Repo-Root): alle neu eingeführten Abhängigkeiten
   (Apt: `graphviz`; Python via uv: `graphviz`, `ruff`; Lisp: `alexandria`,
   `spinneret`, `cl-py-generator`; Toolchain: `sbcl`, `uv`).
- **Validierung:** Jede Repo-Gruppe aus `clusters.json` ist in der Übersicht
  vertreten (Zähl-Check); `deps.md` nennt Versionen.

## T8 — Committen (Conventional Commits, ausführlich)

Reihenfolge, je ein Commit mit aussagekräftigem Body:

1. `feat(diagrams): scan and cluster all exported repositories` (tools/* + JSONs)
2. `feat(diagrams): rebuild *graphs* and regenerate SVGs` (gen00.lisp, gen_graphviz.py, graph*.svg, index.html)
3. `docs: add repository overview and dependency list` (repos_overview.md, deps.md, plan/*)
- **Validierung:** `git log --oneline -5` zeigt die Commits, `git status` sauber
  (bis auf `walkthrough.md`, siehe T9).

## T9 — `walkthrough.md` schreiben (Deutsch, strikte Regeln)

Erst nach T8. Ablage: `plan/20261004_01_update_diagrams/walkthrough.md`.
Pflicht (darf nicht ignoriert werden):

- Deutsch, didaktisch, flüssig wie Blog-Post/Tutorial.
- Fachbegriffe erklären (Bare Repositories, Graphviz Digraphs, … + Warum).
- Reichlich Code-Beispiele + **Mermaid-Diagramme** (Architektur, Datenfluss).
- Struktur: 1. Big Picture · 2. Bare-Repo-Analyse technisch · 3. Clustering-Entscheidungen
  + Anomalien · 4. Learnings/Zukunft · 5. Pakete fürs Dockerfile.
- Danach final committen: `docs: add walkthrough for diagram update`.
