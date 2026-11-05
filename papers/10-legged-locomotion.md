# 10 · 足式运动控制

> 用强化学习（多在仿真中大规模训练）获得鲁棒的足式运动策略，再迁移到真机。四足是这一路线最成功的落地场景，也是人形控制的技术源头。
> 主线：**执行器网络 + 仿真 RL（ANYmal）→ 教师-学生特权蒸馏 → RMA 在线自适应 → GPU 大规模并行（分钟级训练）→ 感知跑酷 → 2026：注意力地图编码、MoE 策略、在线本体自适应**

> 人形专题见 [`11`](./11-humanoid.md)；通用 RL 算法与后训练见 [`07`](./07-rl-post-training.md)。

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
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
| **Neural Map Encoding Locomotion** · Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding | 2026 · T-RO | 注意力式地形地图编码器 + 带不确定性的学习式建图，统一 RL 框架实现敏捷且可泛化的足式运动 | [arXiv](https://arxiv.org/abs/2601.08485) |
| **MoE Quadruped + RoboGauge** · Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion | 2026 · RSS'26 | 混合专家四足运动策略 + 量化 sim2real 可迁移性的预测评估套件 RoboGauge | [arXiv](https://arxiv.org/abs/2602.00678) |
| **APT-RL** · Agile perceptive multi-skill locomotion for quadrupedal robots in the wild | 2026 · Science Robotics | 动作预训练 Transformer + RL，四足仅用机载感知与计算在野外高速多技能切换 | [arXiv](https://arxiv.org/abs/2607.13579) |
| **Rapid Embodiment Adaptation for Quadrupedal Locomotion** | 2026 · arXiv | 从短交互历史在线推断本体参数，让一个通用四足策略适应不同硬件状态 | [arXiv](https://arxiv.org/abs/2608.01506) |
| **OmniQuad** · a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels | 2026 · arXiv | 麦克纳姆轮足复合四足机器人，结合轮式高效与腿式越障 | [arXiv](https://arxiv.org/abs/2610.38502) |

## 🔗 相关

> 2026 年 1-2 月 arXiv 中大量人形运动控制论文的逐篇清单见 [`digests/2026-01-02-arxiv-humanoid.md`](../digests/2026-01-02-arxiv-humanoid.md)。

> 📅 **2026 年本方向全部 439 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#10)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
