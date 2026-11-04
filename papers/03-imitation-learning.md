# 03 · 模仿学习与策略学习

> 从示教数据中学策略（Behavior Cloning 及其变体），是当前操作任务最主流的路线。
> 主线：**DAgger（分布偏移）→ BC-Z / robomimic（规模与经验）→ 隐式/多模态策略（IBC、BeT）→ Diffusion Policy / ACT（生成式动作 + 动作分块）→ 3D 表征、加速推理、数据规律、RL 微调**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **DAgger** · A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | 2010 · AISTATS'11 | 迭代聚合专家纠正数据，从理论上解决行为克隆的复合误差/分布偏移 | [arXiv](https://arxiv.org/abs/1011.0686) |
| ⭐ **End-to-End Visuomotor Policies** · End-to-End Training of Deep Visuomotor Policies | 2015 · JMLR'16 | 首次端到端从图像像素直接学到电机力矩的深度策略，开启深度机器人学习 | [arXiv](https://arxiv.org/abs/1504.00702) |
| **One-Shot Imitation Learning** | 2017 · NeurIPS'17 | 给一条示教即可执行新任务的元模仿学习框架 | [arXiv](https://arxiv.org/abs/1703.07326) |
| **robomimic** · What Matters in Learning from Offline Human Demonstrations for Robot Manipulation | 2021 · CoRL'21 | 系统评估离线示教学习的关键因素（数据质量、网络结构、历史观测）并开源框架 | [arXiv](https://arxiv.org/abs/2108.03298) · [代码](https://github.com/ARISE-Initiative/robomimic) |
| **Implicit BC** · Implicit Behavioral Cloning | 2021 · CoRL'21 | 用能量模型隐式表示策略，更好拟合多模态与不连续的动作分布 | [arXiv](https://arxiv.org/abs/2109.00137) |
| **BC-Z** · Zero-Shot Task Generalization with Robotic Imitation Learning | 2022 · CoRL'21 | 大规模遥操作 + 语言/视频任务条件，实现对未见任务的零样本泛化 | [arXiv](https://arxiv.org/abs/2202.02005) |
| **Diffuser** · Planning with Diffusion for Flexible Behavior Synthesis | 2022 · ICML'22 | 用扩散模型直接生成整条轨迹做规划，奠定“扩散 + 决策”的思路 | [arXiv](https://arxiv.org/abs/2205.09991) |
| **BeT** · Behavior Transformers: Cloning k Modes with One Stone | 2022 · NeurIPS'22 | 动作 k-means 离散 + 残差偏移的 Transformer，有效拟合多模态示教 | [arXiv](https://arxiv.org/abs/2206.11251) |
| ⭐ **Diffusion Policy** · Visuomotor Policy Learning via Action Diffusion | 2023 · RSS'23 | 把动作生成建模为条件去噪扩散，天然支持多模态与高维动作序列，大幅超越前作 | [arXiv](https://arxiv.org/abs/2303.04137) · [代码](https://github.com/real-stanford/diffusion_policy) · [笔记](./notes/2303.04137-diffusion-policy.md) |
| ⭐ **ACT / ALOHA** · Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware | 2023 · RSS'23 | 低成本双臂遥操作平台 + 动作分块 Transformer（CVAE），50 条示教完成精细双臂任务 | [arXiv](https://arxiv.org/abs/2304.13705) · [代码](https://github.com/tonyzhaozh/act) |

## 🚀 最新进展（2024 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **VQ-BeT** · Behavior Generation with Latent Actions | 2024 · ICML'24 | 用残差 VQ 离散化动作，比扩散策略推理更快且同样能处理多模态 | [arXiv](https://arxiv.org/abs/2403.03181) |
| ⭐ **DP3** · 3D Diffusion Policy | 2024 · RSS'24 | 以稀疏点云为输入的扩散策略，10 条左右示教即可泛化到新视角/新物体 | [arXiv](https://arxiv.org/abs/2403.03954) · [代码](https://github.com/YanjieZe/3D-Diffusion-Policy) |
| **Consistency Policy** · Accelerated Visuomotor Policies via Consistency Distillation | 2024 · RSS'24 | 一致性蒸馏把扩散策略推理加速一个数量级，适合算力受限的实时控制 | [arXiv](https://arxiv.org/abs/2405.07503) |
| **DPPO** · Diffusion Policy Policy Optimization | 2024 · ICLR'25 | 用策略梯度直接微调预训练扩散策略，打通“模仿预训练 → RL 精调” | [arXiv](https://arxiv.org/abs/2409.00588) |
| ⭐ **Data Scaling Laws in Imitation Learning for Robotic Manipulation** | 2024 · ICLR'25 | 发现环境与物体多样性远比单一环境示教数量重要，给出高效数据采集策略 | [arXiv](https://arxiv.org/abs/2410.18647) |

> 模仿学习的数据采集（遥操作、UMI、数据增广）见 [`10-data-teleoperation.md`](./10-data-teleoperation.md)；大规模预训练版本见 [`01-vla-foundation-models.md`](./01-vla-foundation-models.md)。
