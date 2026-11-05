# 11 · 仿真平台、Sim2Real 与评测基准

> 仿真提供“无限数据 + 安全试错”，Sim2Real 解决“仿真学的能不能在真机用”，基准让不同方法可比。
> 基准的评测指标与 SOTA 汇总见 [`benchmarks/README.md`](../benchmarks/README.md)；仿真器/框架的上手指南见 [`projects/README.md`](../projects/README.md)。

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **MuJoCo** · A Physics Engine for Model-Based Control | 2012 · IROS'12 | 面向控制与优化的高效接触物理引擎，RL/机器人领域最常用仿真器之一 | [论文](https://ieeexplore.ieee.org/document/6386109) · [代码](https://github.com/google-deepmind/mujoco) |
| ⭐ **Domain Randomization** · for Transferring Deep Neural Networks from Simulation to the Real World | 2017 · IROS'17 | 随机化仿真中的纹理、光照、相机，让只在仿真中训练的检测器直接用于真机 | [arXiv](https://arxiv.org/abs/1703.06907) |
| **Dynamics Randomization** · Sim-to-Real Transfer of Robotic Control with Dynamics Randomization | 2017 · ICRA'18 | 随机化质量、摩擦、阻尼等动力学参数，策略零样本迁移到真实机械臂 | [arXiv](https://arxiv.org/abs/1710.06537) |
| **Habitat** · A Platform for Embodied AI Research | 2019 · ICCV'19 | 每秒数千帧的高性能具身仿真平台，导航研究的事实标准 | [arXiv](https://arxiv.org/abs/1904.01201) · [代码](https://github.com/facebookresearch/habitat-lab) |
| **RLBench** · The Robot Learning Benchmark & Learning Environment | 2019 · RA-L'20 | 100 个操作任务的基准，3D 操作策略（PerAct、RVT 等）的标准评测 | [arXiv](https://arxiv.org/abs/1909.12271) · [代码](https://github.com/stepjam/RLBench) |
| ⭐ **Isaac Gym** · High Performance GPU-Based Physics Simulation for Robot Learning | 2021 · NeurIPS'21 | 物理仿真与策略训练都在 GPU 上，数千环境并行，开启大规模并行 RL 时代 | [arXiv](https://arxiv.org/abs/2108.10470) |
| **CALVIN** · A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks | 2021 · RA-L'22 | 语言条件长程操作基准，考察连续完成 5 个子任务的能力 | [arXiv](https://arxiv.org/abs/2112.03227) · [代码](https://github.com/mees/calvin) |

## 🚀 最新进展（2023 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **Orbit** · A Unified Simulation Framework for Interactive Robot Learning Environments | 2023 · RA-L'23 | 基于 Isaac Sim 的模块化机器人学习框架（Isaac Lab 前身） | [arXiv](https://arxiv.org/abs/2301.04195) |
| ⭐ **LIBERO** · Benchmarking Knowledge Transfer for Lifelong Robot Learning | 2023 · NeurIPS'23 | 130 个任务的终身学习操作基准，现为 VLA 微调最常用的仿真评测 | [arXiv](https://arxiv.org/abs/2306.03310) · [代码](https://github.com/Lifelong-Robot-Learning/LIBERO) |
| **Habitat 3.0** · A Co-Habitat for Humans, Avatars and Robots | 2023 · ICLR'24 | 支持人形虚拟人与机器人共处的仿真，研究人机协作 | [arXiv](https://arxiv.org/abs/2310.13724) |
| **BEHAVIOR-1K** · A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities | 2024 · arXiv | 基于 OmniGibson 的 1000 个日常家务活动基准，强调真实感与长程任务 | [arXiv](https://arxiv.org/abs/2403.09227) |
| ⭐ **SIMPLER** · Evaluating Real-World Robot Manipulation Policies in Simulation | 2024 · CoRL'24 | 复刻真机场景的仿真评测，结果与真机表现高度相关，用于评测 RT-1/Octo/OpenVLA 等 | [arXiv](https://arxiv.org/abs/2405.05941) · [代码](https://github.com/simpler-env/SimplerEnv) |
| **RoboCasa** · Large-Scale Simulation of Everyday Tasks for Generalist Robots | 2024 · RSS'24 | 大规模厨房场景 + 生成式资产 + 自动数据生成，研究仿真数据 scaling | [arXiv](https://arxiv.org/abs/2406.02523) · [代码](https://github.com/robocasa/robocasa) |
| **ManiSkill3** · GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI | 2024 · RSS'25 | GPU 并行物理 + 渲染，视觉 RL 训练速度大幅提升 | [arXiv](https://arxiv.org/abs/2410.00425) · [代码](https://github.com/haosulab/ManiSkill) |
| **MuJoCo Playground** | 2025 · RSS'25 | 基于 MJX 的 GPU 训练环境集合，几分钟训练四足/人形/灵巧手策略并 sim2real | [arXiv](https://arxiv.org/abs/2502.08844) · [代码](https://github.com/google-deepmind/mujoco_playground) |
| ⭐ **Isaac Lab** · A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning | 2025 · arXiv | Isaac Gym 继任者：GPU 并行物理 + RTX 渲染 + 执行器模型 + 传感器仿真 + 数据采集，覆盖全身控制到灵巧操作 | [arXiv](https://arxiv.org/abs/2511.04831) · [代码](https://github.com/isaac-sim/IsaacLab) |
| **mjlab** · A Lightweight Framework for GPU-Accelerated Robot Learning | 2026 · arXiv | 轻量开源 GPU 机器人学习框架：Isaac Lab 式模块化 API + MuJoCo Warp 物理，一行命令安装 | [arXiv](https://arxiv.org/abs/2601.22074) |
| **WorldArena** · A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models | 2026 · arXiv | 统一评测具身世界模型的感知质量与功能效用，提出 EWMScore，揭示“画面好 ≠ 任务能力强” | [arXiv](https://arxiv.org/abs/2602.08971) |
| **UniVTAC** · A Unified Simulation Platform for Visuo-Tactile Manipulation Data Generation, Learning, and Benchmarking | 2026 · arXiv | 支持三种视触觉传感器的仿真数据合成平台，配套视触觉编码器与基准 | [arXiv](https://arxiv.org/abs/2602.10093) |
| **MolmoSpaces** · A Large-Scale Open Ecosystem for Robot Navigation and Manipulation | 2026 · arXiv | 大规模开放机器人导航与操作仿真生态 + 8 任务基准，仿真与真机成绩高度相关（R = 0.96） | [arXiv](https://arxiv.org/abs/2602.11337) |
| **RMBench** · Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design | 2026 · arXiv | 9 个不同记忆复杂度的操作任务基准 + 显式记忆模块化策略 Mem-0，分析策略记忆能力的设计要点 | [arXiv](https://arxiv.org/abs/2603.01229) |
| **RoboCasa365** · A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots | 2026 · ICLR'26 | 大规模家庭移动操作仿真框架与基准，支持多任务学习、基础模型训练与终身学习等评测设置 | [arXiv](https://arxiv.org/abs/2603.04356) |
| **Interactive World Simulator for Robot Policy Training and Evaluation** | 2026 · arXiv | 可交互的学习式世界模拟器，用于刚体、可变形物体、堆叠物等任务的策略训练与评测，结果与真机一致 | [arXiv](https://arxiv.org/abs/2603.08546) |
| **RoboLab** · A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies | 2026 · arXiv | 高保真仿真基准，研究仿真行为能在多大程度上解释通用策略的真机表现，以及哪些因素影响最大 | [arXiv](https://arxiv.org/abs/2604.09860) |
| **RoboMemArena** · A Comprehensive and Challenging Robotic Memory Benchmark | 2026 · arXiv | 26 个任务的大规模机器人记忆基准，并提出带记忆库与预测编码的双系统 VLA（PrediMem） | [arXiv](https://arxiv.org/abs/2605.10921) |
| **DexJoCo** · A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo | 2026 · arXiv | 基于 MuJoCo 的任务导向灵巧操作基准与工具包：11 个任务覆盖工具使用、双手协调、长程与推理，含 1100 条人类示教 | [arXiv](https://arxiv.org/abs/2605.16257) |
| ⭐ **RoboDojo** · A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies | 2026 · arXiv | 统一的仿真 + 真机基准与公开排行榜，集成 30 个通用操作策略进行系统评测，2026 年下半年被大量论文采用 | [arXiv](https://arxiv.org/abs/2607.04434) |
| **RobotWorld** · Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments | 2026 · arXiv | 面向“机器人使用”的多模态智能体仿真测试平台，覆盖多种任务与本体，分析执行轨迹中的能力与失败模式 | [arXiv](https://arxiv.org/abs/2610.10409) |
| **HexaShell** · A Universal Harness for Robot Coding Agents in Simulation and the Real World | 2026 · arXiv | 给编程智能体一个极薄的命令行接口来控制机器人（仿真与真机），研究编程智能体操控机器人能走多远 | [arXiv](https://arxiv.org/abs/2610.23479) |

> 📅 **2026 年本方向全部 484 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#11)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
