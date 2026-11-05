#!/usr/bin/env python3
"""把 fetch_arxiv.py 抓到的论文自动分类，生成按月速递、年度总览和 CSV 数据表。

用法:
    python scripts/build_digest.py data/raw-2026.jsonl --cache data/s2-cache.json --hf data/hf-upvotes.json --year 2026

输出:
    digests/<year>-MM-arxiv.md        每月一份：方向统计 + 本月高引 Top + 各方向清单
    digests/<year>-annual-arxiv.md    年度总览：月度×方向统计 + 年度高引 Top 100 + 各方向年度 Top
    data/arxiv-<year>.csv             全量数据表（可用 Excel / pandas 筛选）

分类是基于标题和摘要关键词的自动规则（见 TOPICS），可能有误；
重要论文请人工确认后用 new_paper.py 写入 papers/ 分类清单。
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIGESTS = ROOT / "digests"
DATA = ROOT / "data"

# (编号, 中文名, 正则)。标题命中权重 3，摘要命中权重 1；得分相同按列表顺序优先。
TOPICS: list[tuple[str, str, str]] = [
    ("12", "综述与教程", r"\b(?:survey|review|tutorial|overview|roadmap|position paper)\b"),
    ("01", "VLA 与机器人基础模型", r"vision[- ]language[- ]action|VLAs?\b|robot(?:ic)? foundation model|generalist (?:robot )?polic|foundation polic|cross[- ]embodiment|robot(?:ic)? (?:large )?model|\bπ0|\bpi0"),
    ("05", "人形机器人", r"\bhumanoids?\b|whole[- ]body (?:control|motion|teleop|track|loco)|motion tracking|motion retarget|\bretarget|behavior foundation model"),
    ("07", "世界模型与视频生成", r"world[- ]models?\b|world[- ]action model|\bWAMs?\b|video (?:generation|prediction|diffusion|world)|generative simulat|action[- ]conditioned video"),
    ("02", "具身推理与任务规划", r"large language model|\bLLMs?\b|\bVLMs?\b|vision[- ]language model|task planning|embodied reasoning|spatial reasoning|chain[- ]of[- ]thought|\breasoning\b|reward (?:design|model|function)|code generation|agentic"),
    ("09", "具身导航与移动操作", r"\bnavigation\b|\bVLN\b|object[- ]goal|exploration|mobile manipulat|\bwayfinding|semantic map"),
    ("06", "操作、抓取与灵巧手", r"\bgrasp|manipulation|dexterous|in[- ]hand|\btactile|\bassembly\b|bimanual|deformable|\bcloth|articulated object|pick[- ]and[- ]place|contact[- ]rich|\bgripper"),
    ("03", "模仿学习与策略学习", r"imitation learning|behavio(?:u)?r(?:al)? cloning|diffusion polic|flow[- ]matching polic|visuomotor|demonstrations?\b|action chunk|policy learning|learning from (?:human|video)"),
    ("04", "强化学习与足式运动控制", r"reinforcement learning|\bRL\b|quadruped|\blegged\b|locomotion|\bgait\b|policy optimization|\bPPO\b|reward shaping"),
    ("10", "数据采集、遥操作与数据集", r"\bdatasets?\b|teleoperat|data collection|data generation|data (?:scaling|engine|pipeline)|egocentric|human videos?|motion capture|\bmocap\b"),
    ("11", "仿真平台、Sim2Real 与评测基准", r"simulat(?:or|ion platform|ion framework)|\bbenchmark|sim[- ]?to[- ]?real|\bsim2real|digital twin|physics engine|evaluation (?:suite|framework|protocol)"),
    ("08", "视觉表征与 3D 场景理解", r"3D reconstruction|scene (?:understanding|graph|representation)|point clouds?|pose estimation|gaussian splatting|\b3DGS\b|\bNeRF\b|segmentation|representation learning|depth estimation|object detection|affordance"),
    ("13", "自动驾驶", r"autonomous (?:driving|vehicles?)|self[- ]driving|\bdriving\b|traffic|\blane\b|motion forecasting|end[- ]to[- ]end driving|\bBEV\b|(?:autonomous|connected|intelligent) vehicles?"),
    ("14", "空中、水下与空间机器人", r"\bUAVs?\b|\bdrones?\b|quadrotor|quadcopter|aerial|multirotor|underwater|\bmarine\b|\bAUVs?\b|spacecraft|\bspace robot|satellite|legged? jump"),
    ("15", "SLAM、定位与建图", r"\bSLAM\b|visual[- ]inertial|\bVIO\b|\bVINS|localization|odometry|\bmapping\b|\bLiDAR\b|calibration|place recognition|loop closure|state estimation"),
    ("16", "运动规划与控制", r"motion planning|path planning|trajectory (?:optimization|planning|generation)|model predictive|\bMPC\b|control barrier|collision avoidance|optimal control|\bcontroller\b|kinematics|dynamics model|impedance|stability"),
    ("17", "多机器人与人机交互", r"multi[- ]robot|multi[- ]agent|\bswarm|human[- ]robot (?:interaction|collaboration)|\bHRI\b|social robot|shared autonomy|human[- ]in[- ]the[- ]loop|user study"),
    ("18", "医疗、软体与特种机器人", r"surgical|surgery|medical|soft robot|continuum robot|exoskeleton|prosthe|rehabilitation|agricultur|\bcrop|harvest|wearable|micro[- ]?robot|actuator design|origami"),
]
OTHER = ("99", "其他")
TOPIC_NAME = {k: n for k, n, _ in TOPICS} | {OTHER[0]: OTHER[1]}
TOPIC_RE = [(k, re.compile(p, re.I)) for k, _, p in TOPICS]
DISPLAY = sorted([k for k, _, _ in TOPICS], key=int) + [OTHER[0]]
PAPER_FILE = {p.name[:2]: p.name for p in (ROOT / "papers").glob("[0-9][0-9]-*.md")}

STRICT = re.compile(
    r"\brobot|\bembodied (?:ai|agent|intelligence|navigation|reasoning|task|planning|perception|question|environment|manipulation|foundation)"
    r"|\bhumanoid|vision[- ]language[- ]action|\bVLA\b|\bquadruped|\blegged\b|\bdexterous|sim[- ]to[- ]real|\bsim2real"
    r"|\bteleoperat|\bmanipulator|world[- ]action model",
    re.I,
)
VENUE_RE = re.compile(
    r"\b(ICRA|IROS|RSS|CoRL|CVPR|ICCV|ECCV|NeurIPS|ICLR|ICML|RA-?L|T-RO|TRO|IJRR|Science Robotics|Humanoids|AAAI|IJCAI|ACL|EMNLP|HRI|ISRR|WAFR|CASE|SIGGRAPH(?: Asia)?|3DV|WACV|ACM MM|L4DC|AAMAS|IROS)\b[\s']*((?:20)?2[5-7])?",
    re.I,
)
MONTH_CN = "一二三四五六七八九十"


def month_name(m: int) -> str:
    return f"{m}月"


def keep(p: dict) -> bool:
    if p.get("source") == "cs.RO":
        return True
    # 非 cs.RO：标题含强关键词，或摘要中至少命中 2 次
    return bool(STRICT.search(p["title"])) or len(STRICT.findall(p["abstract"])) >= 2


# 标题优先规则：标题命中则直接归类（顺序即优先级），解决“自动驾驶 VLA”“操作用世界模型”等跨方向论文
TITLE_PRIORITY = [(k, re.compile(rx, re.I)) for k, rx in [
    ("13", r"autonomous driving|self[- ]driving|\bdriving\b|autonomous vehicle"),
    ("07", r"world[- ]action model|\bWAMs?\b|world models?\b"),
    ("09", r"vision[- ]and[- ]language navigation|vision[- ]language navigation|\bVLN\b"),
    ("01", r"vision[- ]language[- ]action|VLAs?\b"),
    ("05", r"\bhumanoids?\b"),
    ("14", r"\bUAVs?\b|\bdrones?\b|quadrotor|aerial|underwater"),
    ("18", r"surgical|surgery|exoskeleton|soft robot|continuum robot"),
]]


def classify(p: dict) -> str:
    title, abstract = p["title"], p["abstract"]
    if TOPIC_RE[0][1].search(title) and re.search(r"survey|review|tutorial|overview|roadmap", title, re.I):
        return "12"
    for k, rx in TITLE_PRIORITY:
        if rx.search(title):
            return k
    best, best_score = OTHER[0], 0
    for k, rx in TOPIC_RE:
        if k == "12":
            if rx.search(title) and re.search(r"survey|review|tutorial|overview|roadmap", title, re.I):
                return k
            continue
        score = 3 * len(rx.findall(title)) + min(len(rx.findall(abstract)), 4)
        if score > best_score:
            best, best_score = k, score
    return best


def venue(p: dict, s2: dict | None) -> str:
    text = f"{p.get('journal_ref', '')} {p.get('comment', '')}"
    if re.search(r"accept|to appear|published|camera[- ]ready|proceedings|oral|spotlight|journal", text, re.I) or p.get("journal_ref"):
        m = VENUE_RE.search(text)
        if m:
            name = m.group(1)
            name = {"RAL": "RA-L", "TRO": "T-RO"}.get(name.upper().replace("-", ""), name)
            yr = m.group(2) or ""
            yr = ("20" + yr[-2:]) if yr else ""
            return f"{name} {yr}".strip()
    return ""


def tldr(p: dict, s2: dict | None, n: int = 220) -> str:
    if s2 and s2.get("tldr"):
        t = s2["tldr"]
    else:
        t = re.split(r"(?<=[.!?])\s+(?=[A-Z])", p["abstract"], maxsplit=1)[0]
    t = t.replace("|", "/").strip()
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


def short(s: str, n: int = 70) -> str:
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def esc(s: str) -> str:
    return s.replace("[", "［").replace("]", "］").replace("|", "/")


HF: dict[str, int] = {}


def cites(s2: dict | None) -> int:
    return (s2 or {}).get("citations", 0) or 0


def old_year(p: dict, s2: dict | None) -> int | None:
    """Semantic Scholar 记录的发表年份明显早于 arXiv 上传年份 → 旧作新传（继承了旧引用数）"""
    y = (s2 or {}).get("year")
    return y if y and y < int(p["published"][:4]) - 1 else None


def score(p: dict, cache: dict) -> float:
    """热度 = 引用数 + 0.5 × Hugging Face 点赞数（新论文引用低时，点赞提供区分度）；旧作不计引用"""
    s2 = cache.get(p["id"])
    return (0 if old_year(p, s2) else cites(s2)) + 0.5 * HF.get(p["id"], 0)


def stat(p: dict, s2: dict | None) -> str:
    s = f"引用 {cites(s2)}"
    if old_year(p, s2):
        s += f"（{old_year(p, s2)} 年旧作，不计入排名）"
    if HF.get(p["id"]):
        s += f" · 👍 {HF[p['id']]}"
    return s


def line_full(i: int, p: dict, s2: dict | None, show_topic: bool = False) -> str:
    au = p["authors"][0] + (" et al." if len(p["authors"]) > 1 else "") if p["authors"] else ""
    meta = [p["published"], au, stat(p, s2)]
    v = venue(p, s2)
    if v:
        meta.append(f"`{v}`")
    if show_topic:
        meta.append(f"[{p['topic']} {TOPIC_NAME[p['topic']]}](#{p['topic']})")
    return f"{i}. **[{esc(p['title'])}](https://arxiv.org/abs/{p['id']})** · " + " · ".join(meta) + f"\n   > {tldr(p, s2)}"


def line_short(p: dict, s2: dict | None) -> str:
    extra = stat(p, s2) if (cites(s2) or HF.get(p["id"])) else ""
    return f"- [{esc(p['title'])}](https://arxiv.org/abs/{p['id']}) · {p['published'][5:]}" + (f" · {extra}" if extra else "")


def rank(ps: list[dict], cache: dict) -> list[dict]:
    return sorted(ps, key=lambda p: (-score(p, cache), p["published"], p["id"]))


def topic_anchor_table(counter: Counter, link_month: bool = True) -> list[str]:
    rows = ["| 方向 | 篇数 | 长期清单 |", "|---|---:|---|"]
    for k in DISPLAY:
        if counter.get(k):
            pf = PAPER_FILE.get(k)
            rows.append(f"| [{k} · {TOPIC_NAME[k]}](#{k}) | {counter[k]} | " + (f"[papers/{pf}](../papers/{pf})" if pf else "—") + " |")
    return rows


def build_month(year: int, m: int, ps: list[dict], cache: dict, top_overall: int, top_topic: int, start: str, end: str) -> str:
    by_topic = defaultdict(list)
    for p in ps:
        by_topic[p["topic"]].append(p)
    cnt = Counter({k: len(v) for k, v in by_topic.items()})
    out = [
        f"# {year} 年 {m} 月 · arXiv 机器人与具身智能论文全量清单",
        "",
        f"> ⬅️ [进展速递索引](./README.md) · [年度总览](./{year}-annual-arxiv.md)",
        ">",
        f"> 范围：{start} ~ {end} 首次提交（v1）的 **cs.RO 全部论文** + 其他分类中的具身智能相关论文，共 **{len(ps)}** 篇。",
        "> 分类为关键词自动规则（`scripts/build_digest.py`），可能有误；排序按热度 = 引用数 + 0.5×Hugging Face 点赞数；引用数来自 Semantic Scholar（统计于 "
        f"{date.today().isoformat()}），新论文引用天然偏低；摘要为 Semantic Scholar TL;DR 或英文摘要首句。",
        "",
        "## 方向分布",
        "",
        *topic_anchor_table(cnt),
        "",
        f"## 🔥 本月最热 Top {top_overall}",
        "",
    ]
    for i, p in enumerate(rank(ps, cache)[:top_overall], 1):
        out.append(line_full(i, p, cache.get(p["id"]), show_topic=True))
    out.append("")
    for k in DISPLAY:
        group = by_topic.get(k)
        if not group:
            continue
        ranked = rank(group, cache)
        out += ["", f'<a id="{k}"></a>', f"## {k} · {TOPIC_NAME[k]}（{len(group)} 篇）", ""]
        for i, p in enumerate(ranked[:top_topic], 1):
            out.append(line_full(i, p, cache.get(p["id"])))
        rest = ranked[top_topic:]
        if rest:
            out += ["", f"<details><summary>其余 {len(rest)} 篇（按热度排序）</summary>", ""]
            out += [line_short(p, cache.get(p["id"])) for p in rest]
            out += ["", "</details>"]
    return "\n".join(out) + "\n"


def build_annual(year: int, papers: list[dict], cache: dict, months_present: list[int], top_n: int, per_topic: int, start: str, end: str) -> str:
    keys = DISPLAY
    mat = defaultdict(Counter)
    for p in papers:
        mat[p["topic"]][int(p["published"][5:7])] += 1
    out = [
        f"# {year} 年 arXiv 机器人与具身智能论文年度总览",
        "",
        "> ⬅️ [进展速递索引](./README.md)",
        ">",
        f"> 范围：{start} ~ {end}，共 **{len(papers)}** 篇（cs.RO 全部 + 其他分类的具身智能论文）。"
        f" 排序按热度 = 引用数（Semantic Scholar，统计于 {date.today().isoformat()}）+ 0.5×Hugging Face 点赞数。",
        "",
        "## 月度 × 方向统计",
        "",
        "| 方向 | " + " | ".join(f"[{m}月](./{year}-{m:02d}-arxiv.md)" for m in months_present) + " | 合计 |",
        "|---|" + "---:|" * (len(months_present) + 1),
    ]
    for k in keys:
        if not mat[k]:
            continue
        out.append(f"| [{k} · {TOPIC_NAME[k]}](#{k}) | " + " | ".join(str(mat[k][m]) for m in months_present) + f" | {sum(mat[k].values())} |")
    tot = Counter(int(p["published"][5:7]) for p in papers)
    out.append("| **合计** | " + " | ".join(f"**{tot[m]}**" for m in months_present) + f" | **{len(papers)}** |")
    out += ["", f"## 🏆 年度最热 Top {top_n}", ""]
    for i, p in enumerate(rank(papers, cache)[:top_n], 1):
        out.append(line_full(i, p, cache.get(p["id"]), show_topic=True))
    by_topic = defaultdict(list)
    for p in papers:
        by_topic[p["topic"]].append(p)
    out += ["", f"## 各方向年度 Top {per_topic}", ""]
    for k in keys:
        group = by_topic.get(k)
        if not group:
            continue
        pf = PAPER_FILE.get(k)
        out += [f'<a id="{k}"></a>', f"### {k} · {TOPIC_NAME[k]}（{len(group)} 篇）" + (f" · 长期清单 [papers/{pf}](../papers/{pf})" if pf else ""), ""]
        for p in rank(group, cache)[:per_topic]:
            s2 = cache.get(p["id"])
            v = venue(p, s2)
            out.append(f"- [{esc(p['title'])}](https://arxiv.org/abs/{p['id']}) · {p['published']} · {stat(p, s2)}" + (f" · `{v}`" if v else ""))
        out.append("")
    return "\n".join(out) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("jsonl")
    ap.add_argument("--cache", help="fetch_citations.py 生成的缓存")
    ap.add_argument("--year", type=int, required=True)
    ap.add_argument("--hf", help="fetch_hf_upvotes.py 生成的点赞数 JSON（可选）")
    ap.add_argument("--start", help="只保留 v1 日期 >= start（默认当年 1 月 1 日）")
    ap.add_argument("--end", help="只保留 v1 日期 <= end（默认数据中最晚日期）")
    ap.add_argument("--top", type=int, default=15, help="每月总榜条数")
    ap.add_argument("--top-topic", type=int, default=10, help="每月每个方向展开详情的条数")
    a = ap.parse_args()

    if a.hf and Path(a.hf).exists():
        HF.update(json.loads(Path(a.hf).read_text(encoding="utf-8")))
    cache = json.loads(Path(a.cache).read_text(encoding="utf-8")) if a.cache and Path(a.cache).exists() else {}
    start = a.start or f"{a.year}-01-01"
    raw = [json.loads(l) for l in open(a.jsonl, encoding="utf-8")]
    papers = [p for p in raw if p["published"] >= start and p["published"].startswith(str(a.year)) and keep(p)]
    end = a.end or max(p["published"] for p in papers)
    papers = [p for p in papers if p["published"] <= end]
    for p in papers:
        p["topic"] = classify(p)
    print(f"保留 {len(papers)} / {len(raw)} 篇；方向分布：", dict(sorted(Counter(p['topic'] for p in papers).items())))

    DIGESTS.mkdir(exist_ok=True)
    DATA.mkdir(exist_ok=True)
    by_month = defaultdict(list)
    for p in papers:
        by_month[int(p["published"][5:7])].append(p)
    months_present = sorted(by_month)
    for m in months_present:
        ms = f"{a.year}-{m:02d}-01"
        me = min(end, max(p["published"] for p in by_month[m]))
        path = DIGESTS / f"{a.year}-{m:02d}-arxiv.md"
        path.write_text(build_month(a.year, m, by_month[m], cache, a.top, a.top_topic, max(ms, start), me), encoding="utf-8")
        print(f"  {path.relative_to(ROOT)}  {len(by_month[m])} 篇  {path.stat().st_size // 1024} KB")
    annual = DIGESTS / f"{a.year}-annual-arxiv.md"
    annual.write_text(build_annual(a.year, papers, cache, months_present, 100, 20, start, end), encoding="utf-8")
    print(f"  {annual.relative_to(ROOT)}")

    readme = DIGESTS / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        s, e = f"<!-- ARXIV-{a.year}:START -->", f"<!-- ARXIV-{a.year}:END -->"
        if s in text and e in text:
            rows = ["| 月份 | 篇数 | 本月最热 |", "|---|---:|---|"]
            for m in months_present:
                top = rank(by_month[m], cache)[0]
                rows.append(f"| [{a.year}-{m:02d}](./{a.year}-{m:02d}-arxiv.md) | {len(by_month[m])} | [{short(esc(top['title']))}](https://arxiv.org/abs/{top['id']}) |")
            rows.append(f"| [**全年总览**](./{a.year}-annual-arxiv.md) | **{len(papers)}** | 截至 {end} |")
            pre, rest = text.split(s, 1)
            readme.write_text(pre + s + "\n" + "\n".join(rows) + "\n" + e + rest.split(e, 1)[1], encoding="utf-8")
            print(f"  已更新 {readme.relative_to(ROOT)}")

    csv_path = DATA / f"arxiv-{a.year}.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["arxiv_id", "published", "topic_id", "topic", "title", "first_author", "n_authors", "primary_category", "citations", "venue", "url"])
        for p in rank(papers, cache):
            s2 = cache.get(p["id"])
            w.writerow([p["id"], p["published"], p["topic"], TOPIC_NAME[p["topic"]], p["title"], p["authors"][0] if p["authors"] else "",
                        len(p["authors"]), p["primary"], cites(s2), venue(p, s2), f"https://arxiv.org/abs/{p['id']}"])
    print(f"  {csv_path.relative_to(ROOT)}  {csv_path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
