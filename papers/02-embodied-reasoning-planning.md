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
| **RoboReward** · General-Purpose Vision-Language Reward Models for Robotics | 2026 · arXiv | 基于 OXE 与 RoboArena 构建机器人奖励数据集与基准，并用负样本增广训练 4B/8B 视觉语言奖励模型，优于更大的通用 VLM | [arXiv](https://arxiv.org/abs/2601.00675) |
| **Robometer** · Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | 2026 · RSS'26 | 轨迹内进度监督 + 轨迹间偏好比较训练通用机器人奖励模型，能利用大量失败/次优数据 | [arXiv](https://arxiv.org/abs/2603.02115) |
| **CaP-X** · A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation | 2026 · arXiv | 系统评测与改进“代码即策略”智能体的开放框架：12 个模型上发现依赖人工抽象，可用多轮交互、执行反馈等测试时计算弥补 | [arXiv](https://arxiv.org/abs/2603.22435) |
| **HY-Embodied-0.5** · Embodied Foundation Models for Real-World Agents | 2026 · arXiv | 面向真实世界智能体的具身基础模型家族，强化时空感知与预测、交互、规划等具身推理能力 | [arXiv](https://arxiv.org/abs/2604.07430) |
| **MolmoAct2** · Action Reasoning Models for Real-world Deployment | 2026 · arXiv | 完全开源的“动作推理模型”：具身推理骨干 MolmoER 超过 GPT-5 与 Gemini Robotics-ER 1.5，并开放 720 小时双臂数据 | [arXiv](https://arxiv.org/abs/2605.02881) |
| **ENPIRE** · Agentic Robot Policy Self-Improvement in the Real World | 2026 · CoRL'26 | 为编程智能体搭建“重置-执行-验证-改进”的真实世界闭环，自动迭代提升灵巧操作策略 | [arXiv](https://arxiv.org/abs/2606.19980) |
| **ASPIRE** · Agentic /Skills Discovery for Robotics | 2026 · arXiv | 智能体自主编写并迭代机器人控制代码、沉淀为可复用技能库，在未见长程任务上零样本成功率 31%（前作 4%） | [arXiv](https://arxiv.org/abs/2607.00272) |
| **Zetta ζ** · An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence | 2026 · arXiv | 冻结基础策略，在线自我进化基于代码的运行时评判器与恢复技能，LIBERO-Pro 90.8%、RoboCasa 93.6% | [arXiv](https://arxiv.org/abs/2608.16590) |
| **Show-Harness** · Just a VLM Agent Can Play Robots | 2026 · arXiv | 用紧凑的语义动作接口让 VLM 直接“玩”机器人：闭源大模型零样本控制，开源小模型几 GPU 小时即可微调部署 | [arXiv](https://arxiv.org/abs/2609.10522) |
| **RoboDawn** · Transferring the Intelligence of VLMs to Robotic Control | 2026 · arXiv | 离散平移/旋转/夹爪指令接口 + 少样本上下文学习，让智能体式 VLM 闭环控制机器人，迁移 VLM 通用智能 | [arXiv](https://arxiv.org/abs/2609.22966) |
| **LLM as Policy** · An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond | 2026 · arXiv | 系统评测 GPT-6 Astra 等大模型不经微调直接作为操作策略：语义任务表现强，但精细、动态和双臂协调任务明显不足 | [arXiv](https://arxiv.org/abs/2609.24170) |
| **RoboICL** · Embodied In-Context Learning with GPT-6 Astra | 2026 · arXiv | 示教上下文 + 交互记忆的上下文学习框架，不更新参数、不训练 VLA 即可提升大模型直接控制机器人的成绩 | [arXiv](https://arxiv.org/abs/2609.34261) |
| **OpenRUA** · Robot-Use Agents Are Zero-Shot Visuomotor Policies | 2026 · arXiv | 只给现成编程智能体 ROS 2 终端权限、不做任何额外抽象，即可作为零样本视觉运动策略（LIBERO-PRO 87%） | [arXiv](https://arxiv.org/abs/2610.02459) |
| **PhysEvo** · Astra Can Act, Let It | 2026 · arXiv | 围绕单个冻结模型的物理世界递归自我改进：元智能体诊断失败、修订工具与技能并验证 | [arXiv](https://arxiv.org/abs/2610.08995) |
| **Has GPT-6-Astra Achieved Embodied Intelligence?** | 2026 · arXiv | 在 12 个基准上大规模评测通用大模型 GPT-6-Astra 的具身能力：已跨过“具身胜任”门槛，但离实用具身智能仍有距离 | [arXiv](https://arxiv.org/abs/2610.22471) |
| **ThinkWorld** · World Imagination Reinforces Chain-of-Dynamics Reasoning | 2026 · arXiv | 让 VLA 的“动力学思维链”接受世界模型想象结果的强化学习检验，使无动作标注的视频也能提供监督 | [arXiv](https://arxiv.org/abs/2610.37666) |
| **CaPtain** · A Pipeline for Post-Training Code-as-Policy Robot Agents | 2026 · arXiv | 开源后训练流程（合成轨迹 SFT + 多轮 RL + 物理评判器），把小型开源 VLM 训练成代码即策略智能体 | [arXiv](https://arxiv.org/abs/2610.40799) |
| **uni-robot-agent** · Democratizing Robot-Use Agents: A Unified Harness with Open Models | 2026 · arXiv | 统一的开源机器人智能体框架，开放权重模型在 RoboDojo 上超过 GPT-6 Astra 已公布成绩 | [arXiv](https://arxiv.org/abs/2611.01560) |

> Gemini Robotics-ER 1.5 收录在 [`01`](./01-vla-foundation-models.md) 的 Gemini Robotics 1.5 条目中。

> 📅 **2026 年本方向全部 1097 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#02)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
