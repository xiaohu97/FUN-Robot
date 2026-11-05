# 📚 论文库

按**研究方向**组织，每个方向一个文件，文件内统一分为两部分：

- 🏛 **经典论文**：奠定范式、被广泛引用和复现的工作
- 🚀 **最新进展**：近 2 年的前沿工作（持续更新）

不知道从哪读起 → [🧭 必读清单与阅读路线](./must-read.md)　｜　精读笔记 → [📝 notes/](./notes/README.md)　｜　按月追踪新论文 → [🗞 digests/](../digests/README.md)

## 分类索引

| # | 方向 | 关注什么 |
|---|---|---|
| 01 | [VLA 与机器人基础模型](./01-vla-foundation-models.md) | RT 系列、OpenVLA、π 系列、GR00T、Gemini Robotics |
| 02 | [具身推理与任务规划](./02-embodied-reasoning-planning.md) | LLM/VLM 做规划、代码策略、空间推理、奖励设计 |
| 03 | [模仿学习与策略学习](./03-imitation-learning.md) | BC、Diffusion Policy、ACT、3D 策略、数据规律 |
| 04 | [强化学习与足式运动控制](./04-rl-locomotion.md) | 四足/双足 RL、sim2real、跑酷、真机 RL |
| 05 | [人形机器人](./05-humanoid.md) | 动作跟踪、全身控制、全身遥操作、行为基础模型 |
| 06 | [操作、抓取与灵巧手](./06-manipulation-dexterous.md) | 抓取检测、3D 操作策略、灵巧手、触觉 |
| 07 | [世界模型与视频生成](./07-world-models.md) | Dreamer、UniSim、Cosmos、V-JEPA、World-Action Model |
| 08 | [视觉表征与 3D 场景理解](./08-perception-representation.md) | 预训练视觉表征、特征场、场景图、6D 位姿 |
| 09 | [具身导航与移动操作](./09-navigation.md) | VLN、ObjectNav、导航基础模型 |
| 10 | [数据采集、遥操作与数据集](./10-data-teleoperation.md) | ALOHA、UMI、DROID、MimicGen、AgiBot World |
| 11 | [仿真平台、Sim2Real 与评测基准](./11-simulation-benchmarks.md) | MuJoCo、Isaac、LIBERO、SIMPLER |
| 12 | [综述与教程](./12-surveys.md) | 各方向综述 |

## 收录统计

> 由 `python scripts/check.py --update` 自动生成，请勿手改。

<!-- STATS:START -->
| 方向 | 经典 | 最新进展 | ⭐ 必读 | 合计 |
|---|---:|---:|---:|---:|
| [VLA 与机器人基础模型](./01-vla-foundation-models.md) | 7 | 37 | 10 | 44 |
| [具身推理与任务规划（LLM / VLM for Robotics）](./02-embodied-reasoning-planning.md) | 10 | 25 | 5 | 35 |
| [模仿学习与策略学习](./03-imitation-learning.md) | 10 | 13 | 6 | 23 |
| [强化学习与足式运动控制](./04-rl-locomotion.md) | 7 | 13 | 6 | 20 |
| [人形机器人（运动、全身控制与遥操作）](./05-humanoid.md) | 5 | 34 | 8 | 39 |
| [操作、抓取与灵巧手](./06-manipulation-dexterous.md) | 13 | 21 | 6 | 34 |
| [世界模型与视频生成](./07-world-models.md) | 6 | 30 | 10 | 36 |
| [视觉表征与 3D 场景理解](./08-perception-representation.md) | 4 | 10 | 3 | 14 |
| [具身导航与移动操作](./09-navigation.md) | 7 | 18 | 3 | 25 |
| [数据采集、遥操作与大规模数据集](./10-data-teleoperation.md) | 2 | 21 | 6 | 23 |
| [仿真平台、Sim2Real 与评测基准](./11-simulation-benchmarks.md) | 7 | 22 | 7 | 29 |
| [综述与教程](./12-surveys.md) | 0 | 26 | 3 | 26 |
| **总计** | **78** | **270** | **73** | **348** |
<!-- STATS:END -->

## 如何新增一篇论文？

1. 看 [`templates/paper-entry.md`](../templates/paper-entry.md) 了解字段规范；
2. 用脚本插入（推荐）：
   ```bash
   python scripts/new_paper.py <arXiv编号> --short "简称" --topic <01~12> --summary "一句话贡献"
   ```
   或手动复制模板中的表格行，粘贴到对应文件的表格末尾；
3. 精读后加 `--note` 生成笔记（模板：[`templates/paper-note.md`](../templates/paper-note.md)）；
4. 运行 `python scripts/check.py --update` 查重并刷新统计。

详细规范见 [CONTRIBUTING.md](../CONTRIBUTING.md)。
