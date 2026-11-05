# 07 · 世界模型与视频生成

> 世界模型：学习“如果我这样做，世界会怎样变化”。在机器人领域有三种用法：① **在想象中训练策略**（Dreamer 系列）；② **作为交互式模拟器 / 策略评估器**（UniSim、Cosmos、DreamDojo）；③ **视频预测直接驱动动作**（UniPi、GR-1、World-Action Model）。
> 主线：**World Models / Dreamer（潜空间想象）→ UniSim / Genie（视频生成即模拟器）→ GR-1/GR-2（视频预训练操作）→ Cosmos / V-JEPA 2（世界基础模型）→ 2026：World-Action Model（WAM）成为 VLA 之后的新热点**

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
| **UniPi** · Learning Universal Policies via Text-Guided Video Generation | 2023 · NeurIPS'23 | 文本生成未来视频 + 逆动力学恢复动作，把决策问题转化为视频生成 | [arXiv](https://arxiv.org/abs/2302.00111) |
| ⭐ **UniSim** · Learning Interactive Real-World Simulators | 2023 · ICLR'24 | 用海量多源数据训练动作条件视频模型，作为可交互的“真实世界模拟器”训练策略 | [arXiv](https://arxiv.org/abs/2310.06114) |
| **TD-MPC2** · Scalable, Robust World Models for Continuous Control | 2023 · ICLR'24 | 隐式（无解码器）世界模型 + MPC，单模型 317M 参数覆盖 80+ 连续控制任务 | [arXiv](https://arxiv.org/abs/2310.16828) · [代码](https://github.com/nicklashansen/tdmpc2) |
| **GR-1** · Unleashing Large-Scale Video Generative Pre-training for Visual Robot Manipulation | 2023 · ICLR'24 | 在大规模视频上做“预测未来帧”的 GPT 式预训练，再微调为操作策略 | [arXiv](https://arxiv.org/abs/2312.13139) |
| **Genie** · Generative Interactive Environments | 2024 · ICML'24 | 从无标签网络视频中无监督学到潜在动作，生成可交互的虚拟环境 | [arXiv](https://arxiv.org/abs/2402.15391) |
| **GR-2** · A Generative Video-Language-Action Model with Web-Scale Knowledge | 2024 · arXiv | 3800 万视频片段预训练 + 机器人轨迹微调，视频生成与动作预测联合建模 | [arXiv](https://arxiv.org/abs/2410.06158) |
| **DINO-WM** · World Models on Pre-trained Visual Features enable Zero-shot Planning | 2024 · ICML'25 | 在 DINOv2 特征空间学世界模型，测试时零样本规划，无需重建像素 | [arXiv](https://arxiv.org/abs/2411.04983) |
| **VPP** · Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations | 2024 · ICML'25 | 用视频扩散模型的预测性表征作为策略输入，提升泛化 | [arXiv](https://arxiv.org/abs/2412.14803) |
| ⭐ **Cosmos** · World Foundation Model Platform for Physical AI | 2025 · arXiv | NVIDIA 开源世界基础模型平台：视频 tokenizer、扩散/自回归世界模型、后训练配方 | [arXiv](https://arxiv.org/abs/2501.03575) · [代码](https://github.com/nvidia-cosmos) |
| **DreamGen** · Unlocking Generalization in Robot Learning through Video World Models | 2025 · CoRL'25 | 微调视频世界模型生成“神经轨迹”，再用逆动力学/潜在动作标注，用合成数据教会机器人新行为 | [arXiv](https://arxiv.org/abs/2505.12705) · [代码](https://github.com/NVIDIA/GR00T-Dreams) |
| ⭐ **V-JEPA 2** · Self-Supervised Video Models Enable Understanding, Prediction and Planning | 2025 · arXiv | 百万小时视频自监督预训练 + 少量机器人数据训练动作条件模型，零样本规划抓放 | [arXiv](https://arxiv.org/abs/2506.09985) |
| **PointWorld** · Scaling 3D World Models for In-The-Wild Robotic Manipulation | 2026 · arXiv | 以 3D 点流统一状态与动作的大规模 3D 世界模型（约 200 万条轨迹训练），单个检查点无需示教即可完成推、可变形物体、铰接物体与工具操作 | [arXiv](https://arxiv.org/abs/2601.03782) |
| **Cosmos Policy** · Fine-Tuning Video Models for Visuomotor Control and Planning | 2026 · arXiv | 不改结构、单阶段后训练，把预训练视频模型 Cosmos-Predict2 直接变成机器人策略与规划器，LIBERO 等基准 SOTA | [arXiv](https://arxiv.org/abs/2601.16163) |
| ⭐ **LingBot-VA** · Causal World Modeling for Robot Control | 2026 · arXiv | Causal World Modeling：自回归扩散框架同时学习帧预测与策略执行，共享视觉-动作潜空间 + 闭环 rollout，长程任务与后训练数据效率突出 | [arXiv](https://arxiv.org/abs/2601.21998) |
| **DreamDojo** · A Generalist Robot World Model from Large-Scale Human Videos | 2026 · ICML'26 | 4.4 万小时第一视角人类视频预训练，用连续潜在动作统一无标签视频，可实时用于遥操作、策略评估与规划 | [arXiv](https://arxiv.org/abs/2602.06949) |
| **VLA-JEPA** · Enhancing Vision-Language-Action Model with Latent World Model | 2026 · arXiv | JEPA 式潜空间世界模型预训练 VLA，对相机运动与背景变化更鲁棒，LIBERO / SimplerEnv / 真机均有提升 | [arXiv](https://arxiv.org/abs/2602.10098) |
| ⭐ **DreamZero** · World Action Models are Zero-shot Policies | 2026 · arXiv | 基于视频扩散骨干同时预测视频与动作的 WAM，新任务/新环境泛化较 SOTA VLA 提升 2 倍以上 | [arXiv](https://arxiv.org/abs/2602.15922) |
| **DiT4DiT** · Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control | 2026 · arXiv | 视频 DiT 与动作 DiT 级联的端到端视频-动作模型，双 flow matching 目标联合训练，证明视频生成可作为策略的扩展代理 | [arXiv](https://arxiv.org/abs/2603.10448) |
| ⭐ **Fast-WAM** · Do World Action Models Need Test-time Future Imagination? | 2026 · arXiv | 发现 WAM 的收益主要来自训练时的视频协同训练而非测试时“想象未来”：训练保留视频预测、推理跳过，速度大幅提升 | [arXiv](https://arxiv.org/abs/2603.16666) |
| **GigaWorld-Policy** · An Efficient Action-Centered World--Action Model | 2026 · arXiv | 以动作为中心的 WAM，学习 2D 像素-动作动力学、可选生成视频，比 Motus 快 9 倍且成功率更高 | [arXiv](https://arxiv.org/abs/2603.17240) |
| **X-WAM** · Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising | 2026 · arXiv | 统一 4D 世界动作模型：同时做实时动作执行与视频 + 3D 重建的 4D 世界合成，异步噪声采样兼顾质量与速度 | [arXiv](https://arxiv.org/abs/2604.26694) |
| **Being-H0.7** · A Latent World-Action Model from Egocentric Videos | 2026 · arXiv | 从第一视角视频学习的潜在世界动作模型，不生成未来帧也能让 VLA 式策略具备前瞻推理 | [arXiv](https://arxiv.org/abs/2605.00078) |
| ⭐ **Cosmos 3** · Omnimodal World Models for Physical AI | 2026 · arXiv | NVIDIA 全模态世界模型：在统一 MoT 架构中联合理解与生成语言、图像、视频、音频和动作，作为具身智能体通用骨干 | [arXiv](https://arxiv.org/abs/2606.02800) |
| **MotionWAM** · Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation | 2026 · arXiv | 把世界动作模型用于人形实时移动操作 | [arXiv](https://arxiv.org/abs/2606.09215) |
| **LingBot-Video** · Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence | 2026 · arXiv | 面向具身智能的 MoE 视频预训练：在互联网视频中加入大量机器人相关片段，开源首个大规模 MoE 视频基础模型 | [arXiv](https://arxiv.org/abs/2607.07675) |
| **OpenWAM** · An Open, Modular Exploration Towards Systematic World-Action Model Pretraining | 2026 · arXiv | 开放的世界动作模型预训练研究栈，通过对照实验总结“继承什么、世界与动作如何协同、如何扩展”三条原则，并开源全部模型与数据配方 | [arXiv](https://arxiv.org/abs/2609.07398) |
| **Simple-WAM** · What Makes World Action Models Generalize? An Empirical Study of Test-Time Future Modeling | 2026 · arXiv | 实证发现潜在 WAM 在分布内与显式 WAM 持平但丢失泛化优势，提出单步全噪声视频预测的 Simple-WAM，兼顾泛化与效率 | [arXiv](https://arxiv.org/abs/2609.34981) |
| **ProWAM** · World Action Modeling with Progressive Visual Planning | 2026 · arXiv | 联合预测动作与有序的稀疏视觉子目标，用渐进式视觉规划锚定动作生成，LIBERO-Plus 85.8% | [arXiv](https://arxiv.org/abs/2610.02508) |
| **Long-WAM** · Scaling the Context of World-Action Models | 2026 · arXiv | 在实时控制约束下扩展 WAM 的历史上下文，发现自回归预训练的视频底座才能真正利用长历史 | [arXiv](https://arxiv.org/abs/2610.10528) |
| **GreenWAM** · A World Foundation Model for Robotics | 2026 · arXiv | 跨 20 类机器人共享解剖学动作空间的机器人世界基础模型，同时充当世界预测器与策略 | [arXiv](https://arxiv.org/abs/2610.18774) |

> 综述与教程（World-Action Model Survey、WAM Tutorial 等）见 [`12-surveys.md`](./12-surveys.md)。

> 📅 **2026 年本方向全部 843 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#07)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
