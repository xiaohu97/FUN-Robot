# 贡献与维护指南

本仓库的目标是：**分类清晰、条目准确、易于持续更新**。下面是新增内容的统一流程。

## 一、仓库结构

```
FUN-Robot/
├── README.md                  # 总入口：导航 + 统计 + 精选
├── CONTRIBUTING.md            # 本文件
├── taxonomy.md                # 分类体系 + 标签词表
├── papers/                    # 📚 论文库（按方向）
│   ├── README.md              #    分类索引 + 自动统计
│   ├── must-read.md           #    必读清单与阅读路线
│   ├── 01-vla-foundation-models.md
│   ├── ...                    #    共 12 个方向，每个文件分「🏛 经典」「🚀 最新进展」
│   ├── 12-surveys.md
│   └── notes/                 #    📝 精读笔记（一篇一个文件）
├── digests/                   # 🗞 全量月报 + 年度总览（脚本生成）+ 专题速递
├── data/                      # 📊 arxiv-<年>.csv 全量论文表格
├── projects/                  # 🛠 开源项目
├── datasets/                  # 📦 数据集
├── benchmarks/                # 📏 评测基准
├── templates/                 # 🧩 模板
│   ├── paper-entry.md         #    论文表格行（加入分类清单）
│   ├── paper-note.md          #    精读笔记
│   ├── digest.md              #    月度速递
│   └── project-entry.md       #    开源项目条目
└── scripts/
    ├── new_paper.py           #    按模板新增论文（自动拉 arXiv 标题、插表、建笔记）
    ├── check.py               #    查重 + 链接检查 + 刷新统计
    ├── fetch_arxiv.py         #    抓取某时间段 arXiv 机器人/具身论文（全量）
    ├── fetch_citations.py     #    Semantic Scholar 引用数与 TL;DR
    ├── fetch_hf_upvotes.py    #    Hugging Face Daily Papers 点赞数
    └── build_digest.py        #    自动分类 → 月报 / 年度总览 / CSV
```

## 二、新增一篇论文（3 步）

**1）决定放哪里**：按 [`taxonomy.md`](./taxonomy.md) 的归类规则选**一个**主方向；近 2 年的放「🚀 最新进展」，奠基性老论文放「🏛 经典论文」。

**2）写入条目**（二选一）

- 脚本（推荐，能联网时自动获取标题和年份）：
  ```bash
  python scripts/new_paper.py 2410.24164 --short "π0" --topic 01 --venue "RSS'25" \
      --summary "VLM + flow matching 动作专家，输出 50Hz 连续动作，完成叠衣服等长程灵巧任务" \
      --code https://github.com/Physical-Intelligence/openpi
  ```
  无法访问 arXiv 时加上 `--title "..." --year 2024`。加 `--section classic` 放入经典，加 `--star` 标记必读，加 `--note` 同时生成精读笔记。
- 手动：复制 [`templates/paper-entry.md`](./templates/paper-entry.md) 里的表格行，粘贴到对应表格末尾（按年份升序）。

**3）检查**
```bash
python scripts/check.py --update
```
会检查重复收录、arXiv 链接是否带版本号、笔记链接是否存在，并刷新 README 中的统计表。

## 三、写精读笔记

```bash
python scripts/new_paper.py 2303.04137 --short "Diffusion Policy" --note   # 只建笔记，不插表
```
然后按 [`templates/paper-note.md`](./templates/paper-note.md) 的 7 个小节填写，示例见 [`papers/notes/2303.04137-diffusion-policy.md`](./papers/notes/2303.04137-diffusion-policy.md)。写完后在 [`papers/notes/README.md`](./papers/notes/README.md) 的索引表加一行。

## 四、月度更新（全量追踪 + 精选）

1. 按 [`digests/README.md`](./digests/README.md#-如何更新每月一次) 的 4 条命令重新生成全量月报（全自动）；
2. 打开当月月报，从「🔥 本月最热」和各方向 Top 10 中挑选代表作，用 `new_paper.py` 写入分类清单；
3. 需要人工点评的专题速递：复制 [`templates/digest.md`](./templates/digest.md) 到 `digests/YYYY-MM-主题.md`，并在 `digests/README.md` 的「专题速递」表格登记。

## 五、质量规范

- **链接**：arXiv 一律用 `https://arxiv.org/abs/编号`，不带 `v1/v2`；
- **一句话贡献**：中文 ≤ 60 字，写“做了什么 + 怎么做 + 为什么重要”，不要只翻译标题；
- **事实核对**：会议、数字以论文 / 官方页面为准；不确定的会议写 `arXiv`；
- **⭐ 必读**：每个方向不超过 1/3，宁缺毋滥；
- **定期整理**：每年初把“最新进展”中超过 2 年的条目挪到“经典”或删除。

## 六、提交

- 推荐论文但不想改文件：用 Issue 模板「📄 推荐论文」；
- 提交 PR 前运行一次 `python scripts/check.py`，确保无报错。
