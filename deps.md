# Abhängigkeiten (Diagramm-Update 2026-10-04)

Alle Pakete, die für die Analyse der Repositories und die Generierung der
Diagramme benötigt werden. Versionen: Stand 2026-10-04 (Ubuntu 26, Docker-Image
`03_ai_env`).

## System (apt)

| Paket | Version | Wofür |
|---|---|---|
| `graphviz` | 14.1.2 | `dot`-Binary, rendert die SVGs |
| `sbcl` | 2.6.0 | Führt `gen00.lisp` aus |
| `git` | (System) | Liest die Bare Repositories (`ls-tree`, `show`, `log`) |

Installieren: `apt-get update && apt-get install -y graphviz`

## Python (via `uv`, Projekt-`.venv`)

| Paket | Version | Wofür |
|---|---|---|
| `graphviz` | 0.21 | Python-API für `dot` (`gen_graphviz.py`) |
| `ruff` | 0.16.10 | Lint + Format der `tools/*.py`-Skripte |

Installieren: `uv venv && uv pip install graphviz ruff`

## Common Lisp (Quicklisp)

| System | Quelle | Wofür |
|---|---|---|
| `alexandria` | Quicklisp-Dist | `read-file-into-string` (SVG-Einbettung) |
| `spinneret` | Quicklisp-Dist | HTML-Generierung (`index.html`) |
| `cl-py-generator` | `~/quicklisp/local-projects` (Symlink) | Lisp→Python-Transpiler (`gen_graphviz.py`) |

Hinweis: `cl-py-generator` kommt nicht aus der Quicklisp-Dist, sondern aus
`local-projects`. `gen00.lisp` ruft daher zuerst `(ql:register-local-projects)`
auf.

## Reproduzierbarkeit

```sh
uv venv && uv pip install graphviz ruff
uv run python tools/01_scan_repos.py    # Bare-Repos -> tools/repo_scan.json
uv run python tools/02_cluster_data.py  # Scan -> tools/clusters.json
uv run python tools/03_emit_lisp.py --write  # Cluster -> gen00.lisp
sbcl --non-interactive --load gen00.lisp --quit
uv run python gen_graphviz.py
sbcl --non-interactive --load gen00.lisp --quit  # index.html mit frischen SVGs
uv run python tools/04_emit_overview.py # Cluster -> repos_overview.md
```
