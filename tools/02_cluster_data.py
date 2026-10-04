"""Assign each scanned repo a language and a topic cluster.

Rule-based: marker files and file extensions vote for the language,
then name/readme keywords vote for the topic cluster. Tables live in
``tools/cluster_data.json``; manual fixes in
``tools/cluster_overrides.json`` (``{repo: {"cluster": ..., "note": ...}}``)
so re-running this script never loses curation.

Usage:
    uv run python tools/02_cluster_data.py
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

DEFAULT_SCAN = Path("tools/repo_scan.json")
DEFAULT_DATA = Path("tools/cluster_data.json")
DEFAULT_OUT = Path("tools/clusters.json")
DEFAULT_OVERRIDES = Path("tools/cluster_overrides.json")


def normalize(text: str) -> str:
    """Lowercase and unify separators for keyword matching."""
    for sep in ("-", "_", "/", ".", "(", ")", "[", "]", ":", ";", ","):
        text = text.replace(sep, " ")
    return " ".join(text.lower().split())


def flat(text: str) -> str:
    """Normalized text without separators (matches 'gauss-fit' vs 'gaussfit')."""
    return normalize(text).replace(" ", "")


def name_matches(keyword: str, name: str) -> bool:
    """Match a keyword against the short repo name.

    Long keys match separator-insensitively; short keys must not hide
    inside a longer word ('spi' must not match 'spiral', but 'fft'
    matches 'fft3').
    """
    key = normalize(keyword)
    if len(key.replace(" ", "")) >= 5:
        return key.replace(" ", "") in flat(name)
    return re.search(rf"(?<![a-z]){re.escape(key)}(?![a-z])", normalize(name))


def body_matches(keyword: str, body: str, data: dict) -> bool:
    """Match a keyword against long README/log text.

    Long keys match as substrings, short keys only as whole words
    ('sar' must not match 'necessary'). Noisy keys in ``name_only_keys``
    never match here; ``body_word_only`` keys always use word matching
    ('quest' must not match 'request', 'andor' not 'and/or').
    """
    if keyword in data["name_only_keys"]:
        return False
    key = normalize(keyword)
    text = normalize(body)
    if keyword in data["body_word_only"] or len(key.replace(" ", "")) < 5:
        return re.search(rf"\b{re.escape(key)}\b", text) is not None
    return key.replace(" ", "") in text.replace(" ", "")


def detect_language(record: dict, data: dict) -> tuple[str, int, str]:
    """Vote for a language from markers + extensions."""
    scores: collections.Counter[str] = collections.Counter()
    reasons: dict[str, str] = {}
    for marker in record.get("markers", []):
        if marker in data["marker_lang"]:
            lang, bonus = data["marker_lang"][marker]
            scores[lang] += bonus
            reasons[lang] = f"marker {marker}"
    for ext, count in record.get("top_extensions", []):
        if ext in data["ext_lang"]:
            lang, weight = data["ext_lang"][ext]
            scores[lang] += weight * count
            if lang not in reasons:
                reasons[lang] = f"ext {ext}x{count}"
    if not scores:
        return "unknown", 0, "no signal"
    lang, score = scores.most_common(1)[0]
    return lang, score, reasons.get(lang, "")


def detect_cluster(record: dict, lang: str, data: dict) -> tuple[str, str, str]:
    """Return (cluster, confidence, reason) for a scanned repo."""
    name = record["name"]
    body = f"{record.get('readme_head', '')}\n{record.get('last_commit_subject', '')}"
    keywords = data["cluster_keywords"]
    for cluster, keys in keywords.items():
        for keyword in keys:
            if name_matches(keyword, name):
                return cluster, "high", f"name contains '{keyword}'"
    for cluster, keys in keywords.items():
        if cluster in data["name_only_clusters"]:
            continue
        for keyword in keys:
            if body_matches(keyword, body, data):
                return cluster, "medium", f"readme/log contains '{keyword}'"
    fallback = data["lang_fallback"].get(lang, "docs-meta")
    confidence = "medium" if lang not in ("unknown", "docs") else "low"
    return fallback, confidence, f"language fallback ({lang})"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scan", type=Path, default=DEFAULT_SCAN)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--overrides", type=Path, default=DEFAULT_OVERRIDES)
    args = parser.parse_args()

    data = json.loads(args.data.read_text())
    records = json.loads(args.scan.read_text())
    overrides = {}
    if args.overrides.exists():
        overrides = json.loads(args.overrides.read_text())

    result: dict[str, dict] = {}
    for record in records:
        name = record["name"]
        if record["status"] != "ok":
            result[name] = {
                "status": record["status"],
                "cluster": None,
                "language": None,
            }
            continue
        lang, score, lang_reason = detect_language(record, data)
        cluster, confidence, reason = detect_cluster(record, lang, data)
        if name in overrides:
            cluster = overrides[name].get("cluster", cluster)
            confidence = "high"
            note = overrides[name].get("note", "")
            reason = f"manual override ({note})" if note else "manual override"
        result[name] = {
            "status": "ok",
            "language": lang,
            "language_score": score,
            "language_reason": lang_reason,
            "cluster": cluster,
            "confidence": confidence,
            "reason": reason,
            "last_commit_date": record.get("last_commit_date", ""),
        }

    args.out.write_text(json.dumps(result, indent=1, ensure_ascii=False) + "\n")

    sizes: collections.Counter[str] = collections.Counter(
        v["cluster"] for v in result.values() if v["cluster"]
    )
    conf: collections.Counter[str] = collections.Counter(
        v["confidence"] for v in result.values() if v.get("confidence")
    )
    titles = data["cluster_titles"]
    print(f"clustered {len(result)} repos -> {args.out}")
    for cluster, num in sizes.most_common():
        print(f"  {cluster:15s} {num:3d}  {titles.get(cluster, cluster)}")
    print("confidence:", dict(conf))
    low = sorted(n for n, v in result.items() if v.get("confidence") == "low")
    print(f"low_confidence ({len(low)}): {', '.join(low)}")


if __name__ == "__main__":
    main()
