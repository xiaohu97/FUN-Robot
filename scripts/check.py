#!/usr/bin/env python3
"""检查论文清单并统计收录数量。

用法:
    python scripts/check.py              # 检查重复 / 链接格式 / 笔记链接，并打印统计
    python scripts/check.py --update     # 同时把统计表写回 README.md 与 papers/README.md

只依赖 Python 标准库。
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
TOPIC_GLOB = "[0-9][0-9]-*.md"

ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(v\d+)?")
TITLE_RE = re.compile(r"^#\s+(.+)$", re.M)
LINK_RE = re.compile(r"\]\((\./[^)]+\.md)\)")
STATS_START = "<!-- STATS:START -->"
STATS_END = "<!-- STATS:END -->"


def topic_files() -> list[Path]:
    return sorted(PAPERS.glob(TOPIC_GLOB))


def parse_topic(path: Path) -> dict:
    """返回 {title, classic, latest, stars, rows:[(line_no, line)]}"""
    text = path.read_text(encoding="utf-8")
    m = TITLE_RE.search(text)
    title = m.group(1).strip() if m else path.stem
    title = re.sub(r"^\d+\s*·\s*", "", title)
    section = "other"
    info = {"title": title, "classic": 0, "latest": 0, "other": 0, "stars": 0, "rows": []}
    for no, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            if "🏛" in line or "经典" in line:
                section = "classic"
            elif "🚀" in line or "最新" in line:
                section = "latest"
            else:
                section = "other"
            continue
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| 论文") or line.startswith("| 综述"):
            continue
        info[section] += 1
        if "⭐" in line:
            info["stars"] += 1
        info["rows"].append((no, line))
    return info


def check(files: list[Path]) -> tuple[list[str], dict]:
    problems: list[str] = []
    seen: dict[str, list[str]] = defaultdict(list)
    stats = {}
    for f in files:
        info = parse_topic(f)
        stats[f] = info
        for no, line in info["rows"]:
            loc = f"{f.relative_to(ROOT)}:{no}"
            ids = ARXIV_RE.findall(line)
            for aid, ver in ids:
                seen[aid].append(loc)
                if ver:
                    problems.append(f"{loc}: arXiv 链接请去掉版本号 {aid}{ver}")
            if "](" not in line:
                problems.append(f"{loc}: 该行没有任何链接")
            for rel in LINK_RE.findall(line):
                if not (f.parent / rel).exists():
                    problems.append(f"{loc}: 笔记链接不存在 {rel}")
    for aid, locs in seen.items():
        if len(locs) > 1:
            problems.append(f"重复收录 arXiv {aid}: " + ", ".join(locs))
    return problems, stats


def stats_table(stats: dict, link_prefix: str) -> str:
    lines = [
        "| 方向 | 经典 | 最新进展 | ⭐ 必读 | 合计 |",
        "|---|---:|---:|---:|---:|",
    ]
    tc = tl = ts = 0
    for f, s in stats.items():
        total = s["classic"] + s["latest"] + s["other"]
        tc += s["classic"]
        tl += s["latest"] + s["other"]
        ts += s["stars"]
        lines.append(
            f"| [{s['title']}]({link_prefix}{f.name}) | {s['classic']} | {s['latest'] + s['other']} | {s['stars']} | {total} |"
        )
    lines.append(f"| **总计** | **{tc}** | **{tl}** | **{ts}** | **{tc + tl}** |")
    return "\n".join(lines)


def write_block(path: Path, block: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if STATS_START not in text or STATS_END not in text:
        return False
    pre, rest = text.split(STATS_START, 1)
    _, post = rest.split(STATS_END, 1)
    new = f"{pre}{STATS_START}\n{block}\n{STATS_END}{post}"
    if new != text:
        path.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--update", action="store_true", help="把统计表写回 README.md 和 papers/README.md")
    args = ap.parse_args()

    files = topic_files()
    problems, stats = check(files)

    print(stats_table(stats, "papers/"))
    if args.update:
        for path, prefix in ((ROOT / "README.md", "papers/"), (PAPERS / "README.md", "./")):
            if path.exists() and write_block(path, stats_table(stats, prefix)):
                print(f"已更新统计: {path.relative_to(ROOT)}")

    if problems:
        print(f"\n发现 {len(problems)} 个问题:")
        for p in problems:
            print("  - " + p)
        return 1
    print("\n✅ 检查通过：无重复、链接格式正确")
    return 0


if __name__ == "__main__":
    sys.exit(main())
