"""Generate repos_overview.md from the scan + cluster data.

One section per topic cluster, one line per repository
(name + link + one-sentence description + language).

Usage:
    uv run python tools/04_emit_overview.py
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DEFAULT_SCAN = Path("tools/repo_scan.json")
DEFAULT_CLUSTERS = Path("tools/clusters.json")
DEFAULT_DATA = Path("tools/cluster_data.json")
DEFAULT_OUT = Path("repos_overview.md")

GRAPH_ORDER = [
    "generators",
    "lisp-libs",
    "imaging-optics",
    "sdr-radio",
    "embedded-fpga",
    "gpu-graphics",
    "ml-ai",
    "rust-apps",
    "cpp-projects",
    "web-net",
    "mobile",
    "science-math",
    "finance",
    "docs-meta",
]

CLUSTER_INTRO = {
    "generators": "Common-Lisp-Bibliotheken, die S-Expressions in andere Sprachen übersetzen — das Herzstück von plops' Code-Generierungs-Projekten.",
    "lisp-libs": "Bibliotheken, Werkzeuge und Experimente rund um Common Lisp, Clojure und artverwandte Sprachen.",
    "imaging-optics": "Mikroskopie (Steuerung, Auswertung, Simulation), Optik, Kameras und Video-Codecs.",
    "sdr-radio": "Software Defined Radio, (Amateur-)Funk, Radar und Satelliten-Empfang.",
    "embedded-fpga": "Mikrocontroller (Arduino, ESP32, RP2350), FPGAs, HDL und Firmware-nahes.",
    "gpu-graphics": "GPU-Compute (CUDA, OpenCL, Vulkan), Grafik-Demos, GUI-Toolkits und Visualisierung.",
    "ml-ai": "Machine Learning, LLMs und klassische KI-Experimente.",
    "rust-apps": "Eigenständige Werkzeuge in Rust ohne eigenen Themen-Cluster.",
    "cpp-projects": "C/C++-Projekte ohne eigenen Themen-Cluster.",
    "web-net": "Web-Frameworks, Scraping, Netzwerk-Tools und Server.",
    "mobile": "Android- und Mobile-Projekte.",
    "science-math": "Numerik, Simulation, Astrophysik, Optimierung und Mathematik.",
    "finance": "Finanz- und Trading-Experimente.",
    "docs-meta": "Abschlussarbeiten, Vorträge, Notizen, Dotfiles und Meta-Repositories.",
}


def clean_line(line: str) -> str:
    """Strip markdown/org markup from a README line."""
    line = line.strip()
    line = re.sub(r"^[#*=\-+]+\s*", "", line)  # headers, bullets
    line = re.sub(r"\[\!\[.*?\]\(.*?\)\]\(.*?\)", "", line)  # badges
    line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)  # links -> text
    line = re.sub(r"[*_`~]+", "", line)  # emphasis, code
    line = re.sub(r"\s+", " ", line).strip()
    return line


def shorten(text: str, limit: int = 160) -> str:
    """Shorten to one line, preferring full sentences and word boundaries."""
    if len(text) <= limit:
        return text
    cut = text.rfind(". ", 0, limit - 3)
    if cut > 40:
        return text[: cut + 1]
    cut = text.rfind(" ", 0, limit - 1)
    if cut > 40:
        return text[:cut] + "…"
    return text[: limit - 1] + "…"


def paragraphs(readme_head: str) -> list[tuple[str, bool]]:
    """Join wrapped lines into (text, is_header) paragraphs."""
    paras: list[tuple[str, bool]] = []
    current: list[str] = []
    for line in readme_head.splitlines():
        if not line.strip():
            if current:
                paras.append((" ".join(current), current[0].lstrip().startswith("#")))
                current = []
            continue
        current.append(line.strip())
    if current:
        paras.append((" ".join(current), current[0].lstrip().startswith("#")))
    return paras


def describe(record: dict) -> str:
    """One-sentence repo description from README head or commit subject."""
    paras = [
        (clean_line(text), header)
        for text, header in paragraphs(record.get("readme_head") or "")
    ]

    def pick(*, allow_headers: bool) -> str:
        for text, header in paras:
            if len(text) < 25:
                continue
            if header and not allow_headers:
                continue
            low = text.lower()
            if low.startswith(
                ("http://", "https://", "<", "note:", "summary description")
            ):
                continue
            if low in ("overview",):
                continue
            return shorten(text)
        return ""

    return (
        pick(allow_headers=False)
        or pick(allow_headers=True)
        or shorten((record.get("last_commit_subject") or "").strip())
        or "keine Beschreibung verfügbar"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan", type=Path, default=DEFAULT_SCAN)
    parser.add_argument("--clusters", type=Path, default=DEFAULT_CLUSTERS)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    scan = {r["name"]: r for r in json.loads(args.scan.read_text())}
    clusters = json.loads(args.clusters.read_text())
    titles = json.loads(args.data.read_text())["cluster_titles"]

    members: dict[str, list[str]] = {}
    for repo, info in clusters.items():
        if info["status"] == "ok" and info["cluster"]:
            members.setdefault(info["cluster"], []).append(repo)
    empty = sorted(n for n, i in clusters.items() if i["status"] == "empty")
    wikis = sorted(n for n, i in clusters.items() if i["status"] == "wiki")

    total = sum(len(v) for v in members.values())
    lines = [
        "# Repository-Übersicht (plops)",
        "",
        f"Kurzbeschreibung aller {total} aktiven Repositories, gruppiert nach",
        "Themengebieten. Die gleiche Gruppierung treibt die Diagramme auf der",
        "Startseite (`index.html`, `graph0..N.svg`). Stand: automatisiert aus dem",
        "GitHub-Export erzeugt, siehe `tools/` zur Reproduzierbarkeit.",
        "",
    ]
    for cluster in GRAPH_ORDER:
        repos = sorted(members.get(cluster, []))
        if not repos:
            continue
        lines += [f"## {titles[cluster]} ({len(repos)})", ""]
        lines += [CLUSTER_INTRO[cluster], ""]
        for repo in repos:
            info = clusters[repo]
            url = f"https://github.com/plops/{repo}"
            lang = info["language"]
            desc = describe(scan[repo])
            lines.append(f"- [{repo}]({url}) — {desc} ({lang})")
        lines.append("")

    lines += [
        "## Leere Repositories (kein Commit)",
        "",
        "Diese Repositories enthalten keinen einzigen Commit und erscheinen",
        "daher nicht im Diagramm:",
        "",
    ]
    lines += [f"- `{name}`" for name in empty]
    lines += [
        "",
        "## Wiki-Repositories",
        "",
        "Reine Dokumentations-Abspaltungen (GitHub Wikis), ebenfalls nicht im Diagramm:",
        "",
    ]
    lines += [f"- `{name}`" for name in wikis]
    lines.append("")

    args.out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {args.out} ({total} repos, {len(empty)} empty, {len(wikis)} wiki)")


if __name__ == "__main__":
    main()
