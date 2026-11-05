# 09 · 记忆与长时程任务 🆕

> 🆕 **2026 年新增方向**。VLA 默认只看当前一帧，遇到“数一数做了几次”“物体被挡住了”“15 分钟的做饭任务”就会失败。2026 年出现了大量给机器人策略加**记忆**的工作，以及专门的记忆基准。
> 数据：标题含 memory 的论文从上半年的 59 篇增长到下半年的 154 篇。
> 主线：**MemoryVLA（感知-认知双记忆）→ MEM（视频短时 + 文本长时多尺度记忆）→ RoboMME / RMBench / RoboMemArena（记忆基准）→ 潜在记忆、事件记忆、记忆即规划**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🚀 最新进展（2025 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **MemoryVLA** · Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation | 2025 · arXiv | 受人类工作记忆启发的感知-认知双记忆库，提升 VLA 在依赖历史的长程任务上的表现 | [arXiv](https://arxiv.org/abs/2508.19236) |
| **PALM** · Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation | 2026 · CVPR'26 | 以交互式可供性推理与子任务进度线索组织策略学习，LIBERO-LONG 91.8% | [arXiv](https://arxiv.org/abs/2601.07060) |
| **BPP** · Long-Context Robot Imitation Learning by Focusing on Key History Frames | 2026 · arXiv | 只以 VLM 检测出的少量关键历史帧为条件，缓解长上下文模仿学习中的虚假相关与分布偏移 | [arXiv](https://arxiv.org/abs/2602.15010) |
| **RMBench** · Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design | 2026 · arXiv | 9 个不同记忆复杂度的操作任务基准 + 显式记忆模块化策略 Mem-0，分析策略记忆能力的设计要点 | [arXiv](https://arxiv.org/abs/2603.01229) |
| ⭐ **MEM** · Multi-Scale Embodied Memory for Vision Language Action Models | 2026 · arXiv | Physical Intelligence 的多尺度记忆：视频短时记忆 + 文本长时记忆，支撑长达 15 分钟的任务（收拾厨房、做烤三明治） | [arXiv](https://arxiv.org/abs/2603.03596) |
| ⭐ **RoboMME** · Benchmarking and Understanding Memory for Robotic Generalist Policies | 2026 · ICML'26 | 记忆基准：16 个任务覆盖时间、空间、物体、程序四类记忆，并在 π0.5 上系统比较 14 种记忆增强 VLA | [arXiv](https://arxiv.org/abs/2603.04639) |
| **ReMem-VLA** · Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries | 2026 · arXiv | 帧级 + 块级两组循环记忆查询，分别承载短时与长时记忆的 VLA | [arXiv](https://arxiv.org/abs/2603.12942) |
| **RoboMemArena** · A Comprehensive and Challenging Robotic Memory Benchmark | 2026 · arXiv | 26 个任务的大规模机器人记忆基准，并提出带记忆库与预测编码的双系统 VLA（PrediMem） | [arXiv](https://arxiv.org/abs/2605.10921) |
| **EventVLA** · Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies | 2026 · arXiv | 稀疏“视觉证据记忆”：保留初始与近期视觉锚点 + 动态关键帧证据记忆模块 | [arXiv](https://arxiv.org/abs/2606.20092) |
| **LaMem-VLA** · Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation | 2026 · arXiv | 把历史经验重构为潜在记忆 token，与 VLA 推理在同一连续潜空间中直接交织 | [arXiv](https://arxiv.org/abs/2607.07608) |
| **ABot-AgentOS** · A General Robotic Agent OS with Lifelong Multi-modal Memory | 2026 · arXiv | 位于底层控制之上的通用机器人智能体操作系统，提供终身多模态记忆、工具调用、验证与跨本体执行 | [arXiv](https://arxiv.org/abs/2607.10350) |
| **MaP-WAM** · Memory as Plans: World-Action Modeling with Memory-Grounded Planning | 2026 · arXiv | Memory-as-Plans：把依赖记忆的世界动作建模拆成“基于记忆的规划 + 计划条件执行” | [arXiv](https://arxiv.org/abs/2609.11561) |

> 📅 **2026 年本方向全部 587 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#09)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
