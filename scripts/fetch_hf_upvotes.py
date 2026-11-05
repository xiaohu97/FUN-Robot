#!/usr/bin/env python3
"""抓取 Hugging Face Daily Papers 的点赞数，作为新论文（引用数还很低时）的热度信号。

用法:
    python scripts/fetch_hf_upvotes.py --start 2026-01-01 --end 2026-11-05 --out data/hf-upvotes.json

输出 {arxiv_id: upvotes}；已存在的输出文件会被合并（断点续跑）。只依赖 Python 标准库。
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
from datetime import date, timedelta
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out)
    votes = json.loads(out.read_text()) if out.exists() else {}
    d, end = date.fromisoformat(a.start), date.fromisoformat(a.end)
    while d <= end:
        url = f"https://huggingface.co/api/daily_papers?date={d.isoformat()}&limit=100"
        for k in range(5):
            try:
                with urllib.request.urlopen(url, timeout=60) as r:
                    for item in json.load(r):
                        p = item.get("paper", {})
                        if p.get("id"):
                            votes[p["id"]] = max(votes.get(p["id"], 0), p.get("upvotes") or 0)
                break
            except Exception as e:
                print(f"  ! {d} {e}", file=sys.stderr)
                time.sleep(2 ** k)
        d += timedelta(days=1)
        time.sleep(0.3)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(votes), encoding="utf-8")
    print(f"共 {len(votes)} 篇 → {out}")


if __name__ == "__main__":
    main()
