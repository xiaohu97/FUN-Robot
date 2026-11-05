<div align="center">
  <h1>🤖 FUN-Robot</h1>
  <p><b>机器人与具身智能：经典论文 · 最新进展 · 开源项目</b></p>
  <p>Robotics & Embodied AI Paper Collection（中文友好、分类清晰、持续更新）</p>
  <p>
    <a href="./papers/README.md">📚 论文库</a> ·
    <a href="./papers/must-read.md">🧭 阅读路线</a> ·
    <a href="./digests/README.md">🗞 进展速递</a> ·
    <a href="./projects/README.md">🛠 开源项目</a> ·
    <a href="./datasets/README.md">📦 数据集</a> ·
    <a href="./benchmarks/README.md">📏 基准</a> ·
    <a href="./templates/">🧩 模板</a>
  </p>
</div>

---

## 这是什么

参考 [funNLP](https://github.com/fighting41love/funNLP) 的组织方式，把机器人 / 具身智能领域的论文整理成**按方向分类、经典与前沿分开、每篇一句话中文解读**的资料库，并配套**模板 + 脚本**，方便自己持续添加新论文。

适合：
- 想系统入门具身智能的同学 → 从 [🧭 阅读路线](./papers/must-read.md) 开始
- 想跟踪前沿的研究者 → 看各方向的「🚀 最新进展」和 [📅 2026 全量论文追踪](#-2026-全量论文追踪)
- 想动手复现的开发者 → 看 [🛠 开源项目](./projects/README.md)

## 📚 论文库（v2 · 18 个方向）

> 🆕 **2026-11 分类升级**：基于全年 14960 篇论文的趋势分析，新增 **世界动作模型、机器人智能体、奖励与失败恢复、记忆与长时程、触觉** 5 个方向，并把“强化学习与足式运动控制”拆成 **RL 后训练** 和 **足式运动控制** 两个方向。依据与归类规则见 [taxonomy.md](./taxonomy.md#v2-有什么变化)。

| # | 方向 | 代表工作 |
|---|---|---|
| | **A. 基础模型与智能体** | |
| 01 | [VLA 与机器人基础模型](./papers/01-vla-foundation-models.md) | RT-2 · OpenVLA · π0 / π0.5 / π0.7 · GR00T · Gemini Robotics · Qwen-VLA |
| 02 | [世界动作模型（WAM）🆕](./papers/02-world-action-models.md) | UniPi · DreamZero · Fast-WAM · LingBot-VA · Cosmos Policy · OpenWAM |
| 03 | [世界模型与视频生成](./papers/03-world-models.md) | Dreamer · UniSim · Genie · Cosmos 3 · V-JEPA 2 · DreamDojo |
| 04 | [具身推理与任务规划](./papers/04-embodied-reasoning-planning.md) | SayCan · VoxPoser · ReKep · RoboBrain 2.0 · MolmoAct2 |
| 05 | [机器人智能体与自我进化 🆕](./papers/05-robot-agents.md) | Code as Policies · Voyager · CaP-X · Show-Harness · OpenRUA · Zetta |
| | **B. 策略学习与改进** | |
| 06 | [模仿学习与策略学习](./papers/06-imitation-learning.md) | DAgger · Diffusion Policy · ACT · DP3 · Legato |
| 07 | [强化学习与后训练 🔀](./papers/07-rl-post-training.md) | PPO · SAC · HIL-SERL · DPPO · π\*0.6 · QAM |
| 08 | [奖励模型、失败检测与恢复 🆕](./papers/08-reward-failure-recovery.md) | Eureka · VIP · GVL · RoboReward · Robometer · AgentChord |
| 09 | [记忆与长时程任务 🆕](./papers/09-memory-long-horizon.md) | MemoryVLA · MEM · RoboMME · RMBench · EventVLA |
| | **C. 本体与技能** | |
| 10 | [足式运动控制 🔀](./papers/10-legged-locomotion.md) | RMA · legged_gym · Extreme Parkour · APT-RL |
| 11 | [人形机器人](./papers/11-humanoid.md) | DeepMimic · PHC · HumanPlus · ASAP · BeyondMimic · Ψ0 · Humanoid-GPT |
| 12 | [操作、抓取与灵巧手](./papers/12-manipulation-dexterous.md) | Dex-Net · Rubik's Cube · PerAct · DexterityGen · EgoScale |
| 13 | [触觉与接触感知 🆕](./papers/13-tactile.md) | DIGIT · 3D-ViTac · Sparsh · TacVLA · FTP-1 · N0-TWAM |
| 14 | [具身导航与移动操作](./papers/14-navigation.md) | R2R · ViNT · NoMaD · NaVILA · ABot-N1 · SuperNav |
| | **D. 感知** | |
| 15 | [视觉表征与 3D 场景理解](./papers/15-perception-representation.md) | R3M · VC-1 · F3RM · FoundationPose · V-JEPA 2.1 |
| | **E. 数据与基础设施** | |
| 16 | [数据采集、遥操作与人类视频](./papers/16-data-teleoperation.md) | ALOHA · UMI · DROID · AgiBot World · EgoVerse · HumanNet |
| 17 | [仿真、Sim2Real 与评测基准](./papers/17-simulation-benchmarks.md) | MuJoCo · Isaac Lab · LIBERO · SIMPLER · RoboDojo |
| 18 | [综述与教程](./papers/18-surveys.md) | VLA 综述 · WAM 综述 · 行为基础模型综述 |

### 收录统计

<!-- STATS:START -->
| 方向 | 经典 | 最新进展 | ⭐ 必读 | 合计 |
|---|---:|---:|---:|---:|
| [VLA 与机器人基础模型](papers/01-vla-foundation-models.md) | 7 | 34 | 9 | 41 |
| [世界动作模型（World-Action Model, WAM）🆕](papers/02-world-action-models.md) | 4 | 16 | 3 | 20 |
| [世界模型与视频生成](papers/03-world-models.md) | 6 | 11 | 7 | 17 |
| [具身推理与任务规划（LLM / VLM for Robotics）](papers/04-embodied-reasoning-planning.md) | 6 | 10 | 3 | 16 |
| [机器人智能体与自我进化（Robot-Use Agents / Embodied Harness）🆕](papers/05-robot-agents.md) | 2 | 16 | 2 | 18 |
| [模仿学习与策略学习](papers/06-imitation-learning.md) | 10 | 9 | 6 | 19 |
| [强化学习与后训练](papers/07-rl-post-training.md) | 5 | 9 | 4 | 14 |
| [奖励模型、失败检测与恢复 🆕](papers/08-reward-failure-recovery.md) | 6 | 12 | 3 | 18 |
| [记忆与长时程任务 🆕](papers/09-memory-long-horizon.md) | 0 | 12 | 2 | 12 |
| [足式运动控制](papers/10-legged-locomotion.md) | 6 | 8 | 5 | 14 |
| [人形机器人（运动、全身控制、移动操作与遥操作）](papers/11-humanoid.md) | 5 | 36 | 8 | 41 |
| [操作、抓取与灵巧手](papers/12-manipulation-dexterous.md) | 13 | 14 | 6 | 27 |
| [触觉与接触感知 🆕](papers/13-tactile.md) | 7 | 18 | 2 | 25 |
| [具身导航与移动操作](papers/14-navigation.md) | 7 | 18 | 3 | 25 |
| [视觉表征与 3D 场景理解](papers/15-perception-representation.md) | 4 | 10 | 3 | 14 |
| [数据采集、遥操作与人类视频](papers/16-data-teleoperation.md) | 2 | 21 | 6 | 23 |
| [仿真平台、Sim2Real 与评测基准](papers/17-simulation-benchmarks.md) | 7 | 19 | 7 | 26 |
| [综述与教程](papers/18-surveys.md) | 0 | 27 | 3 | 27 |
| **总计** | **97** | **300** | **82** | **397** |
<!-- STATS:END -->

## 📅 2026 全量论文追踪

除了人工精选的分类清单，仓库还用脚本抓取了 **2026 年 1 月 1 日至 11 月 5 日 arXiv 上的全部机器人 / 具身智能论文**（cs.RO 全部 13994 篇 + 其他分类中的具身论文 966 篇，共 **14960** 篇），自动分到 24 个方向（18 个论文库方向 + 6 个其他机器人方向），并按热度（引用数 + Hugging Face 点赞）排序：

- 📆 **按月**：[2026 全量月报索引](./digests/README.md)（每月一份，含当月最热 Top 15 与各方向清单）
- 🏆 **全年**：[2026 年度总览](./digests/2026-annual-arxiv.md)（月度 × 方向统计、年度最热 Top 100、各方向年度 Top 20）
- 📊 **表格**：[`data/arxiv-2026.csv`](./data/arxiv-2026.csv)（可用 Excel / pandas 自由筛选）
- 🔄 **更新**：`scripts/fetch_arxiv.py` → `fetch_citations.py` → `fetch_hf_upvotes.py` → `build_digest.py`，步骤见 [digests/README.md](./digests/README.md#-如何更新每月一次)

## 🔥 2026 前沿速览（基于全年 14960 篇论文的统计）

1. **[世界动作模型（WAM）](./papers/02-world-action-models.md) 爆发**：标题含 world-action / WAM 的论文从 1 月 0 篇增长到 10 月 81 篇（全年 298 篇）。年度引用最高的四篇论文（DreamZero、Fast-WAM、Cosmos Policy、LingBot-VA）全部是“视频模型 → 机器人策略”路线；Fast-WAM 发现收益主要来自训练时的视频协同训练，而不是测试时“想象未来”。
2. **VLA 仍是最大主线**：标题含 VLA 的论文全年 1286 篇，9–10 月每月 200+。重点从“更大的模型”转向[记忆](./papers/09-memory-long-horizon.md)（MEM、RoboMME）、[RL 后训练](./papers/07-rl-post-training.md)（π\*0.6、ACCRUE）、[奖励与失败恢复](./papers/08-reward-failure-recovery.md)（Robometer、LIBERO-RECOVER）、可引导性（π0.7）和[触觉](./papers/13-tactile.md)（TacVLA、N0-VTLA）。
3. **[“大模型 + 智能体框架”直接控制机器人](./papers/05-robot-agents.md)**：下半年出现大量 harness / 机器人智能体工作（CaP-X、Show-Harness、OpenRUA、Zetta），摘要提到 GPT-6 Astra 的论文 9–10 月共 53 篇。普遍结论：通用大模型语义能力强，但精细、动态与双臂控制仍明显不足。
4. **人类数据规模化**：EgoScale（2 万小时）、HumanNet（百万小时）、EgoVerse、UniDex 等用第一视角人类视频替代昂贵的遥操作，并观察到数据规模与性能的对数线性关系。
5. **人形机器人持续升温**：标题含 humanoid 的论文全年 588 篇，10 月达 133 篇。全身控制走向大规模动作预训练（Humanoid-GPT）与跨本体基础模型（Ψ0、X-WBC）。
6. **评测基础设施**：RoboDojo、RoboCasa365、RoboMemArena、WorldArena 等新基准与公开排行榜成为下半年论文的标准评测。

## ➕ 如何添加新论文

```bash
# 自动获取 arXiv 标题，插入指定方向的「最新进展」表格，并生成精读笔记
python scripts/new_paper.py 2410.24164 --short "π0" --topic 01 --summary "一句话贡献" --note

# 查重 + 检查链接 + 刷新上面的统计表
python scripts/check.py --update
```

| 模板 | 用途 |
|---|---|
| [`templates/paper-entry.md`](./templates/paper-entry.md) | 论文表格行（加入分类清单） |
| [`templates/paper-note.md`](./templates/paper-note.md) | 精读笔记（[示例：Diffusion Policy](./papers/notes/2303.04137-diffusion-policy.md)） |
| [`templates/digest.md`](./templates/digest.md) | 月度进展速递 |
| [`templates/project-entry.md`](./templates/project-entry.md) | 开源项目条目 |

完整流程与规范见 [CONTRIBUTING.md](./CONTRIBUTING.md)；分类与标签规则见 [taxonomy.md](./taxonomy.md)。

## 📁 仓库结构

```
├── papers/        # 论文库：18 个方向文件 + 必读路线 + notes/ 精读笔记
├── digests/       # 2026 全量月报 + 年度总览（14960 篇，自动生成）+ 专题速递
├── data/          # arxiv-2026.csv：全年论文表格（编号、日期、方向、标题、引用数…）
├── projects/      # 开源项目（框架、仿真器、人形控制、系统库）
├── datasets/      # 数据集
├── benchmarks/    # 评测基准与指标
├── templates/     # 所有模板
├── scripts/       # new_paper.py（新增论文）、check.py（查重 + 统计）、fetch_*/build_digest.py（全量追踪）
├── taxonomy.md    # 分类体系与标签词表
└── CONTRIBUTING.md
```

## 维护节奏建议

- **每月**：运行全量追踪脚本生成当月月报，从“本月最热”和各方向 Top 中挑选代表作，用 `new_paper.py` 升级进分类清单
- **每年初**：把超过 2 年的「最新进展」挪进「经典」或删除，更新阅读路线

欢迎通过 Issue（「📄 推荐论文」模板）或 PR 贡献。

## License

建议补充 MIT License（如需可直接添加 `LICENSE` 文件）。
