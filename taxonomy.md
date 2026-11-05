# 🗂 分类体系与标签规范（v2 · 2026-11）

本仓库用两层结构组织内容：

1. **一级分类 = 文件**：每篇论文只放进一个主方向文件（`papers/NN-*.md`），避免重复；
2. **标签 = 交叉维度**：在精读笔记的 `tags` 字段、月报中使用，表达“跨方向”的属性。

## v2 有什么变化？

v1 有 12 个方向。2026-11 用全年 14960 篇 arXiv 论文做了词频增长分析和 NMF 主题聚类（下半年对比上半年），发现几类快速增长的主题装不进原来的 12 个方向，于是扩展为 **18 个方向**：

| 变化 | 方向 | 依据（2026 年 arXiv 数据） |
|---|---|---|
| 🆕 新增 | **02 世界动作模型（WAM）** | 标题含 world-action / WAM：1 月 0 篇 → 10 月 81 篇；下半年占比是上半年的 6.2 倍 |
| 🆕 新增 | **05 机器人智能体与自我进化** | harness / robot-use agent / 自我进化类论文占比增长 5.3 倍；9–10 月 53 篇摘要提到 GPT-6 Astra |
| 🆕 新增 | **08 奖励模型、失败检测与恢复** | 聚类中 failure / recovery / test-time 主题增长 9.8 倍；通用奖励模型大量出现 |
| 🆕 新增 | **09 记忆与长时程任务** | 标题含 memory：上半年 59 篇 → 下半年 154 篇 |
| 🆕 拆分 | **13 触觉与接触感知**（自原 06 操作） | 全年 458 篇，触觉 VLA、触觉世界模型成为独立主线 |
| 🔀 拆分 | **07 强化学习与后训练** + **10 足式运动控制**（自原 04） | 通用 RL / VLA 后训练与足式运动控制是两个研究社区 |
| 🔢 重新编号 | 其余方向 | 按“基础模型 → 策略学习 → 本体与技能 → 感知 → 数据与基础设施”排序 |

> 本页的统计和月报中的自动分类都由 `scripts/build_digest.py` 中的 `TOPICS` 规则给出，规则与本页编号一一对应。

## 一级分类（18 个方向）

```
具身智能 Embodied AI
├── A. 基础模型与智能体（“大脑”）
│   ├── 01 VLA 与机器人基础模型          papers/01-vla-foundation-models.md
│   ├── 02 世界动作模型（WAM）🆕         papers/02-world-action-models.md
│   ├── 03 世界模型与视频生成            papers/03-world-models.md
│   ├── 04 具身推理与任务规划            papers/04-embodied-reasoning-planning.md
│   └── 05 机器人智能体与自我进化 🆕     papers/05-robot-agents.md
├── B. 策略学习与改进
│   ├── 06 模仿学习与策略学习            papers/06-imitation-learning.md
│   ├── 07 强化学习与后训练 🔀           papers/07-rl-post-training.md
│   ├── 08 奖励模型、失败检测与恢复 🆕   papers/08-reward-failure-recovery.md
│   └── 09 记忆与长时程任务 🆕           papers/09-memory-long-horizon.md
├── C. 本体与技能（“身体”）
│   ├── 10 足式运动控制 🔀               papers/10-legged-locomotion.md
│   ├── 11 人形机器人                    papers/11-humanoid.md
│   ├── 12 操作、抓取与灵巧手            papers/12-manipulation-dexterous.md
│   ├── 13 触觉与接触感知 🆕             papers/13-tactile.md
│   └── 14 具身导航与移动操作            papers/14-navigation.md
├── D. 感知（“眼睛”）
│   └── 15 视觉表征与 3D 场景理解        papers/15-perception-representation.md
├── E. 数据与基础设施（“燃料”）
│   ├── 16 数据采集、遥操作与人类视频    papers/16-data-teleoperation.md
│   └── 17 仿真、Sim2Real 与评测基准     papers/17-simulation-benchmarks.md
└── 18 综述与教程                        papers/18-surveys.md

F. 其他机器人方向（只在全量月报中自动追踪，暂不建人工清单）
   19 自动驾驶 · 20 空中、水下与空间机器人 · 21 SLAM、定位与建图
   22 运动规划与控制 · 23 多机器人与人机交互 · 24 医疗、软体与特种机器人 · 99 其他
```

### 归类规则（一篇论文跨多个方向时）

按下表**从上到下**匹配，命中即停：

| 情况 | 放到 |
|---|---|
| 综述、教程、路线图 | 18 |
| 以触觉 / 力觉为核心贡献（包括触觉 VLA、触觉世界模型） | 13 |
| 以记忆或长时程能力为核心贡献（包括记忆 VLA、记忆基准） | 09 |
| 大模型通过框架直接控制机器人、代码智能体、自我进化 | 05 |
| 奖励 / 进度 / 价值模型、成功检测、失败检测与恢复 | 08 |
| 同时预测未来画面与动作的视频-动作模型 | 02 |
| 用作模拟器、评测器、数据合成或表征的世界模型 | 03 |
| 视觉语言导航 / 导航基础模型 | 14 |
| 其余 VLA 与通用机器人策略（包括人形 VLA，如 GR00T） | 01 |
| 人形全身控制 / 动作跟踪 / 全身遥操作 / 人形移动操作 | 11 |
| 四足 / 双足 RL 运动控制 | 10 |
| 通用 RL 算法、真机 RL、RL 微调扩散策略或 VLA | 07 |
| 提出新数据采集系统、数据集、人类视频数据管线 | 16 |
| 提出新仿真器或评测基准 | 17 |
| 用 LLM/VLM 做规划、空间推理、具身推理模型 | 04 |

## 标签词表

> 新增标签前先查这张表，尽量复用；确实需要新标签时在 PR 中说明并补进来。

| 维度 | 标签 |
|---|---|
| 任务 | `locomotion` `manipulation` `loco-manipulation` `dexterous` `bimanual` `navigation` `whole-body-control` `teleoperation` `long-horizon` `HRI` |
| 方法 | `VLA` `WAM` `world-model` `LLM-planning` `agent-harness` `self-improvement` `imitation-learning` `RL` `post-training` `reward-model` `failure-recovery` `memory` `sim2real` `diffusion` `flow-matching` `latent-action` `motion-tracking` `retargeting` `in-context-learning` |
| 本体 | `humanoid` `quadruped` `arm` `mobile-manipulator` `dexterous-hand` `drone` `cross-embodiment` |
| 输入 | `RGB` `depth` `point-cloud` `tactile` `force` `proprioception` `language` `human-video` `egocentric` |
| 实验 | `sim` `real-world` `zero-shot` |
| 开放程度 | `open-source` `open-weights` `closed` |
| 应用场景 | `household` `factory` `warehouse` `retail` `logistics` `service` `healthcare` |
| 状态 | `classic` `sota` `reproducible` `must-read` `todo` |
