# 07 · 强化学习与后训练

> 原“强化学习与足式运动控制”拆分而来：本文件收录**通用 RL 算法、真机 RL，以及用 RL 对扩散/flow 策略和 VLA 做后训练**；足式运动控制见 [`10`](./10-legged-locomotion.md)。
> 主线：**PPO / SAC（基础算法）→ QT-Opt（大规模真机 RL）→ HIL-SERL（人在回路真机 RL）→ DPPO（RL 微调扩散策略）→ π\*0.6 / RECAP（VLA 从经验中学习）→ 2026：QAM / TRQAM、持续离策略 RL、机群经验学习**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典与奠基工作

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **PPO** · Proximal Policy Optimization Algorithms | 2017 · arXiv | 裁剪目标的稳定策略梯度算法，几乎所有仿真并行 RL（足式、人形、灵巧手）的默认选择 | [arXiv](https://arxiv.org/abs/1707.06347) |
| ⭐ **SAC** · Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL with a Stochastic Actor | 2018 · ICML'18 | 最大熵离策略 actor-critic，样本效率高，真机 RL 与 RL 微调的常用基础算法 | [arXiv](https://arxiv.org/abs/1801.01290) |
| **QT-Opt** · Scalable Deep RL for Vision-Based Robotic Manipulation | 2018 · CoRL'18 | 7 台机械臂 58 万次真机抓取的离策略视觉 RL，抓取成功率 96% | [arXiv](https://arxiv.org/abs/1806.10293) |
| **DPPO** · Diffusion Policy Policy Optimization | 2024 · ICLR'25 | 用策略梯度直接微调预训练扩散策略，打通“模仿预训练 → RL 精调” | [arXiv](https://arxiv.org/abs/2409.00588) |
| ⭐ **HIL-SERL** · Precise and Dexterous Robotic Manipulation via Human-in-the-Loop RL | 2024 · Science Robotics | 示教 + 人工纠正 + 高效离策略 RL，1~2.5 小时真机训练达到接近 100% 成功率 | [arXiv](https://arxiv.org/abs/2410.21845) |

## 🚀 最新进展（2025 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **π\*0.6** · a VLA That Learns From Experience | 2025 · arXiv | RECAP：融合示教、自主经验与人工纠正的优势条件 RL，难任务吞吐翻倍、失败率约减半 | [arXiv](https://arxiv.org/abs/2511.14759) · [博客](https://pi.website/blog/pistar06) |
| **QAM** · Q-learning with Adjoint Matching | 2026 · arXiv | 借用生成模型中的 adjoint matching 技术，稳定地用 Q 函数优化扩散/flow 策略 | [arXiv](https://arxiv.org/abs/2601.14234) |
| **USER** · A Unified and Extensible System for Real-World Online Policy Learning in Embodied AI | 2026 · RSS'26 | 面向真实世界在线策略学习的统一系统：硬件抽象层、云边协同训练、多机器人与长时异步训练 | [arXiv](https://arxiv.org/abs/2602.07837) |
| **DICE-RL** · From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning | 2026 · arXiv | 把 RL 当作“分布收缩”算子：残差离策略 RL 精调预训练扩散/flow 策略，从像素学会长程操作技能 | [arXiv](https://arxiv.org/abs/2603.10263) |
| **OmniReset** · Emergent Dexterity via Diverse Resets and Large-Scale Reinforcement Learning | 2026 · arXiv | 多样化重置 + 大规模在线 RL，单一奖励、固定超参、无课程无示教即可解决一大类灵巧操作任务 | [arXiv](https://arxiv.org/abs/2603.15789) |
| **FlashSAC** · Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control | 2026 · RSS'26 | 快速稳定的离策略 SAC 变体，在 10 个仿真器 60+ 任务上优于 PPO，人形 sim2real 训练从数小时降到分钟级 | [arXiv](https://arxiv.org/abs/2604.04539) |
| **TRQAM** · Trust Region Q Adjoint Matching | 2026 · NeurIPS'26 | 在 QAM 上加入路径空间 KL 信赖域，避免评论家误差被放大，稳定地离策略精调预训练策略 | [arXiv](https://arxiv.org/abs/2605.27079) |
| **ACCRUE** · Continual Off-Policy Reinforcement Learning for Robot Foundation Models | 2026 · arXiv | 面向机器人基础模型的持续离策略 RL：学新任务几乎不遗忘，真机训练时间减少 31%~68.5% | [arXiv](https://arxiv.org/abs/2610.18596) |
| **Collective Experience Learning** · Learning from Fleet Experience: Collective Experience Learning Across 96 Robots | 2026 · arXiv | 96 台机器人汇聚部署中的执行经验更新共享策略再下发给机群，减少对专家纠正的依赖 | [arXiv](https://arxiv.org/abs/2610.25736) |

## 🔗 相关

- 奖励与价值模型见 [`08`](./08-reward-failure-recovery.md)

> 📅 **2026 年本方向全部 559 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#07)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
