# 02 · 具身推理与任务规划（LLM / VLM for Robotics）

> 大模型负责“想”：理解指令、分解任务、推断空间关系、生成代码或奖励；底层技能负责“做”。
> 主线：**LLM 零样本规划 → SayCan（可行性约束）→ Code as Policies（代码即策略）→ VoxPoser / ReKep（空间约束）→ 具身推理 VLM（Cosmos-Reason / RoboBrain / Gemini-ER）**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **LM Zero-Shot Planners** · Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents | 2022 · ICML'22 | 首次展示 LLM 无需训练即可把高层指令分解为可执行步骤 | [arXiv](https://arxiv.org/abs/2201.07207) |
| ⭐ **SayCan** · Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022 · CoRL'22 | LLM 判断“该做什么”，价值函数判断“能否做成”，两者相乘选择技能 | [arXiv](https://arxiv.org/abs/2204.01691) |
| **Inner Monologue** · Embodied Reasoning through Planning with Language Models | 2022 · CoRL'22 | 把成功检测、场景描述、人类反馈作为语言反馈闭环喂给 LLM 规划器 | [arXiv](https://arxiv.org/abs/2207.05608) |
| ⭐ **Code as Policies** · Language Model Programs for Embodied Control | 2022 · ICRA'23 | LLM 直接生成调用感知/控制 API 的 Python 代码作为策略，可组合、可解释 | [arXiv](https://arxiv.org/abs/2209.07753) |
| **ProgPrompt** · Generating Situated Robot Task Plans using Large Language Models | 2022 · ICRA'23 | 程序化提示（可用动作 + 物体 + 断言）让 LLM 生成与环境匹配的任务计划 | [arXiv](https://arxiv.org/abs/2209.11302) |
| **Voyager** · An Open-Ended Embodied Agent with Large Language Models | 2023 · TMLR | Minecraft 中的终身学习智能体：自动课程 + 技能代码库 + 自我验证 | [arXiv](https://arxiv.org/abs/2305.16291) |
| **SayPlan** · Grounding LLMs using 3D Scene Graphs for Scalable Robot Task Planning | 2023 · CoRL'23 | 在 3D 场景图上做语义搜索与迭代重规划，扩展到多楼层大场景 | [arXiv](https://arxiv.org/abs/2307.06135) |
| ⭐ **VoxPoser** · Composable 3D Value Maps for Robotic Manipulation with Language Models | 2023 · CoRL'23 | LLM 写代码调用 VLM，组合出 3D 可供性/约束价值图，零样本合成轨迹 | [arXiv](https://arxiv.org/abs/2307.05973) · [代码](https://github.com/huangwl18/VoxPoser) |
| **Text2Reward** · Reward Shaping with Language Models for Reinforcement Learning | 2023 · ICLR'24 | 由自然语言自动生成稠密奖励函数代码，并可根据人类反馈迭代 | [arXiv](https://arxiv.org/abs/2309.11489) |
| ⭐ **Eureka** · Human-Level Reward Design via Coding Large Language Models | 2023 · ICLR'24 | GPT-4 写奖励函数并进化式迭代，教会灵巧手转笔等技能，超过人类专家奖励 | [arXiv](https://arxiv.org/abs/2310.12931) · [代码](https://github.com/eureka-research/Eureka) |

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

> Gemini Robotics-ER 1.5 收录在 [`01`](./01-vla-foundation-models.md) 的 Gemini Robotics 1.5 条目中。
