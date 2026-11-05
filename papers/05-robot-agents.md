# 05 · 机器人智能体与自我进化（Robot-Use Agents / Embodied Harness）🆕

> 🆕 **2026 年新增方向**。让通用大模型（GPT-6 Astra、Claude、Qwen 等）通过一层“框架”（harness）直接控制机器人：写代码调用接口、调度冻结的 VLA 技能、在执行中诊断失败、把经验沉淀为技能库并**自我进化**，基本不训练机器人专用模型。
> 数据：该方向下半年论文占比是上半年的 5.3 倍；9–10 月摘要提到 GPT-6 Astra 的论文共 53 篇。
> 主线：**Code as Policies / Voyager（代码策略 + 技能库）→ CaP-X（代码智能体基准）→ Show-Harness / OpenRUA（大模型零样本控制）→ Zetta / PhysEvo / RoboFoundry（在线自我进化）→ LLM as Policy 评测（语义强、精细控制弱）**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典与奠基工作

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **Code as Policies** · Language Model Programs for Embodied Control | 2022 · ICRA'23 | LLM 直接生成调用感知/控制 API 的 Python 代码作为策略，可组合、可解释 | [arXiv](https://arxiv.org/abs/2209.07753) |
| **Voyager** · An Open-Ended Embodied Agent with Large Language Models | 2023 · TMLR | Minecraft 中的终身学习智能体：自动课程 + 技能代码库 + 自我验证 | [arXiv](https://arxiv.org/abs/2305.16291) |

## 🚀 最新进展（2025 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **RoboClaw** · An Agentic Framework for Scalable Long-Horizon Robotic Tasks | 2026 · arXiv | 由 VLM 统一驱动数据采集、策略学习与执行的智能体框架，减少人工复位，支撑长程任务 | [arXiv](https://arxiv.org/abs/2603.11558) |
| ⭐ **CaP-X** · A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation | 2026 · arXiv | 系统评测与改进“代码即策略”智能体的开放框架：12 个模型上发现依赖人工抽象，可用多轮交互、执行反馈等测试时计算弥补 | [arXiv](https://arxiv.org/abs/2603.22435) |
| **ENPIRE** · Agentic Robot Policy Self-Improvement in the Real World | 2026 · CoRL'26 | 为编程智能体搭建“重置-执行-验证-改进”的真实世界闭环，自动迭代提升灵巧操作策略 | [arXiv](https://arxiv.org/abs/2606.19980) |
| **ASPIRE** · Agentic /Skills Discovery for Robotics | 2026 · arXiv | 智能体自主编写并迭代机器人控制代码、沉淀为可复用技能库，在未见长程任务上零样本成功率 31%（前作 4%） | [arXiv](https://arxiv.org/abs/2607.00272) |
| **Harness VLA** · Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents | 2026 · arXiv | 把冻结的 VLA 当作可重试的接触操作原语，由记忆增强智能体与解析原语组合调度，LIBERO-Pro 上提升 38.6 个点 | [arXiv](https://arxiv.org/abs/2607.08448) |
| **Zetta ζ** · An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence | 2026 · arXiv | 冻结基础策略，在线自我进化基于代码的运行时评判器与恢复技能，LIBERO-Pro 90.8%、RoboCasa 93.6% | [arXiv](https://arxiv.org/abs/2608.16590) |
| **Show-Harness** · Just a VLM Agent Can Play Robots | 2026 · arXiv | 用紧凑的语义动作接口让 VLM 直接“玩”机器人：闭源大模型零样本控制，开源小模型几 GPU 小时即可微调部署 | [arXiv](https://arxiv.org/abs/2609.10522) |
| **RoboDawn** · Transferring the Intelligence of VLMs to Robotic Control | 2026 · arXiv | 离散平移/旋转/夹爪指令接口 + 少样本上下文学习，让智能体式 VLM 闭环控制机器人，迁移 VLM 通用智能 | [arXiv](https://arxiv.org/abs/2609.22966) |
| **LLM as Policy** · An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond | 2026 · arXiv | 系统评测 GPT-6 Astra 等大模型不经微调直接作为操作策略：语义任务表现强，但精细、动态和双臂协调任务明显不足 | [arXiv](https://arxiv.org/abs/2609.24170) |
| **RoboFoundry** · System-as-Policy Evolution for Self-Learning Embodied Agents | 2026 · arXiv | “系统即策略”的自我进化：诊断能力缺口，把执行经验转化为经过验证的系统级改动 | [arXiv](https://arxiv.org/abs/2609.32862) |
| **RoboICL** · Embodied In-Context Learning with GPT-6 Astra | 2026 · arXiv | 示教上下文 + 交互记忆的上下文学习框架，不更新参数、不训练 VLA 即可提升大模型直接控制机器人的成绩 | [arXiv](https://arxiv.org/abs/2609.34261) |
| **OpenRUA** · Robot-Use Agents Are Zero-Shot Visuomotor Policies | 2026 · arXiv | 只给现成编程智能体 ROS 2 终端权限、不做任何额外抽象，即可作为零样本视觉运动策略（LIBERO-PRO 87%） | [arXiv](https://arxiv.org/abs/2610.02459) |
| **PhysEvo** · Astra Can Act, Let It | 2026 · arXiv | 围绕单个冻结模型的物理世界递归自我改进：元智能体诊断失败、修订工具与技能并验证 | [arXiv](https://arxiv.org/abs/2610.08995) |
| **Has GPT-6-Astra Achieved Embodied Intelligence?** | 2026 · arXiv | 在 12 个基准上大规模评测通用大模型 GPT-6-Astra 的具身能力：已跨过“具身胜任”门槛，但离实用具身智能仍有距离 | [arXiv](https://arxiv.org/abs/2610.22471) |
| **CaPtain** · A Pipeline for Post-Training Code-as-Policy Robot Agents | 2026 · arXiv | 开源后训练流程（合成轨迹 SFT + 多轮 RL + 物理评判器），把小型开源 VLM 训练成代码即策略智能体 | [arXiv](https://arxiv.org/abs/2610.40799) |
| **uni-robot-agent** · Democratizing Robot-Use Agents: A Unified Harness with Open Models | 2026 · arXiv | 统一的开源机器人智能体框架，开放权重模型在 RoboDojo 上超过 GPT-6 Astra 已公布成绩 | [arXiv](https://arxiv.org/abs/2611.01560) |

## 🔗 相关

- 评测平台：RoboDojo、RobotWorld、HexaShell 见 [`17`](./17-simulation-benchmarks.md)

> 📅 **2026 年本方向全部 182 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#05)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
