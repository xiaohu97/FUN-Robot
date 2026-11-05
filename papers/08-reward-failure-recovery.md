# 08 · 奖励模型、失败检测与恢复 🆕

> 🆕 **2026 年新增方向**。机器人走向部署后，“怎么知道做得好不好、哪里失败了、如何恢复”变成独立的研究问题：通用奖励 / 进度 / 价值模型、成功检测与运行时监控、失败恢复与不确定性感知的策略引导。
> 主线：**Eureka / Text2Reward（LLM 写奖励）→ VIP / LIV / GVL（视频-语言价值模型）→ 2026：RoboReward / Robometer / TOPReward（通用奖励模型）→ 运行时失败检测（Hide-and-Seek）→ 失败恢复（AgentChord、LIBERO-RECOVER）**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典与奠基工作

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **VIP** · Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training | 2022 · ICLR'23 | 在人类视频上做隐式价值预训练，得到可直接当作稠密奖励的通用视觉表征 | [arXiv](https://arxiv.org/abs/2210.00030) |
| **LIV** · Language-Image Representations and Rewards for Robotic Control | 2023 · ICML'23 | 把 VIP 扩展到语言条件，统一视觉-语言表征与奖励 | [arXiv](https://arxiv.org/abs/2306.00958) |
| **Text2Reward** · Reward Shaping with Language Models for Reinforcement Learning | 2023 · ICLR'24 | 由自然语言自动生成稠密奖励函数代码，并可根据人类反馈迭代 | [arXiv](https://arxiv.org/abs/2309.11489) |
| **RoboCLIP** · One Demonstration is Enough to Learn Robot Policies | 2023 · NeurIPS'23 | 用视频-语言模型对比示教与策略轨迹生成奖励，一条示教即可训练策略 | [arXiv](https://arxiv.org/abs/2310.07899) |
| ⭐ **Eureka** · Human-Level Reward Design via Coding Large Language Models | 2023 · ICLR'24 | GPT-4 写奖励函数并进化式迭代，教会灵巧手转笔等技能，超过人类专家奖励 | [arXiv](https://arxiv.org/abs/2310.12931) · [代码](https://github.com/eureka-research/Eureka) |
| ⭐ **GVL** · Vision Language Models are In-Context Value Learners | 2024 · ICLR'25 | 打乱视频帧让 VLM 上下文预测任务进度，零样本得到通用价值函数，可用于数据筛选与成功检测 | [arXiv](https://arxiv.org/abs/2411.04549) |

## 🚀 最新进展（2025 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **RoboReward** · General-Purpose Vision-Language Reward Models for Robotics | 2026 · arXiv | 基于 OXE 与 RoboArena 构建机器人奖励数据集与基准，并用负样本增广训练 4B/8B 视觉语言奖励模型，优于更大的通用 VLM | [arXiv](https://arxiv.org/abs/2601.00675) |
| **TOPReward** · Token Probabilities as Hidden Zero-Shot Rewards for Robotics | 2026 · arXiv | 免训练的进度奖励：直接探测预训练视频语言模型的 token 概率，作为零样本稠密奖励 | [arXiv](https://arxiv.org/abs/2602.19313) |
| **UPS** · When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering | 2026 · RSS'26 | 不确定性感知的策略引导：在“直接执行 / 用语言澄清任务 / 请求人工干预”之间自动选择 | [arXiv](https://arxiv.org/abs/2602.22474) |
| **Robometer** · Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons | 2026 · RSS'26 | 轨迹内进度监督 + 轨迹间偏好比较训练通用机器人奖励模型，能利用大量失败/次优数据 | [arXiv](https://arxiv.org/abs/2603.02115) |
| **Large Reward Models** · Generalizable Online Robot Reward Generation with Vision-Language Models | 2026 · arXiv | 用视觉语言模型在线生成可泛化、可复用的机器人奖励，服务真机 RL | [arXiv](https://arxiv.org/abs/2603.16065) |
| **PRM-as-a-Judge** · A Dense Evaluation Paradigm for Fine-Grained Robotic Auditing | 2026 · arXiv | 用过程奖励模型从轨迹视频估计任务进度，对策略执行做稠密、细粒度的审计与评估 | [arXiv](https://arxiv.org/abs/2603.21669) |
| **ViVa** · A Video-Generative Value Model for Robot Reinforcement Learning | 2026 · arXiv | 把预训练视频生成模型改造成价值模型（联合预测未来本体状态与价值），接入 RECAP 提升真机 RL | [arXiv](https://arxiv.org/abs/2604.08168) |
| **ProcVLM** · Learning Procedure-Grounded Progress Rewards for Robotic Manipulation | 2026 · arXiv | 按子任务结构合成帧级进度标注，训练“过程感知”的进度奖励 VLM | [arXiv](https://arxiv.org/abs/2605.08774) |
| **AgentChord** · From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation | 2026 · RSS'26 | 把操作任务建模为有向任务图，预判可能的失败并提前规划恢复，长程双臂任务成功率显著提升 | [arXiv](https://arxiv.org/abs/2605.11951) |
| **Hide-and-Seek in Trajectories** · Discovering Failure Signals for VLA Runtime Monitoring | 2026 · NeurIPS'26 | 从 VLA 自身轨迹特征中发现失败信号，实现运行时失败检测 | [arXiv](https://arxiv.org/abs/2605.30834) |
| **LIBERO-RECOVER** · Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models | 2026 · arXiv | 在 LIBERO 上专门评测 VLA / WAM 的失败恢复能力，揭示“近 100% 成功率”背后的脆弱性 | [arXiv](https://arxiv.org/abs/2609.05178) |
| **RoboValue** · A Fine-Grained Sim-and-Real Benchmark for Unified Evaluation of Robotic Value Models | 2026 · arXiv | 仿真 + 真机细粒度基准，统一评测机器人价值模型 | [arXiv](https://arxiv.org/abs/2610.26663) |

## 🔗 相关

- 奖励模型用于 RL 后训练见 [`07`](./07-rl-post-training.md)；综述 Progress Reward Modeling 见 [`18`](./18-surveys.md)

> 📅 **2026 年本方向全部 135 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#08)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
