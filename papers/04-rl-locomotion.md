# 04 · 强化学习与足式运动控制

> 用强化学习（多在仿真中大规模训练）获得鲁棒的运动/操作策略，再迁移到真机。四足机器人是这一路线最成功的落地场景，也是人形控制的技术源头。
> 主线：**真机大规模 RL（QT-Opt）→ 执行器网络 + 仿真 RL（ANYmal）→ 教师-学生特权蒸馏 → RMA 在线自适应 → GPU 大规模并行（分钟级训练）→ 感知跑酷 → 真机人在回路 RL**

⭐ = 必读　｜　人形专题见 [`05-humanoid.md`](./05-humanoid.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **QT-Opt** · Scalable Deep RL for Vision-Based Robotic Manipulation | 2018 · CoRL'18 | 7 台机械臂 58 万次真机抓取的离策略视觉 RL，抓取成功率 96% | [arXiv](https://arxiv.org/abs/1806.10293) |
| ⭐ **ANYmal Agile Skills** · Learning Agile and Dynamic Motor Skills for Legged Robots | 2019 · Science Robotics | 用神经网络建模执行器 + 仿真 RL，首次让四足在真机上做出敏捷动作与摔倒恢复 | [arXiv](https://arxiv.org/abs/1901.08652) |
| ⭐ **Teacher-Student Locomotion** · Learning Quadrupedal Locomotion over Challenging Terrain | 2020 · Science Robotics | 特权信息教师 → 本体感知学生的蒸馏范式，ANYmal 在野外复杂地形“盲走” | [arXiv](https://arxiv.org/abs/2010.11251) |
| **Cassie All Gaits** · Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition | 2020 · ICRA'21 | 周期性奖励组合统一学习走、跑、跳、单脚等双足步态，并迁移到 Cassie 真机 | [arXiv](https://arxiv.org/abs/2011.01387) |
| ⭐ **RMA** · Rapid Motor Adaptation for Legged Robots | 2021 · RSS'21 | 在线估计环境“外参”潜变量，让低成本四足零样本适应沙地、油面、负载等 | [arXiv](https://arxiv.org/abs/2107.04034) |
| ⭐ **legged_gym** · Learning to Walk in Minutes Using Massively Parallel Deep RL | 2021 · CoRL'21 | Isaac Gym 上数千环境并行 PPO + 地形课程，分钟级训练出可上真机的步态 | [arXiv](https://arxiv.org/abs/2109.11978) · [代码](https://github.com/leggedrobotics/legged_gym) |
| **Perceptive Locomotion in the Wild** · Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild | 2022 · Science Robotics | 注意力式 belief encoder 融合外部感知与本体感知，感知出错时也能稳健行走 | [arXiv](https://arxiv.org/abs/2201.08117) |

## 🚀 最新进展（2023 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **ANYmal Parkour** · Learning Agile Navigation for Quadrupedal Robots | 2023 · Science Robotics | 感知 + 运动 + 导航分层模块，四足完成跳跃、攀爬、钻越等跑酷动作 | [arXiv](https://arxiv.org/abs/2306.14874) |
| **Robot Parkour Learning** | 2023 · CoRL'23 | 软约束到硬约束的 RL 课程 + 蒸馏，低成本四足学会攀爬、跳跃、钻洞 | [arXiv](https://arxiv.org/abs/2309.05665) |
| ⭐ **Extreme Parkour** · Extreme Parkour with Legged Robots | 2023 · ICRA'24 | 单个前视深度相机端到端策略，低成本四足跳过 2 倍身高障碍 | [arXiv](https://arxiv.org/abs/2309.14341) |
| ⭐ **HIL-SERL** · Precise and Dexterous Robotic Manipulation via Human-in-the-Loop RL | 2024 · Science Robotics | 示教 + 人工纠正 + 高效离策略 RL，1~2.5 小时真机训练达到接近 100% 成功率 | [arXiv](https://arxiv.org/abs/2410.21845) |

> 2026 年 1-2 月 arXiv 中大量人形运动控制论文的逐篇清单见 [`digests/2026-01-02-arxiv-humanoid.md`](../digests/2026-01-02-arxiv-humanoid.md)。
