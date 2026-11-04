# 📏 评测基准

> 论文里“刷榜”最常见的基准，以及它们**到底在测什么**。基准对应的原始论文见 [`papers/11-simulation-benchmarks.md`](../papers/11-simulation-benchmarks.md)。

## 操作（Manipulation）

| 基准 | 平台 | 测什么 | 主要指标 | 常见于 | 链接 |
|---|---|---|---|---|---|
| **LIBERO** | robosuite / MuJoCo | 空间、物体、目标、长程 4 个子集的知识迁移 | 各子集成功率、平均成功率 | OpenVLA、π0、OFT 等 VLA 微调 | [代码](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| **SIMPLER** | SAPIEN | 复刻 Google Robot / WidowX 真机场景，衡量“仿真成绩能否预测真机” | 成功率；与真机的排序一致性 | RT-1、Octo、OpenVLA、π0 | [代码](https://github.com/simpler-env/SimplerEnv) |
| **CALVIN** | PyBullet | 语言条件下连续完成 5 个子任务 | 平均完成长度（Avg. Len，满分 5） | GR-1、3D Diffuser Actor | [代码](https://github.com/mees/calvin) |
| **RLBench** | CoppeliaSim | 100 个多样化操作任务（常用 18 任务子集） | 成功率 | PerAct、RVT、3D Diffuser Actor | [代码](https://github.com/stepjam/RLBench) |
| **ManiSkill3** | SAPIEN（GPU） | 操作、移动操作、灵巧手，支持大规模并行 RL | 成功率 | RL 与视觉策略 | [代码](https://github.com/haosulab/ManiSkill) |
| **RoboCasa** | robosuite | 大规模厨房日常任务 | 成功率 | 仿真数据 scaling | [代码](https://github.com/robocasa/robocasa) |
| **BEHAVIOR-1K** | OmniGibson | 1000 个家务活动，长程、真实感 | 任务成功率 | 家庭服务机器人 | [主页](https://behavior.stanford.edu/) |

## 导航（Navigation）

| 基准 | 平台 | 测什么 | 主要指标 | 链接 |
|---|---|---|---|---|
| **ObjectNav（HM3D）** | Habitat | 找到指定类别物体 | SR（成功率）、SPL（路径加权成功率） | [Habitat](https://github.com/facebookresearch/habitat-lab) |
| **R2R / R2R-CE** | Matterport3D / Habitat | 按自然语言指令导航（离散 / 连续环境） | SR、SPL、NE（导航误差） | [R2R](https://bringmeaspoon.org/) |

## 运动控制（Locomotion）

| 基准 / 环境 | 平台 | 测什么 | 常用指标 | 链接 |
|---|---|---|---|---|
| Isaac Lab 运动任务 | Isaac Sim | 四足/人形速度跟踪、复杂地形 | 速度跟踪误差、地形等级、存活率 | [代码](https://github.com/isaac-sim/IsaacLab) |
| MuJoCo Playground | MJX | 四足、人形、灵巧手 GPU 训练与 sim2real | 回报、成功率 | [代码](https://github.com/google-deepmind/mujoco_playground) |
| 动作跟踪（AMASS 测试集） | IsaacGym / IsaacLab | 人形跟踪参考动作的精度 | MPJPE、成功率 | 见 [`05-humanoid.md`](../papers/05-humanoid.md) |

## SOTA 记录（手动维护）

> 记录格式：`| 基准 | 设置 | 方法 | 成绩 | 来源论文 | 记录日期 |`。只记录论文中明确报告的数字，并写清来源。

| 基准 | 设置 | 方法 | 成绩 | 来源论文 | 记录日期 |
|---|---|---|---|---|---|
| | | | | | |
