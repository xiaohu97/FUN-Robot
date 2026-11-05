# 09 · 具身导航与移动操作

> 让机器人“找得到、走得到”：视觉语言导航（VLN）、目标导航（ObjectNav）、通用导航基础模型，以及导航 + 操作结合的移动操作。
> 主线：**R2R（VLN 任务定义）→ DD-PPO / SemExp（仿真大规模训练、语义地图）→ CLIP/LLM 零样本导航 → GNM / ViNT / NoMaD（导航基础模型）→ NaVid / NaVILA（视频 VLM 导航）→ 2026：统一导航 VLA 与世界动作模型**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **R2R** · Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments | 2017 · CVPR'18 | 提出 VLN 任务与 Room-to-Room 数据集，奠定语言导航研究 | [arXiv](https://arxiv.org/abs/1711.07280) |
| **DD-PPO** · Learning Near-Perfect PointGoal Navigators from 2.5 Billion Frames | 2019 · ICLR'20 | 去中心化分布式 PPO，25 亿帧训练出近乎完美的点目标导航 | [arXiv](https://arxiv.org/abs/1911.00357) |
| **SemExp** · Object Goal Navigation using Goal-Oriented Semantic Exploration | 2020 · NeurIPS'20 | 构建语义地图 + 目标导向探索策略，ObjectNav 经典方法（CVPR'20 Habitat 挑战冠军） | [arXiv](https://arxiv.org/abs/2007.00643) |
| **CoW** · CoWs on Pasture: Baselines and Benchmarks for Language-Driven Zero-Shot Object Navigation | 2022 · CVPR'23 | 用 CLIP 做开放词汇目标定位 + 经典探索，实现零样本目标导航 | [arXiv](https://arxiv.org/abs/2203.10421) |
| **LM-Nav** · Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action | 2022 · CoRL'22 | 组合 GPT-3、CLIP 与视觉导航模型，无需标注即可执行语言导航指令 | [arXiv](https://arxiv.org/abs/2207.04429) |
| **GNM** · A General Navigation Model to Drive Any Robot | 2022 · ICRA'23 | 多种机器人混合数据训练的通用视觉导航策略，可跨本体部署 | [arXiv](https://arxiv.org/abs/2210.03370) |
| **VLMaps** · Visual Language Maps for Robot Navigation | 2022 · ICRA'23 | 把视觉语言特征融合进 3D 重建地图，支持“去沙发和电视之间”等空间语言导航 | [arXiv](https://arxiv.org/abs/2210.05714) |

## 🚀 最新进展（2023 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **ViNT** · A Foundation Model for Visual Navigation | 2023 · CoRL'23 | Transformer 导航基础模型，可通过 prompt-tuning 适配新任务与新机器人 | [arXiv](https://arxiv.org/abs/2306.14846) · [代码](https://github.com/robodhruv/visualnav-transformer) |
| **NoMaD** · Goal Masked Diffusion Policies for Navigation and Exploration | 2023 · ICRA'24 | 目标掩码 + 扩散策略，一个模型同时完成目标导航与无目标探索 | [arXiv](https://arxiv.org/abs/2310.07896) · [代码](https://github.com/robodhruv/visualnav-transformer) |
| ⭐ **OK-Robot** · What Really Matters in Integrating Open-Knowledge Models for Robotics | 2024 · CoRL'24 | 组合开放词汇检测、语义记忆与抓取模型的家庭移动拾放系统，并分析失败原因 | [arXiv](https://arxiv.org/abs/2401.12202) |
| **NaVid** · Video-based VLM Plans the Next Step for Vision-and-Language Navigation | 2024 · RSS'24 | 仅用单目 RGB 视频流的视频 VLM 导航，无需地图、深度和里程计 | [arXiv](https://arxiv.org/abs/2402.15852) |
| **Mobility VLA** · Multimodal Instruction Navigation with Long-Context VLMs and Topological Graphs | 2024 · CoRL'24 | 长上下文 VLM 理解演示视频 + 拓扑图低层导航，执行多模态指令 | [arXiv](https://arxiv.org/abs/2407.07775) |
| **NaVILA** · Legged Robot Vision-Language-Action Model for Navigation | 2024 · RSS'25 | VLA 输出语言化的中层动作，再由 RL 运动策略执行，四足/人形完成语言导航 | [arXiv](https://arxiv.org/abs/2412.04453) |
| **Uni-NaVid** · A Video-based VLA Model for Unifying Embodied Navigation Tasks | 2024 · RSS'25 | 一个视频 VLA 统一 VLN、目标导航、跟随、问答等多种导航任务 | [arXiv](https://arxiv.org/abs/2412.06224) |
| **NavFoM** · Embodied Navigation Foundation Model | 2025 · arXiv | 跨本体（四足、无人机、轮式、汽车）、跨任务的导航基础模型 | [arXiv](https://arxiv.org/abs/2509.12129) |
| **Ground Slow, Move Fast** · A Dual-System Foundation Model for Generalizable VLN | 2025 · arXiv | 慢系统做语义定位、快系统做运动控制的双系统 VLN 基础模型 | [arXiv](https://arxiv.org/abs/2512.08186) |
| **SparseVideoNav** · Sparse Video Generation Propels Real-World Beyond-the-View Vision-Language Navigation | 2026 · arXiv | 首次把视频生成模型用于“视野外”语言导航：生成 20 秒稀疏未来画面指导轨迹，亚秒级推理，真机零样本 | [arXiv](https://arxiv.org/abs/2602.05827) |
| **ABot-N0** · Technical Report on the VLA Foundation Model for Versatile Embodied Navigation | 2026 · arXiv | 统一五类导航任务的导航 VLA，flow matching 动作专家生成轨迹 | [arXiv](https://arxiv.org/abs/2602.11598) |
| **HoMMI** · Learning Whole-Body Mobile Manipulation from Human Demonstrations | 2026 · arXiv | 在 UMI 基础上加入第一视角感知，用无机器人的人类示教学习全身移动操作，跨本体手眼策略设计 | [arXiv](https://arxiv.org/abs/2603.03243) |
| **Qwen-RobotNav Technical Report** · A Scalable Navigation Model Designed for an Agentic Navigation System | 2026 · arXiv | 面向智能体式导航系统的可扩展导航模型：多任务模式 + 可控观测参数接口，1560 万样本训练 | [arXiv](https://arxiv.org/abs/2606.18112) |
| **FutureNav** · Unified World-Action Modeling for Vision-and-Language Navigation | 2026 · arXiv | 把世界动作模型引入连续环境 VLN，4B 规模骨干超过更大的导航基础模型 | [arXiv](https://arxiv.org/abs/2606.30367) |
| **ABot-N1** · Toward a General Visual Language Navigation Foundation Model | 2026 · arXiv | “慢思考认知 + 快速控制”解耦的通用视觉语言导航基础模型，城市级导航 POI 到达率提升 35 个点 | [arXiv](https://arxiv.org/abs/2607.10383) |
| **HarnessVLN** · Unifying Training-Free Embodied Navigation through an Agent Harness | 2026 · arXiv | 免训练的智能体框架统一指令导航与目标导航，在 R2R、RxR、HM3D 上验证并可真机部署 | [arXiv](https://arxiv.org/abs/2609.15195) |
| **SuperNav** · An Agentic Navigation System for Any Task in Any Scene | 2026 · arXiv | 给预训练多模态大模型配上导航技能、工具与进度管理的智能体框架，无需导航微调即可处理任意场景任意任务 | [arXiv](https://arxiv.org/abs/2610.12126) |
| **ScaleNav** · Scalable Internet Video Pretraining for Language-Conditioned Local Navigation | 2026 · arXiv | 从互联网第一视角视频中学习目标导向的视觉动力学，三阶段世界-动作框架做语言条件局部导航 | [arXiv](https://arxiv.org/abs/2610.25690) |

> 📅 **2026 年本方向全部 1065 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#09)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
