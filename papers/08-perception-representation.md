# 08 · 视觉表征与 3D 场景理解

> 机器人“看什么、怎么表示”：通用视觉预训练表征（R3M、VC-1）、语义 3D 场景表示（特征场、场景图）、物体位姿估计。

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **NDF** · Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation | 2021 · ICRA'22 | SE(3) 等变的隐式物体描述子，几条示教即可泛化到新物体、新位姿 | [arXiv](https://arxiv.org/abs/2112.05124) |
| **MVP** · Masked Visual Pre-training for Motor Control | 2022 · arXiv | 用 MAE 在真实图像上自监督预训练视觉编码器，冻结后用于控制 | [arXiv](https://arxiv.org/abs/2203.06173) |
| ⭐ **R3M** · A Universal Visual Representation for Robot Manipulation | 2022 · CoRL'22 | 在 Ego4D 人类视频上用时间对比 + 语言对齐预训练，成为通用机器人视觉表征 | [arXiv](https://arxiv.org/abs/2203.12601) |
| **CLIP-Fields** · Weakly Supervised Semantic Fields for Robotic Memory | 2022 · arXiv | 把 CLIP/检测特征蒸馏到 3D 隐式场，支持开放词汇的空间查询 | [arXiv](https://arxiv.org/abs/2210.05663) |

## 🚀 最新进展（2023 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **VC-1** · Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence? | 2023 · NeurIPS'23 | 系统评测预训练视觉表征，发现没有“万能”表征，并发布 CortexBench | [arXiv](https://arxiv.org/abs/2303.18240) |
| **F3RM** · Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation | 2023 · CoRL'23 | 把 CLIP 特征蒸馏进 NeRF 特征场，语言指定物体后少样本完成 6-DoF 抓取 | [arXiv](https://arxiv.org/abs/2308.07931) |
| **ConceptGraphs** · Open-Vocabulary 3D Scene Graphs for Perception and Planning | 2023 · ICRA'24 | 开放词汇 3D 场景图，物体级语义 + 关系，可直接交给 LLM 规划 | [arXiv](https://arxiv.org/abs/2309.16650) |
| ⭐ **FoundationPose** · Unified 6D Pose Estimation and Tracking of Novel Objects | 2023 · CVPR'24 | 新物体 6D 位姿估计与跟踪的基础模型，支持有模型/无模型两种设定 | [arXiv](https://arxiv.org/abs/2312.08344) · [代码](https://github.com/NVlabs/FoundationPose) |
| **EmbodMocap** · In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents | 2026 · arXiv | 低成本采集真实场景中的 4D 人-场景交互数据，为具身智能体提供训练数据 | [arXiv](https://arxiv.org/abs/2602.23205) |
