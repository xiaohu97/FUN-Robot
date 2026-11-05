# 📚 论文库

按**研究方向**组织，每个方向一个文件，文件内统一分为两部分：

- 🏛 **经典论文**：奠定范式、被广泛引用和复现的工作
- 🚀 **最新进展**：近 2 年的前沿工作（持续更新）

不知道从哪读起 → [🧭 必读清单与阅读路线](./must-read.md)　｜　精读笔记 → [📝 notes/](./notes/README.md)　｜　按月追踪新论文 → [🗞 digests/](../digests/README.md)

## 分类索引（v2 · 18 个方向）

> 2026-11 根据全年 14960 篇论文的趋势分析，从 12 个方向扩展为 18 个（🆕 新增 · 🔀 拆分），变化说明见 [`taxonomy.md`](../taxonomy.md#v2-有什么变化)。

| # | 方向 | 关注什么 |
|---|---|---|
| | **A. 基础模型与智能体** | |
| 01 | [VLA 与机器人基础模型](./01-vla-foundation-models.md) | RT 系列、OpenVLA、π 系列、GR00T、Gemini Robotics、Qwen-VLA |
| 02 | [世界动作模型（WAM）🆕](./02-world-action-models.md) | DreamZero、Fast-WAM、LingBot-VA、OpenWAM：视频 + 动作联合建模 |
| 03 | [世界模型与视频生成](./03-world-models.md) | Dreamer、UniSim、Cosmos、V-JEPA、DreamDojo |
| 04 | [具身推理与任务规划](./04-embodied-reasoning-planning.md) | LLM/VLM 规划、空间推理、具身推理模型 |
| 05 | [机器人智能体与自我进化 🆕](./05-robot-agents.md) | 代码即策略智能体、Embodied Harness、大模型直接控制、自我进化 |
| | **B. 策略学习与改进** | |
| 06 | [模仿学习与策略学习](./06-imitation-learning.md) | BC、Diffusion Policy、ACT、动作分块、上下文学习 |
| 07 | [强化学习与后训练 🔀](./07-rl-post-training.md) | PPO/SAC、真机 RL、扩散策略与 VLA 的 RL 后训练 |
| 08 | [奖励模型、失败检测与恢复 🆕](./08-reward-failure-recovery.md) | 通用奖励/进度/价值模型、成功检测、运行时监控、失败恢复 |
| 09 | [记忆与长时程任务 🆕](./09-memory-long-horizon.md) | 记忆增强 VLA、记忆基准、长程任务 |
| | **C. 本体与技能** | |
| 10 | [足式运动控制 🔀](./10-legged-locomotion.md) | 四足/双足 RL、sim2real、跑酷 |
| 11 | [人形机器人](./11-humanoid.md) | 动作跟踪、全身控制、人形移动操作、全身遥操作 |
| 12 | [操作、抓取与灵巧手](./12-manipulation-dexterous.md) | 抓取检测、3D 操作策略、灵巧手 |
| 13 | [触觉与接触感知 🆕](./13-tactile.md) | 触觉传感器与表征、视触觉策略、触觉 VLA / 世界模型 |
| 14 | [具身导航与移动操作](./14-navigation.md) | VLN、ObjectNav、导航基础模型、智能体式导航 |
| | **D. 感知** | |
| 15 | [视觉表征与 3D 场景理解](./15-perception-representation.md) | 预训练视觉表征、特征场、场景图、6D 位姿 |
| | **E. 数据与基础设施** | |
| 16 | [数据采集、遥操作与人类视频](./16-data-teleoperation.md) | ALOHA、UMI、DROID、第一视角人类视频 |
| 17 | [仿真、Sim2Real 与评测基准](./17-simulation-benchmarks.md) | MuJoCo、Isaac Lab、LIBERO、RoboDojo |
| 18 | [综述与教程](./18-surveys.md) | 各方向综述 |

## 收录统计

> 由 `python scripts/check.py --update` 自动生成，请勿手改。

<!-- STATS:START -->
| 方向 | 经典 | 最新进展 | ⭐ 必读 | 合计 |
|---|---:|---:|---:|---:|
| [VLA 与机器人基础模型](./01-vla-foundation-models.md) | 7 | 34 | 9 | 41 |
| [世界动作模型（World-Action Model, WAM）🆕](./02-world-action-models.md) | 4 | 16 | 3 | 20 |
| [世界模型与视频生成](./03-world-models.md) | 6 | 11 | 7 | 17 |
| [具身推理与任务规划（LLM / VLM for Robotics）](./04-embodied-reasoning-planning.md) | 6 | 10 | 3 | 16 |
| [机器人智能体与自我进化（Robot-Use Agents / Embodied Harness）🆕](./05-robot-agents.md) | 2 | 16 | 2 | 18 |
| [模仿学习与策略学习](./06-imitation-learning.md) | 10 | 9 | 6 | 19 |
| [强化学习与后训练](./07-rl-post-training.md) | 5 | 9 | 4 | 14 |
| [奖励模型、失败检测与恢复 🆕](./08-reward-failure-recovery.md) | 6 | 12 | 3 | 18 |
| [记忆与长时程任务 🆕](./09-memory-long-horizon.md) | 0 | 12 | 2 | 12 |
| [足式运动控制](./10-legged-locomotion.md) | 6 | 8 | 5 | 14 |
| [人形机器人（运动、全身控制、移动操作与遥操作）](./11-humanoid.md) | 5 | 36 | 8 | 41 |
| [操作、抓取与灵巧手](./12-manipulation-dexterous.md) | 13 | 14 | 6 | 27 |
| [触觉与接触感知 🆕](./13-tactile.md) | 7 | 18 | 2 | 25 |
| [具身导航与移动操作](./14-navigation.md) | 7 | 18 | 3 | 25 |
| [视觉表征与 3D 场景理解](./15-perception-representation.md) | 4 | 10 | 3 | 14 |
| [数据采集、遥操作与人类视频](./16-data-teleoperation.md) | 2 | 21 | 6 | 23 |
| [仿真平台、Sim2Real 与评测基准](./17-simulation-benchmarks.md) | 7 | 19 | 7 | 26 |
| [综述与教程](./18-surveys.md) | 0 | 27 | 3 | 27 |
| **总计** | **97** | **300** | **82** | **397** |
<!-- STATS:END -->

## 如何新增一篇论文？

1. 看 [`templates/paper-entry.md`](../templates/paper-entry.md) 了解字段规范；
2. 用脚本插入（推荐）：
   ```bash
   python scripts/new_paper.py <arXiv编号> --short "简称" --topic <01~18> --summary "一句话贡献"
   ```
   或手动复制模板中的表格行，粘贴到对应文件的表格末尾；
3. 精读后加 `--note` 生成笔记（模板：[`templates/paper-note.md`](../templates/paper-note.md)）；
4. 运行 `python scripts/check.py --update` 查重并刷新统计。

详细规范见 [CONTRIBUTING.md](../CONTRIBUTING.md)。
