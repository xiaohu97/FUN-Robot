# 🗂 分类体系与标签规范

本仓库用两层结构组织内容：

1. **一级分类 = 文件**：每篇论文只放进一个主方向文件（`papers/NN-*.md`），避免重复；
2. **标签 = 交叉维度**：在精读笔记的 `tags` 字段、月报中使用，表达“跨方向”的属性。

## 一级分类（12 个方向）

```
具身智能 Embodied AI
├── 大脑：理解与决策
│   ├── 01 VLA 与机器人基础模型        papers/01-vla-foundation-models.md
│   ├── 02 具身推理与任务规划          papers/02-embodied-reasoning-planning.md
│   └── 07 世界模型与视频生成          papers/07-world-models.md
├── 小脑：策略学习与控制
│   ├── 03 模仿学习与策略学习          papers/03-imitation-learning.md
│   ├── 04 强化学习与足式运动控制      papers/04-rl-locomotion.md
│   └── 05 人形机器人                  papers/05-humanoid.md
├── 身体：任务能力
│   ├── 06 操作、抓取与灵巧手          papers/06-manipulation-dexterous.md
│   └── 09 具身导航与移动操作          papers/09-navigation.md
├── 眼睛：感知与表征
│   └── 08 视觉表征与 3D 场景理解      papers/08-perception-representation.md
├── 燃料：数据与基础设施
│   ├── 10 数据采集、遥操作与数据集    papers/10-data-teleoperation.md
│   └── 11 仿真平台、Sim2Real 与基准   papers/11-simulation-benchmarks.md
└── 12 综述与教程                      papers/12-surveys.md
```

### 归类规则（一篇论文跨多个方向时）
| 情况 | 放到 |
|---|---|
| 人形机器人上的 VLA（如 GR00T） | 01（贡献核心是基础模型） |
| 人形全身控制 / 动作跟踪 / 全身遥操作 | 05 |
| 四足或通用的 RL 运动控制、真机 RL | 04 |
| 提出新数据采集系统或数据集 | 10 |
| 提出新仿真器或评测基准 | 11 |
| 用世界模型 / 视频模型生成动作或数据 | 07 |
| 用 LLM/VLM 做规划、写代码、空间推理 | 02 |

## 标签词表

> 新增标签前先查这张表，尽量复用；确实需要新标签时在 PR 中说明并补进来。

| 维度 | 标签 |
|---|---|
| 任务 | `locomotion` `manipulation` `loco-manipulation` `dexterous` `bimanual` `navigation` `whole-body-control` `teleoperation` `HRI` |
| 方法 | `VLA` `LLM-planning` `imitation-learning` `RL` `sim2real` `diffusion` `flow-matching` `world-model` `latent-action` `motion-tracking` `retargeting` `reward-design` |
| 本体 | `humanoid` `quadruped` `arm` `mobile-manipulator` `dexterous-hand` `drone` `cross-embodiment` |
| 输入 | `RGB` `depth` `point-cloud` `tactile` `proprioception` `language` `human-video` |
| 实验 | `sim` `real-world` `zero-shot` |
| 开放程度 | `open-source` `open-weights` `closed` |
| 应用场景 | `household` `factory` `warehouse` `retail` `logistics` `service` `healthcare` |
| 状态 | `classic` `sota` `reproducible` `must-read` `todo` |
