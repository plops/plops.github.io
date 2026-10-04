"""Emit the *graphs* literal for gen00.lisp from clusters.json.

One graph per topic cluster (plus an overview graph). Big clusters are
grouped one level deep (by language, by name prefix for lisp-libs, by
target language for generators) so the SVGs stay readable.

The generated section is spliced into gen00.lisp between the markers
``;;; BEGIN GENERATED GRAPHS`` and ``;;; END GENERATED GRAPHS``.

Usage:
    uv run python tools/03_emit_lisp.py --write   # update gen00.lisp
    uv run python tools/03_emit_lisp.py           # print to stdout
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DEFAULT_CLUSTERS = Path("tools/clusters.json")
DEFAULT_DATA = Path("tools/cluster_data.json")
DEFAULT_LISP = Path("gen00.lisp")

BEGIN_MARKER = ";;; BEGIN GENERATED GRAPHS"
END_MARKER = ";;; END GENERATED GRAPHS"

# Curated graph order (narrative, not size-sorted). Empty clusters are skipped.
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

# Clusters above this size get one intermediate grouping level.
GROUP_THRESHOLD = 14

SAFE_NAME = re.compile(r"^[A-Za-z0-9_.\-]+$")


def lisp_string(text: str) -> str:
    """Render text as a Lisp string literal."""
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def generator_target(repo: str) -> str:
    """Target language of a *-generator repo: cl-rust-generator -> rust."""
    short = repo
    for prefix in ("cl-", "coalton-"):
        short = short.removeprefix(prefix)
    short = short.removesuffix("-generator")
    return {"m": "matlab", "py": "python"}.get(short, short)


def lisp_prefix_group(repo: str) -> str:
    """Prefix group for lisp-libs members."""
    for prefix, group in (("cl-", "cl-*"), ("sb-", "sb-*")):
        if repo.startswith(prefix):
            return group
    if repo.startswith(("cl", "c-", "c_")):
        return "c/cl-*"
    return "other"


def subgroup(cluster: str, repo: str, language: str) -> str | None:
    """Intermediate group node for big clusters, else None (flat edge)."""
    if cluster == "generators":
        return f"{cluster}/{generator_target(repo)}"
    if cluster == "lisp-libs":
        return f"{cluster}/{lisp_prefix_group(repo)}"
    return f"{cluster}/{language}"


def emit_graph(root: str, members: list[tuple[str, str]], grouped: bool) -> list[str]:
    """Render one graph's edge list. Members are (repo, language) tuples."""
    lines = []
    groups: dict[str, list[str]] = {}
    if grouped:
        for repo, language in members:
            key = subgroup(root, repo, language) or root
            groups.setdefault(key, []).append(repo)
        for group in sorted(groups):
            lines.append(f"     {lisp_string(root)} {lisp_string(group)}")
        for group in sorted(groups):
            lines.append(f"     ;; {group}")
            for repo in sorted(groups[group]):
                pair = f"({lisp_string(repo)} {lisp_string(repo)})"
                lines.append(f"     {lisp_string(group)} {pair}")
    else:
        for repo, _ in sorted(members):
            pair = f"({lisp_string(repo)} {lisp_string(repo)})"
            lines.append(f"     {lisp_string(root)} {pair}")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--clusters", type=Path, default=DEFAULT_CLUSTERS)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--lisp", type=Path, default=DEFAULT_LISP)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    clusters = json.loads(args.clusters.read_text())
    titles = json.loads(args.data.read_text())["cluster_titles"]

    members: dict[str, list[tuple[str, str]]] = {}
    for repo, info in clusters.items():
        if info["status"] != "ok" or not info["cluster"]:
            continue
        assert SAFE_NAME.match(repo), f"unsafe repo name: {repo!r}"
        members.setdefault(info["cluster"], []).append((repo, info["language"]))

    ordered = [c for c in GRAPH_ORDER if c in members]
    assert len(ordered) == len(members), "GRAPH_ORDER misses a cluster!"

    graph_titles = ["Overview"] + [titles[c] for c in ordered]
    blocks = ["(defparameter *graph-titles*", "  '("]
    blocks += [f"    {lisp_string(t)}" for t in graph_titles]
    blocks += ["    ))", "", "(defparameter *graphs*", "  `("]

    overview = [f'     "main" {lisp_string(c)}' for c in ordered]
    blocks.append("   (;; 0 overview")
    blocks += overview
    blocks.append("    )")

    for index, cluster in enumerate(ordered, start=1):
        repos = members[cluster]
        grouped = len(repos) > GROUP_THRESHOLD
        blocks.append(f"   (;; {index} {cluster} ({len(repos)} repos)")
        blocks += emit_graph(cluster, repos, grouped)
        blocks.append("    )")
    blocks.append("   ))")
    section = "\n".join(blocks) + "\n"

    total = sum(len(v) for v in members.values())
    print(f"emitted {len(ordered) + 1} graphs, {total} repos")

    if not args.write:
        print(section)
        return
    text = args.lisp.read_text()
    begin = text.index(BEGIN_MARKER) + len(BEGIN_MARKER)
    end = text.index(END_MARKER)
    args.lisp.write_text(text[:begin] + "\n" + section + text[end:])
    print(f"updated {args.lisp}")


if __name__ == "__main__":
    main()
