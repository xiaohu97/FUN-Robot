#!/usr/bin/env python3
"""从 arXiv API 批量抓取某时间段内的机器人 / 具身智能论文，输出 JSONL。

抓取范围（两路查询，结果按 arXiv 编号去重）:
  1. 主类或交叉列表为 cs.RO 的全部论文；
  2. cs.CV / cs.AI / cs.LG / cs.CL / cs.HC / eess.SY 中、摘要含 robot / embodied /
     humanoid / vision-language-action 等关键词、但不属于 cs.RO 的论文
     （本地再用更严格的规则过滤，去掉 "embodied carbon" 之类的误报）。

用法:
    python scripts/fetch_arxiv.py --start 2026-01-01 --end 2026-11-05 --out data/raw-2026.jsonl
    python scripts/fetch_arxiv.py --start 2026-11-01 --end 2026-11-30 --out data/raw-2026-11.jsonl

遵守 arXiv API 使用规范：每次请求间隔 3 秒。只依赖 Python 标准库。
"""
from __future__ import annotations

import argparse
import calendar
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from pathlib import Path

API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom", "os": "http://a9.com/-/spec/opensearch/1.1/"}
PAGE = 1000
DELAY = 3.0

RO_QUERY = "cat:cs.RO"
EMBODIED_QUERY = (
    "(cat:cs.CV OR cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.HC OR cat:eess.SY) AND "
    '(abs:robot OR abs:robots OR abs:robotic OR abs:embodied OR abs:humanoid OR abs:"vision-language-action") '
    "ANDNOT cat:cs.RO"
)
# 非 cs.RO 论文需要满足的严格关键词（标题或摘要）
STRICT = re.compile(
    r"\brobot|\bembodied (?:ai|agent|intelligence|navigation|reasoning|task|planning|perception|question|environment|manipulation|foundation)"
    r"|\bhumanoid|vision[- ]language[- ]action|\bVLA\b|\bquadruped|\blegged\b|\bdexterous|sim[- ]to[- ]real|\bsim2real"
    r"|\bteleoperat|\bmanipulator|\bgrasp(?:ing)?\b|world[- ]action model|\bmanipulation polic",
    re.I,
)


def months(start: date, end: date):
    cur = start
    while cur <= end:
        last = date(cur.year, cur.month, calendar.monthrange(cur.year, cur.month)[1])
        yield cur, min(last, end)
        cur = last + timedelta(days=1)


def request(params: dict, retries: int = 6) -> ET.Element:
    url = API + "?" + urllib.parse.urlencode(params)
    for k in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                root = ET.fromstring(r.read())
            time.sleep(DELAY)
            return root
        except Exception as e:  # 网络抖动 / 429 / 503
            wait = DELAY * (2 ** k)
            print(f"  ! {e}; {wait:.0f}s 后重试", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"请求失败: {url}")


def parse(entry: ET.Element) -> dict:
    t = lambda tag: (entry.findtext(tag, default="", namespaces=NS) or "").strip()
    aid = t("a:id").rsplit("/abs/", 1)[-1]
    aid = re.sub(r"v\d+$", "", aid)
    return {
        "id": aid,
        "title": " ".join(t("a:title").split()),
        "abstract": " ".join(t("a:summary").split()),
        "authors": [a.findtext("a:name", namespaces=NS) for a in entry.findall("a:author", NS)],
        "published": t("a:published")[:10],
        "updated": t("a:updated")[:10],
        "primary": entry.find("arxiv:primary_category", NS).get("term") if entry.find("arxiv:primary_category", NS) is not None else "",
        "categories": [c.get("term") for c in entry.findall("a:category", NS)],
        "comment": " ".join(t("arxiv:comment").split()),
        "journal_ref": t("arxiv:journal_ref"),
    }


def fetch_window(query: str, d0: date, d1: date) -> list[dict]:
    q = f"({query}) AND submittedDate:[{d0:%Y%m%d}0000 TO {d1:%Y%m%d}2359]"
    out, start, total = [], 0, None
    while total is None or start < total:
        root = request({"search_query": q, "start": start, "max_results": PAGE, "sortBy": "submittedDate", "sortOrder": "ascending"})
        if total is None:
            total = int(root.findtext("os:totalResults", default="0", namespaces=NS))
        entries = root.findall("a:entry", NS)
        if not entries:
            # arXiv 偶尔返回空页：重试一次后跳出
            root = request({"search_query": q, "start": start, "max_results": PAGE, "sortBy": "submittedDate", "sortOrder": "ascending"})
            entries = root.findall("a:entry", NS)
            if not entries:
                print(f"  ! 空页 start={start}/{total}，提前结束该窗口", file=sys.stderr)
                break
        out += [parse(e) for e in entries]
        start += len(entries)
    return out


def split_windows(d0: date, d1: date, parts: int):
    days = (d1 - d0).days + 1
    step = max(1, -(-days // parts))
    cur = d0
    while cur <= d1:
        nxt = min(d1, cur + timedelta(days=step - 1))
        yield cur, nxt
        cur = nxt + timedelta(days=1)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", required=True, help="起始日期 YYYY-MM-DD")
    ap.add_argument("--end", required=True, help="结束日期 YYYY-MM-DD（含）")
    ap.add_argument("--out", required=True, help="输出 JSONL 路径")
    a = ap.parse_args()
    d0, d1 = date.fromisoformat(a.start), date.fromisoformat(a.end)

    papers: dict[str, dict] = {}
    for m0, m1 in months(d0, d1):
        for name, query in (("cs.RO", RO_QUERY), ("embodied", EMBODIED_QUERY)):
            # 每月拆成 3 段，避免单次结果过大导致 arXiv 截断
            n = 0
            for w0, w1 in split_windows(m0, m1, 3):
                rows = fetch_window(query, w0, w1)
                for p in rows:
                    if name == "embodied" and not STRICT.search(p["title"] + " " + p["abstract"]):
                        continue
                    p["source"] = name
                    if p["id"] not in papers:
                        papers[p["id"]] = p
                        n += 1
            print(f"{m0:%Y-%m} {name:8s} +{n}（累计 {len(papers)}）", flush=True)

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for p in sorted(papers.values(), key=lambda x: (x["published"], x["id"])):
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f"共 {len(papers)} 篇 → {out}")


if __name__ == "__main__":
    main()
