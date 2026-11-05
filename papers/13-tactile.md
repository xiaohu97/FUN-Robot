# 13 · 触觉与接触感知 🆕

> 🆕 **新增方向**（由“操作与灵巧手”拆分）。视觉看不到接触状态，接触丰富的任务（装配、插拔、易碎物体、手内操作）需要触觉 / 力觉。2026 年触觉从“附加传感器”变成 VLA 和世界动作模型的一等输入：VTLA、触觉世界模型、跨传感器的触觉基础策略。
> 主线：**GelSight / DIGIT（视觉式触觉传感器）→ TACTO（触觉仿真）→ UniTouch / Sparsh / AnyTouch（触觉表征）→ 3D-ViTac（视触觉策略）→ 2026：TacVLA / N0-VTLA（触觉 VLA）、视触觉世界模型、FTP-1（跨传感器触觉基础策略）**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典与奠基工作

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **The Feeling of Success** · Does Touch Sensing Help Predict Grasp Outcomes? | 2017 · CoRL'17 | 用 GelSight 触觉 + 视觉预测抓取成败，证明触觉显著提升抓取结果预测 | [arXiv](https://arxiv.org/abs/1710.05512) |
| **More Than a Feeling** · Learning to Grasp and Regrasp using Vision and Touch | 2018 · RA-L'18 | 端到端视触觉动作条件模型，学会根据触觉反馈重新抓取 | [arXiv](https://arxiv.org/abs/1805.11085) |
| ⭐ **DIGIT** · A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation | 2020 · RA-L'20 | 低成本、紧凑、高分辨率的视觉式触觉传感器，后续大量触觉研究的标准硬件 | [arXiv](https://arxiv.org/abs/2005.14679) |
| **TACTO** · A Fast, Flexible, and Open-source Simulator for High-Resolution Vision-based Tactile Sensors | 2020 · RA-L'22 | 开源视觉式触觉传感器仿真器，支持在仿真中学习触觉策略 | [arXiv](https://arxiv.org/abs/2012.08456) · [代码](https://github.com/facebookresearch/tacto) |
| **UniTouch** · Binding Touch to Everything: Learning Unified Multimodal Tactile Representations | 2024 · CVPR'24 | 把触觉对齐到视觉、语言、声音的统一表征空间，跨多种触觉传感器零样本迁移 | [arXiv](https://arxiv.org/abs/2401.18084) |
| **Sparsh** · Self-supervised touch representations for vision-based tactile sensing | 2024 · CoRL'24 | 在 46 万张触觉图像上自监督预训练的通用触觉表征，并发布触觉基准 TacBench | [arXiv](https://arxiv.org/abs/2410.24090) |
| ⭐ **3D-ViTac** · Learning Fine-Grained Manipulation with Visuo-Tactile Sensing | 2024 · CoRL'24 | 低成本柔性触觉阵列 + 视触觉 3D 点云融合策略，完成易碎物体等精细双臂操作 | [arXiv](https://arxiv.org/abs/2410.24091) |

## 🚀 最新进展（2025 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **TouchGuide** · Inference-Time Steering of Visuomotor Policies via Touch Guidance | 2026 · arXiv | 推理时用触觉可行性评分引导视觉运动策略的采样，配套 TacUMI 采集系统，系鞋带等接触任务大幅领先 | [arXiv](https://arxiv.org/abs/2601.20239) |
| **TaF-VLA** · Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation | 2026 · arXiv | 从“触觉-视觉对齐”转向“触觉-力对齐”：把高维触觉观测显式落到物理交互力上，实现力感知操作 | [arXiv](https://arxiv.org/abs/2601.20321) |
| **Visuo-Tactile World Models** | 2026 · arXiv | 多任务视触觉世界模型，用触觉推理刻画接触物理，想象轨迹更符合物理，真机零样本成功率最高提升 35% | [arXiv](https://arxiv.org/abs/2602.06001) |
| **AnyTouch 2** · General Optical Tactile Representation Learning For Dynamic Tactile Perception | 2026 · ICLR'26 | 面向动态触觉感知的通用光学触觉表征学习，配套分层大规模触觉数据集 ToucHD | [arXiv](https://arxiv.org/abs/2602.09617) |
| **UniVTAC** · A Unified Simulation Platform for Visuo-Tactile Manipulation Data Generation, Learning, and Benchmarking | 2026 · arXiv | 支持三种视触觉传感器的仿真数据合成平台，配套视触觉编码器与基准 | [arXiv](https://arxiv.org/abs/2602.10093) |
| **Grasp, Slide, Roll** · Comparative Analysis of Contact Modes for Tactile-Based Shape Reconstruction | 2026 · arXiv | 比较抓放、指尖滑动、掌心滚动三种触觉接触模式，滑动/滚动少用约 34% 接触完成纯触觉形状重建 | [arXiv](https://arxiv.org/abs/2602.23206) |
| **TacVLA** · Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation | 2026 · arXiv | 接触门控的触觉融合：只在检测到接触时激活触觉 token，提升 VLA 的精细接触操作 | [arXiv](https://arxiv.org/abs/2603.12665) |
| **HapticVLA** · Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing | 2026 · arXiv | 离线学习触觉感知能力，部署时无需触觉传感器也能完成接触丰富操作 | [arXiv](https://arxiv.org/abs/2603.15257) |
| **OmniVTA** · Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation | 2026 · arXiv | 2.1 万条视觉-触觉-动作轨迹数据集 + 视触觉世界模型，用预测式接触建模和高频触觉闭环完成接触丰富操作 | [arXiv](https://arxiv.org/abs/2603.19201) |
| **VTAM** · Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs | 2026 · arXiv | 视频-触觉-动作模型，补足 VLA 在视觉不可观测接触状态下的短板 | [arXiv](https://arxiv.org/abs/2603.23481) |
| **Dream-Tac** · A Unified Tactile World Action Model for Contact-Rich Robot Manipulation | 2026 · arXiv | 联合建模动作、未来视觉与触觉动态的触觉世界动作模型，接触门控融合 + 推理加速 | [arXiv](https://arxiv.org/abs/2606.08737) |
| **TacForeSight** · Force-Guided Tactile World Model for Contact-Rich Manipulation | 2026 · arXiv | 力条件化的轻量触觉预见模型，区分全局力与局部触觉的时空作用 | [arXiv](https://arxiv.org/abs/2606.11184) |
| **FTP-1** · A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation | 2026 · arXiv | 首个跨触觉传感器与本体的通用触觉基础策略，在 26 个来源约 3000 小时触觉操作数据上预训练 | [arXiv](https://arxiv.org/abs/2606.13102) |
| **T-Rex** · Tactile-Reactive Dexterous Manipulation | 2026 · arXiv | 100 小时富触觉数据集 + 利用高频触觉的反应式灵巧操作策略 | [arXiv](https://arxiv.org/abs/2606.17055) |
| **VT-WAM** · Visual-Tactile World Action Model for Contact-Rich Manipulation | 2026 · arXiv | 统一 flow matching 框架联合预测未来视觉、触觉形变与动作，6 个真机接触任务平均 71.67% | [arXiv](https://arxiv.org/abs/2607.02503) |
| **N0-VTLA** · Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens | 2026 · arXiv | 视觉-触觉-语言-动作基础模型：潜在触觉 token、分阶段触觉通路接入，以及基于部署数据的优势条件离线改进 | [arXiv](https://arxiv.org/abs/2607.23782) |
| **N0-TWAM** · Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation | 2026 · arXiv | 首个大规模训练的“触觉原生”世界动作模型，同时预测未来视觉与未来接触 | [arXiv](https://arxiv.org/abs/2607.23783) |
| **Tactile-JEPA** · Topology-Aware Self-Supervised Representation Learning for Distributed Tactile Sensors | 2026 · arXiv | 利用分布式触觉传感器空间拓扑的自监督 JEPA 式预训练 | [arXiv](https://arxiv.org/abs/2609.24385) |

> 📅 **2026 年本方向全部 458 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#13)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
