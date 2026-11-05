#!/usr/bin/env python3
"""按模板新增一篇论文：生成表格行（可直接插入分类文件），可选同时生成精读笔记。

示例:
    # 只打印表格行（自动从 arXiv 拉标题/年份；无网络时用 --title/--year 手填）
    python scripts/new_paper.py 2410.24164 --short "π0"

    # 直接插入 01 分类的「最新进展」表格末尾，并生成笔记文件
    python scripts/new_paper.py 2410.24164 --short "π0" --topic 01 \\
        --summary "VLM + flow matching 动作专家，输出 50Hz 连续动作" \\
        --code https://github.com/Physical-Intelligence/openpi --note

    # 放进「经典论文」表格、加 ⭐
    python scripts/new_paper.py 2303.04137 --short "Diffusion Policy" --topic 06 --section classic --star

参数说明见 `--help`。只依赖 Python 标准库。
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
NOTES = PAPERS / "notes"
NOTE_TEMPLATE = ROOT / "templates" / "paper-note.md"
ATOM = "{http://www.w3.org/2005/Atom}"


def fetch_arxiv(aid: str) -> dict:
    url = f"https://export.arxiv.org/api/query?id_list={aid}&max_results=1"
    with urllib.request.urlopen(url, timeout=15) as resp:
        root = ET.fromstring(resp.read())
    entry = root.find(f"{ATOM}entry")
    if entry is None or entry.find(f"{ATOM}title") is None:
        raise RuntimeError("arXiv 未返回该编号")
    title = " ".join(entry.find(f"{ATOM}title").text.split())
    published = entry.find(f"{ATOM}published").text[:10]
    authors = [a.find(f"{ATOM}name").text for a in entry.findall(f"{ATOM}author")]
    return {"title": title, "year": int(published[:4]), "authors": authors, "published": published}


def find_topic(key: str) -> Path:
    matches = sorted(PAPERS.glob(f"{key}*.md")) or sorted(PAPERS.glob(f"*{key}*.md"))
    matches = [m for m in matches if re.match(r"\d\d-", m.name)]
    if len(matches) != 1:
        names = ", ".join(p.name for p in sorted(PAPERS.glob("[0-9][0-9]-*.md")))
        sys.exit(f"--topic '{key}' 匹配到 {len(matches)} 个文件，请从以下选择: {names}")
    return matches[0]


def slugify(s: str) -> str:
    s = re.sub(r"[^0-9A-Za-z]+", "-", s).strip("-").lower()
    return s or "paper"


def build_row(a: argparse.Namespace, note_rel: str | None) -> str:
    star = "⭐ " if a.star else ""
    name = f"**{a.short}** · {a.title}" if a.short else f"**{a.title}**"
    links = [f"[arXiv](https://arxiv.org/abs/{a.arxiv})"] if a.arxiv else []
    if a.url:
        links.append(f"[论文]({a.url})")
    if a.code:
        links.append(f"[代码]({a.code})")
    if a.project:
        links.append(f"[主页]({a.project})")
    if note_rel:
        links.append(f"[笔记]({note_rel})")
    summary = a.summary or "TODO: 一句话说清问题 + 方法 + 关键结果"
    return f"| {star}{name} | {a.year} · {a.venue} | {summary} | {' · '.join(links)} |"


def insert_row(path: Path, row: str, section: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    marker = "🏛" if section == "classic" else "🚀"
    try:
        start = next(i for i, l in enumerate(lines) if l.startswith("## ") and marker in l)
    except StopIteration:
        sys.exit(f"{path.name} 中没有找到 '{marker}' 小节，请手动粘贴表格行")
    i = start + 1
    while i < len(lines) and not lines[i].startswith("|"):
        i += 1
    while i < len(lines) and lines[i].startswith("|"):
        i += 1
    lines.insert(i, row)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def make_note(a: argparse.Namespace, topic: Path | None) -> Path:
    NOTES.mkdir(parents=True, exist_ok=True)
    fname = f"{a.arxiv or date.today().isoformat()}-{slugify(a.short or a.title)[:40]}.md"
    path = NOTES / fname
    if path.exists():
        print(f"笔记已存在，跳过创建: {path.relative_to(ROOT)}")
        return path
    t = NOTE_TEMPLATE.read_text(encoding="utf-8")
    title = a.title.replace('"', "'")
    repl = [
        ('title: "论文英文全称"', f'title: "{title}"'),
        ('short_name: "简称"', f'short_name: "{a.short or ""}"'),
        ('arxiv: "XXXX.XXXXX"', f'arxiv: "{a.arxiv or ""}"'),
        ('venue: "CoRL 2025 / arXiv"', f'venue: "{a.venue}"'),
        ("year: 2026", f"year: {a.year}"),
        ('authors: "第一作者 et al."', f'authors: "{a.authors}"'),
        ('topic: "06-imitation-learning"', f'topic: "{topic.stem if topic else ""}"'),
        ('paper: "https://arxiv.org/abs/XXXX.XXXXX"', f'paper: "https://arxiv.org/abs/{a.arxiv}"' if a.arxiv else f'paper: "{a.url or ""}"'),
        ('code: ""', f'code: "{a.code or ""}"'),
        ('project: ""', f'project: "{a.project or ""}"'),
        ('status: "精读"', 'status: "待读"'),
        ('date_read: "YYYY-MM-DD"', f'date_read: "{date.today().isoformat()}"'),
        ("# 简称：英文全称", f"# {a.short + '：' if a.short else ''}{a.title}"),
        ("journal = {arXiv preprint arXiv:XXXX.XXXXX}", f"journal = {{arXiv preprint arXiv:{a.arxiv}}}"),
    ]
    for old, new in repl:
        t = t.replace(old, new, 1)
    path.write_text(t, encoding="utf-8")
    return path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arxiv", nargs="?", help="arXiv 编号，如 2410.24164（不带 v1）；无 arXiv 时省略并使用 --url")
    ap.add_argument("--short", default="", help="简称，如 π0 / RT-2")
    ap.add_argument("--title", help="英文全称（默认从 arXiv 获取）")
    ap.add_argument("--year", type=int, help="年份（默认从 arXiv 获取）")
    ap.add_argument("--venue", default="arXiv", help="会议/期刊，如 CoRL'25（默认 arXiv）")
    ap.add_argument("--summary", help="中文一句话贡献（≤60 字）")
    ap.add_argument("--url", help="非 arXiv 论文链接")
    ap.add_argument("--code", help="代码仓库链接")
    ap.add_argument("--project", help="项目主页链接")
    ap.add_argument("--topic", help="分类编号或关键词，如 01 / humanoid；给出则直接插入该文件")
    ap.add_argument("--section", choices=["latest", "classic"], default="latest", help="插入哪个小节（默认 latest）")
    ap.add_argument("--star", action="store_true", help="标记为 ⭐ 必读")
    ap.add_argument("--note", action="store_true", help="同时用 templates/paper-note.md 生成精读笔记")
    a = ap.parse_args()

    if a.arxiv:
        a.arxiv = re.sub(r"v\d+$", "", a.arxiv.strip().split("/")[-1])
    elif not a.url:
        ap.error("需要 arXiv 编号或 --url")

    a.authors = ""
    if a.arxiv and (not a.title or not a.year):
        try:
            meta = fetch_arxiv(a.arxiv)
            a.title = a.title or meta["title"]
            a.year = a.year or meta["year"]
            a.authors = f"{meta['authors'][0]} et al." if meta["authors"] else ""
            print(f"[arXiv] {meta['title']} ({meta['published']})")
        except Exception as e:  # 网络不可用等
            print(f"⚠️  无法从 arXiv 获取元信息（{e}），请用 --title / --year 手动填写", file=sys.stderr)
    if not a.title or not a.year:
        sys.exit("缺少 --title 或 --year")

    topic = find_topic(a.topic) if a.topic else None

    if topic and a.arxiv:
        for f in PAPERS.glob("[0-9][0-9]-*.md"):
            if f"arxiv.org/abs/{a.arxiv}" in f.read_text(encoding="utf-8"):
                sys.exit(f"❌ {a.arxiv} 已收录在 papers/{f.name}，不重复添加")

    note_path = make_note(a, topic) if a.note else None
    note_rel = f"./notes/{note_path.name}" if note_path else None
    row = build_row(a, note_rel)

    if topic:
        insert_row(topic, row, a.section)
        print(f"✅ 已插入 papers/{topic.name}（{'经典论文' if a.section == 'classic' else '最新进展'}）")
    print("\n" + row + "\n")
    if note_path:
        print(f"📝 笔记: {note_path.relative_to(ROOT)}")
    print("下一步：运行 `python scripts/check.py --update` 检查重复并刷新统计")


if __name__ == "__main__":
    main()
