# 02 · 世界动作模型（World-Action Model, WAM）🆕

> 🆕 **2026 年新增方向**。WAM 用预训练视频生成模型作为骨干，**同时预测未来画面与动作**，把“理解世界如何变化”和“决定怎么做”合在一个模型里，被视为 VLA 之后的新范式。
> 数据：2026 年标题含 world-action / WAM 的论文从 1 月 0 篇增长到 10 月 81 篇；年度引用最高的 4 篇论文（DreamZero、Fast-WAM、Cosmos Policy、LingBot-VA）全部属于这一方向。
> 主线：**UniPi / GR-1（视频生成 → 动作）→ DreamZero（WAM 是零样本策略）→ Fast-WAM（测试时不必想象未来）→ 潜在 WAM、4D WAM、长上下文 WAM → OpenWAM（系统化预训练研究）**

> 与 [`03 世界模型`](./03-world-models.md) 的区别：03 收录用于模拟、评测、数据合成的世界模型；本方向只收录**直接输出动作的“视频 + 动作”联合模型**。

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典与奠基工作

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **UniPi** · Learning Universal Policies via Text-Guided Video Generation | 2023 · NeurIPS'23 | 文本生成未来视频 + 逆动力学恢复动作，把决策问题转化为视频生成 | [arXiv](https://arxiv.org/abs/2302.00111) |
| **GR-1** · Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation | 2023 · ICLR'24 | 在大规模视频上做“预测未来帧”的 GPT 式预训练，再微调为操作策略 | [arXiv](https://arxiv.org/abs/2312.13139) |
| **GR-2** · A Generative Video-Language-Action Model with Web-Scale Knowledge | 2024 · arXiv | 3800 万视频片段预训练 + 机器人轨迹微调，视频生成与动作预测联合建模 | [arXiv](https://arxiv.org/abs/2410.06158) |
| **VPP** · Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations | 2024 · ICML'25 | 用视频扩散模型的预测性表征作为策略输入，提升泛化 | [arXiv](https://arxiv.org/abs/2412.14803) |

## 🚀 最新进展（2025 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **Cosmos Policy** · Fine-Tuning Video Models for Visuomotor Control and Planning | 2026 · arXiv | 不改结构、单阶段后训练，把预训练视频模型 Cosmos-Predict2 直接变成机器人策略与规划器，LIBERO 等基准 SOTA | [arXiv](https://arxiv.org/abs/2601.16163) |
| ⭐ **LingBot-VA** · Causal World Modeling for Robot Control | 2026 · arXiv | Causal World Modeling：自回归扩散框架同时学习帧预测与策略执行，共享视觉-动作潜空间 + 闭环 rollout，长程任务与后训练数据效率突出 | [arXiv](https://arxiv.org/abs/2601.21998) |
| **VLA-JEPA** · Enhancing Vision-Language-Action Model with Latent World Model | 2026 · arXiv | JEPA 式潜空间世界模型预训练 VLA，对相机运动与背景变化更鲁棒，LIBERO / SimplerEnv / 真机均有提升 | [arXiv](https://arxiv.org/abs/2602.10098) |
| ⭐ **DreamZero** · World Action Models are Zero-shot Policies | 2026 · arXiv | 基于视频扩散骨干同时预测视频与动作的 WAM，新任务/新环境泛化较 SOTA VLA 提升 2 倍以上 | [arXiv](https://arxiv.org/abs/2602.15922) |
| **DiT4DiT** · Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control | 2026 · arXiv | 视频 DiT 与动作 DiT 级联的端到端视频-动作模型，双 flow matching 目标联合训练，证明视频生成可作为策略的扩展代理 | [arXiv](https://arxiv.org/abs/2603.10448) |
| ⭐ **Fast-WAM** · Do World Action Models Need Test-time Future Imagination? | 2026 · arXiv | 发现 WAM 的收益主要来自训练时的视频协同训练而非测试时“想象未来”：训练保留视频预测、推理跳过，速度大幅提升 | [arXiv](https://arxiv.org/abs/2603.16666) |
| **GigaWorld-Policy** · An Efficient Action-Centered World--Action Model | 2026 · arXiv | 以动作为中心的 WAM，学习 2D 像素-动作动力学、可选生成视频，比 Motus 快 9 倍且成功率更高 | [arXiv](https://arxiv.org/abs/2603.17240) |
| **X-WAM** · Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising | 2026 · arXiv | 统一 4D 世界动作模型：同时做实时动作执行与视频 + 3D 重建的 4D 世界合成，异步噪声采样兼顾质量与速度 | [arXiv](https://arxiv.org/abs/2604.26694) |
| **Being-H0.7** · A Latent World-Action Model from Egocentric Videos | 2026 · arXiv | 从第一视角视频学习的潜在世界动作模型，不生成未来帧也能让 VLA 式策略具备前瞻推理 | [arXiv](https://arxiv.org/abs/2605.00078) |
| **MotionWAM** · Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation | 2026 · arXiv | 把世界动作模型用于人形实时移动操作 | [arXiv](https://arxiv.org/abs/2606.09215) |
| **OpenWAM** · An Open, Modular Exploration Towards Systematic World-Action Model Pretraining | 2026 · arXiv | 开放的世界动作模型预训练研究栈，通过对照实验总结“继承什么、世界与动作如何协同、如何扩展”三条原则，并开源全部模型与数据配方 | [arXiv](https://arxiv.org/abs/2609.07398) |
| **Simple-WAM** · What Makes World Action Models Generalize? An Empirical Study of Test-Time Future Modeling | 2026 · arXiv | 实证发现潜在 WAM 在分布内与显式 WAM 持平但丢失泛化优势，提出单步全噪声视频预测的 Simple-WAM，兼顾泛化与效率 | [arXiv](https://arxiv.org/abs/2609.34981) |
| **ProWAM** · World Action Modeling with Progressive Visual Planning | 2026 · arXiv | 联合预测动作与有序的稀疏视觉子目标，用渐进式视觉规划锚定动作生成，LIBERO-Plus 85.8% | [arXiv](https://arxiv.org/abs/2610.02508) |
| **PointWAM** · 3D World Action Modeling for Dexterous Robotic Manipulation | 2026 · arXiv | 把世界分解为“场景 + 手”并联合预测 3D 点轨迹的世界动作模型，可直接用人类视频预训练，DexJoCo 提升 56.9 个点 | [arXiv](https://arxiv.org/abs/2610.02840) |
| **Long-WAM** · Scaling the Context of World-Action Models | 2026 · arXiv | 在实时控制约束下扩展 WAM 的历史上下文，发现自回归预训练的视频底座才能真正利用长历史 | [arXiv](https://arxiv.org/abs/2610.10528) |
| **GreenWAM** · A World Foundation Model for Robotics | 2026 · arXiv | 跨 20 类机器人共享解剖学动作空间的机器人世界基础模型，同时充当世界预测器与策略 | [arXiv](https://arxiv.org/abs/2610.18774) |

## 🔗 相关

- 入门：先读 [From World Models to World Action Models 教程](https://arxiv.org/abs/2607.00836)，再读 DreamZero → Fast-WAM → OpenWAM
- 综述见 [`18`](./18-surveys.md)（World Action Models: The Next Frontier / A Survey）

> 📅 **2026 年本方向全部 ? 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#02)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
