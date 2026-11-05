# 🗞 最新进展速递（按时间）

分类清单（`papers/`）回答“这个方向有哪些重要论文”，速递回答“最近发生了什么”。速递分两类：

| 类型 | 内容 | 生成方式 |
|---|---|---|
| **全量月报** `YYYY-MM-arxiv.md` | 当月 arXiv **cs.RO 全部论文** + 其他分类中的具身智能论文，自动分到 24 个方向（18 个论文库方向 + 6 个其他机器人方向），按热度排序 | 脚本自动生成 |
| **精选速递 / 专题** `YYYY-MM-主题.md` | 人工挑选的 Top 论文、趋势观察、中文解读 | 按 [`templates/digest.md`](../templates/digest.md) 手写 |

## 📅 2026 全量月报

<!-- ARXIV-2026:START -->
| 月份 | 篇数 | 本月最热 |
|---|---:|---|
| [2026-01](./2026-01-arxiv.md) | 749 | [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Pl…](https://arxiv.org/abs/2601.16163) |
| [2026-02](./2026-02-arxiv.md) | 1122 | [World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922) |
| [2026-03](./2026-03-arxiv.md) | 1619 | [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666) |
| [2026-04](./2026-04-arxiv.md) | 1058 | [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emerg…](https://arxiv.org/abs/2604.15483) |
| [2026-05](./2026-05-arxiv.md) | 1357 | [MolmoAct2: Action Reasoning Models for Real-world Deployment](https://arxiv.org/abs/2605.02881) |
| [2026-06](./2026-06-arxiv.md) | 1622 | [Cosmos 3: Omnimodal World Models for Physical AI](https://arxiv.org/abs/2606.02800) |
| [2026-07](./2026-07-arxiv.md) | 1267 | [RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluati…](https://arxiv.org/abs/2607.04434) |
| [2026-08](./2026-08-arxiv.md) | 1269 | [Zetta $ζ$: An Efficient Closed-Loop Embodied Harness for Self-Evolvin…](https://arxiv.org/abs/2608.16590) |
| [2026-09](./2026-09-arxiv.md) | 2302 | [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522) |
| [2026-10](./2026-10-arxiv.md) | 2367 | [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Represe…](https://arxiv.org/abs/2610.37381) |
| [2026-11](./2026-11-arxiv.md) | 228 | [Route Anything: A Study of Model and Policy Routing for General-Purpo…](https://arxiv.org/abs/2611.05275) |
| [**全年总览**](./2026-annual-arxiv.md) | **14960** | 截至 2026-11-05 |
<!-- ARXIV-2026:END -->

> 全部论文的表格版（可用 Excel / pandas 筛选）：[`data/arxiv-2026.csv`](../data/arxiv-2026.csv)

## 🧩 专题速递

| 期号 | 范围 | 篇数 | 说明 |
|---|---|---|---|
| [2026-01-02 arXiv humanoid](./2026-01-02-arxiv-humanoid.md) | 2026-01-01 ~ 2026-02-28，关键词 `humanoid` | 109 | 自动初版：按方向分类 + 摘要首句 |

## 🔄 如何更新（每月一次）

```bash
# 1. 抓取 arXiv（cs.RO 全部 + 其他分类的具身智能论文），约 1~2 分钟/月
python scripts/fetch_arxiv.py --start 2026-01-01 --end 2026-11-30 --out data/raw-2026.jsonl

# 2. 补充引用数与 TL;DR（Semantic Scholar，带缓存，可断点续跑）
python scripts/fetch_citations.py data/raw-2026.jsonl --cache data/s2-cache.json --refresh

# 3. 补充 Hugging Face Daily Papers 点赞数（新论文引用很低时用于排序）
python scripts/fetch_hf_upvotes.py --start 2026-01-01 --end 2026-11-30 --out data/hf-upvotes.json

# 4. 分类并生成月报、年度总览、CSV，同时刷新本页索引
python scripts/build_digest.py data/raw-2026.jsonl --cache data/s2-cache.json --hf data/hf-upvotes.json --year 2026
```

- `data/raw-*.jsonl`（含完整摘要）、`data/s2-cache.json`、`data/hf-upvotes.json` 体积较大且可重新生成，已在 `.gitignore` 中忽略；仓库只保存生成后的月报与 CSV。
- **热度** = 引用数 + 0.5 × Hugging Face 点赞数。Semantic Scholar 记录的发表年份明显早于上传年份的“旧作新传”不计引用。
- **统计口径**：以 arXiv v1 提交日期为准；cs.RO 全部收录，其他分类（cs.CV / cs.AI / cs.LG / cs.CL / cs.HC / eess.SY）需标题含机器人/具身关键词或摘要多次命中。

之后从月报里挑出值得长期保留的论文，用 `scripts/new_paper.py` 写进 `papers/NN-*.md` 的「🚀 最新进展」表格。

## 方向编号说明

01~18 与 [`papers/`](../papers/README.md) 的分类文件一一对应（v2 分类，见 [`taxonomy.md`](../taxonomy.md)）；19~24 是论文库暂未单独建清单的其他机器人方向：
19 自动驾驶 · 20 空中、水下与空间机器人 · 21 SLAM、定位与建图 · 22 运动规划与控制 · 23 多机器人与人机交互 · 24 医疗、软体与特种机器人 · 99 其他。
