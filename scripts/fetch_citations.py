#!/usr/bin/env python3
"""用 Semantic Scholar 批量接口为 JSONL 中的论文补充引用数与 TL;DR（带缓存，可断点续跑）。

用法:
    python scripts/fetch_citations.py data/raw-2026.jsonl --cache data/s2-cache.json

无 API key 时 Semantic Scholar 限流较严，脚本会自动指数退避重试；
有 key 可设置环境变量 S2_API_KEY 提速。只依赖 Python 标准库。
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

URL = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=citationCount,influentialCitationCount,tldr,venue,year"
BATCH = 400


def post(ids: list[str]) -> list:
    body = json.dumps({"ids": [f"ARXIV:{i}" for i in ids]}).encode()
    headers = {"Content-Type": "application/json"}
    if os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = os.environ["S2_API_KEY"]
    wait = 5
    for _ in range(12):
        try:
            req = urllib.request.Request(URL, data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            print(f"  ! {e}; {wait}s 后重试", file=sys.stderr, flush=True)
            time.sleep(wait)
            wait = min(wait * 2, 120)
    raise RuntimeError("Semantic Scholar 请求多次失败")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("jsonl", help="fetch_arxiv.py 生成的 JSONL")
    ap.add_argument("--cache", required=True, help="缓存 JSON 路径（id -> {citations, tldr, venue}）")
    ap.add_argument("--refresh", action="store_true", help="忽略缓存，重新拉取全部")
    a = ap.parse_args()

    cache_path = Path(a.cache)
    cache = {} if a.refresh or not cache_path.exists() else json.loads(cache_path.read_text(encoding="utf-8"))
    ids = [json.loads(l)["id"] for l in open(a.jsonl, encoding="utf-8")]
    todo = [i for i in ids if i not in cache]
    print(f"共 {len(ids)} 篇，需拉取 {len(todo)} 篇")
    for k in range(0, len(todo), BATCH):
        chunk = todo[k : k + BATCH]
        for aid, r in zip(chunk, post(chunk)):
            cache[aid] = None if r is None else {
                "citations": r.get("citationCount") or 0,
                "influential": r.get("influentialCitationCount") or 0,
                "tldr": (r.get("tldr") or {}).get("text") or "",
                "venue": r.get("venue") or "",
                "year": r.get("year"),
            }
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
        print(f"  {min(k + BATCH, len(todo))}/{len(todo)}", flush=True)
        time.sleep(3)
    print(f"完成 → {cache_path}")


if __name__ == "__main__":
    main()
