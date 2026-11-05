# 03 · 世界模型与视频生成

> 世界模型：学习“如果我这样做，世界会怎样变化”。机器人中的用法包括：① **在想象中训练策略**（Dreamer 系列）；② **作为交互式模拟器 / 策略评估器**（UniSim、Cosmos、DreamDojo）；③ **合成训练数据**（DreamGen）；④ **作为表征**（V-JEPA）。
> 主线：**World Models / Dreamer（潜空间想象）→ UniSim / Genie（视频生成即模拟器）→ Cosmos / V-JEPA 2（世界基础模型）→ 2026：Cosmos 3 全模态世界模型、DreamDojo 人类视频世界模型**

> 直接输出动作的视频-动作联合模型已拆分到 [`02 世界动作模型`](./02-world-action-models.md)。

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **World Models** | 2018 · NeurIPS'18 | VAE + MDN-RNN 学习环境的压缩时空模型，智能体可以“在梦里”训练 | [arXiv](https://arxiv.org/abs/1803.10122) |
| **PlaNet** · Learning Latent Dynamics for Planning from Pixels | 2018 · ICML'19 | 循环状态空间模型（RSSM）+ 潜空间规划，从像素学控制 | [arXiv](https://arxiv.org/abs/1811.04551) |
| ⭐ **Dreamer** · Dream to Control: Learning Behaviors by Latent Imagination | 2019 · ICLR'20 | 在学到的潜空间中“想象”轨迹并反传价值梯度，样本效率大幅提升 | [arXiv](https://arxiv.org/abs/1912.01603) |
| **DreamerV2** · Mastering Atari with Discrete World Models | 2020 · ICLR'21 | 离散潜变量世界模型，首次在 Atari 上达到人类水平 | [arXiv](https://arxiv.org/abs/2010.02193) |
| **DayDreamer** · World Models for Physical Robot Learning | 2022 · CoRL'22 | 不用仿真器，直接在真机上用 Dreamer 学习：四足 1 小时学会走路 | [arXiv](https://arxiv.org/abs/2206.14176) |
| ⭐ **DreamerV3** · Mastering Diverse Domains through World Models | 2023 · Nature'25 | 一套超参数通吃 150+ 任务，首次从零在 Minecraft 中挖到钻石 | [arXiv](https://arxiv.org/abs/2301.04104) · [代码](https://github.com/danijar/dreamerv3) |

## 🚀 最新进展（2023 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **UniSim** · Learning Interactive Real-World Simulators | 2023 · ICLR'24 | 用海量多源数据训练动作条件视频模型，作为可交互的“真实世界模拟器”训练策略 | [arXiv](https://arxiv.org/abs/2310.06114) |
| **TD-MPC2** · Scalable, Robust World Models for Continuous Control | 2023 · ICLR'24 | 隐式（无解码器）世界模型 + MPC，单模型 317M 参数覆盖 80+ 连续控制任务 | [arXiv](https://arxiv.org/abs/2310.16828) · [代码](https://github.com/nicklashansen/tdmpc2) |
| **Genie** · Generative Interactive Environments | 2024 · ICML'24 | 从无标签网络视频中无监督学到潜在动作，生成可交互的虚拟环境 | [arXiv](https://arxiv.org/abs/2402.15391) |
| **DINO-WM** · World Models on Pre-trained Visual Features enable Zero-shot Planning | 2024 · ICML'25 | 在 DINOv2 特征空间学世界模型，测试时零样本规划，无需重建像素 | [arXiv](https://arxiv.org/abs/2411.04983) |
| ⭐ **Cosmos** · World Foundation Model Platform for Physical AI | 2025 · arXiv | NVIDIA 开源世界基础模型平台：视频 tokenizer、扩散/自回归世界模型、后训练配方 | [arXiv](https://arxiv.org/abs/2501.03575) · [代码](https://github.com/nvidia-cosmos) |
| **DreamGen** · Unlocking Generalization in Robot Learning through Video World Models | 2025 · CoRL'25 | 微调视频世界模型生成“神经轨迹”，再用逆动力学/潜在动作标注，用合成数据教会机器人新行为 | [arXiv](https://arxiv.org/abs/2505.12705) · [代码](https://github.com/NVIDIA/GR00T-Dreams) |
| ⭐ **V-JEPA 2** · Self-Supervised Video Models Enable Understanding, Prediction and Planning | 2025 · arXiv | 百万小时视频自监督预训练 + 少量机器人数据训练动作条件模型，零样本规划抓放 | [arXiv](https://arxiv.org/abs/2506.09985) |
| **PointWorld** · Scaling 3D World Models for In-The-Wild Robotic Manipulation | 2026 · arXiv | 以 3D 点流统一状态与动作的大规模 3D 世界模型（约 200 万条轨迹训练），单个检查点无需示教即可完成推、可变形物体、铰接物体与工具操作 | [arXiv](https://arxiv.org/abs/2601.03782) |
| **DreamDojo** · A Generalist Robot World Model from Large-Scale Human Videos | 2026 · ICML'26 | 4.4 万小时第一视角人类视频预训练，用连续潜在动作统一无标签视频，可实时用于遥操作、策略评估与规划 | [arXiv](https://arxiv.org/abs/2602.06949) |
| ⭐ **Cosmos 3** · Omnimodal World Models for Physical AI | 2026 · arXiv | NVIDIA 全模态世界模型：在统一 MoT 架构中联合理解与生成语言、图像、视频、音频和动作，作为具身智能体通用骨干 | [arXiv](https://arxiv.org/abs/2606.02800) |
| **LingBot-Video** · Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence | 2026 · arXiv | 面向具身智能的 MoE 视频预训练：在互联网视频中加入大量机器人相关片段，开源首个大规模 MoE 视频基础模型 | [arXiv](https://arxiv.org/abs/2607.07675) |

## 🔗 相关

- 世界模型评测：WorldArena 见 [`17`](./17-simulation-benchmarks.md)；综述见 [`18`](./18-surveys.md)

> 📅 **2026 年本方向全部 505 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#03)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
