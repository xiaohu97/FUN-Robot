# 04 · 具身推理与任务规划（LLM / VLM for Robotics）

> 大模型负责“想”：理解指令、分解任务、推断空间关系；底层技能负责“做”。
> 主线：**LLM 零样本规划 → SayCan（可行性约束）→ VoxPoser / ReKep（空间约束）→ 具身推理 VLM（Cosmos-Reason、RoboBrain、MolmoAct2）**

> 让大模型**直接**控制机器人、写代码、自我进化的工作已拆分到 [`05 机器人智能体`](./05-robot-agents.md)；奖励设计与奖励模型见 [`08`](./08-reward-failure-recovery.md)。

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **LM Zero-Shot Planners** · Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents | 2022 · ICML'22 | 首次展示 LLM 无需训练即可把高层指令分解为可执行步骤 | [arXiv](https://arxiv.org/abs/2201.07207) |
| ⭐ **SayCan** · Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022 · CoRL'22 | LLM 判断“该做什么”，价值函数判断“能否做成”，两者相乘选择技能 | [arXiv](https://arxiv.org/abs/2204.01691) |
| **Inner Monologue** · Embodied Reasoning through Planning with Language Models | 2022 · CoRL'22 | 把成功检测、场景描述、人类反馈作为语言反馈闭环喂给 LLM 规划器 | [arXiv](https://arxiv.org/abs/2207.05608) |
| **ProgPrompt** · Generating Situated Robot Task Plans using Large Language Models | 2022 · ICRA'23 | 程序化提示（可用动作 + 物体 + 断言）让 LLM 生成与环境匹配的任务计划 | [arXiv](https://arxiv.org/abs/2209.11302) |
| ⭐ **VoxPoser** · Composable 3D Value Maps for Robotic Manipulation with Language Models | 2023 · CoRL'23 | LLM 写代码调用 VLM，组合出 3D 可供性/约束价值图，零样本合成轨迹 | [arXiv](https://arxiv.org/abs/2307.05973) · [代码](https://github.com/huangwl18/VoxPoser) |
| **SayPlan** · Grounding LLMs using 3D Scene Graphs for Scalable Robot Task Planning | 2023 · CoRL'23 | 在 3D 场景图上做语义搜索与迭代重规划，扩展到多楼层大场景 | [arXiv](https://arxiv.org/abs/2307.06135) |

## 🚀 最新进展（2024 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **SpatialVLM** · Endowing Vision-Language Models with Spatial Reasoning Capabilities | 2024 · CVPR'24 | 自动合成大规模 3D 空间问答数据，让 VLM 具备定量空间推理（距离、方位） | [arXiv](https://arxiv.org/abs/2401.12168) |
| **MOKA** · Open-World Robotic Manipulation through Mark-Based Visual Prompting | 2024 · RSS'24 | 在图像上标点让 VLM 选择关键点/路径点，把操作问题转为视觉问答 | [arXiv](https://arxiv.org/abs/2403.03174) |
| **RoboPoint** · A Vision-Language Model for Spatial Affordance Prediction | 2024 · CoRL'24 | 用合成数据微调 VLM，直接输出图像上的可操作点 | [arXiv](https://arxiv.org/abs/2406.10721) |
| **ECoT** · Robotic Control via Embodied Chain-of-Thought Reasoning | 2024 · CoRL'24 | 让 VLA 在输出动作前先推理子任务、物体框、末端位置，泛化显著提升 | [arXiv](https://arxiv.org/abs/2407.08693) |
| ⭐ **ReKep** · Spatio-Temporal Reasoning of Relational Keypoint Constraints | 2024 · CoRL'24 | VLM 生成“关键点关系约束”代码，交给优化器实时求解多阶段、双臂操作 | [arXiv](https://arxiv.org/abs/2409.01652) |
| **Cosmos-Reason1** · From Physical Common Sense To Embodied Reasoning | 2025 · arXiv | NVIDIA 物理常识与具身推理 VLM，带长思维链，配套物理常识本体与基准 | [arXiv](https://arxiv.org/abs/2503.15558) |
| **RoboBrain 2.0** · Technical Report | 2025 · arXiv | 智源具身大脑：空间理解（可供性、轨迹预测）+ 时序决策（闭环交互、多智能体规划），开源 7B/32B | [arXiv](https://arxiv.org/abs/2507.02029) |
| **HY-Embodied-0.5** · Embodied Foundation Models for Real-World Agents | 2026 · arXiv | 面向真实世界智能体的具身基础模型家族，强化时空感知与预测、交互、规划等具身推理能力 | [arXiv](https://arxiv.org/abs/2604.07430) |
| **MolmoAct2** · Action Reasoning Models for Real-world Deployment | 2026 · arXiv | 完全开源的“动作推理模型”：具身推理骨干 MolmoER 超过 GPT-5 与 Gemini Robotics-ER 1.5，并开放 720 小时双臂数据 | [arXiv](https://arxiv.org/abs/2605.02881) |
| **ThinkWorld** · World Imagination Reinforces Chain-of-Dynamics Reasoning | 2026 · arXiv | 让 VLA 的“动力学思维链”接受世界模型想象结果的强化学习检验，使无动作标注的视频也能提供监督 | [arXiv](https://arxiv.org/abs/2610.37666) |

> 📅 **2026 年本方向全部 825 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#04)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
