# 06 · 操作、抓取与灵巧手

> 从“抓得起来”到“用得巧”：抓取检测 → 语言条件操作 → 3D 表征策略 → 多指灵巧手（RL + sim2real、触觉、从人类视频学习）。

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **Dex-Net 2.0** · Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics | 2017 · RSS'17 | 670 万合成点云 + 解析抓取指标训练 GQ-CNN，开启“仿真合成数据学抓取” | [arXiv](https://arxiv.org/abs/1703.09312) |
| **Dactyl** · Learning Dexterous In-Hand Manipulation | 2018 · IJRR'20 | 大规模域随机化 RL，Shadow 手在真机上完成方块重定向 | [arXiv](https://arxiv.org/abs/1808.00177) |
| ⭐ **Rubik's Cube** · Solving Rubik's Cube with a Robot Hand | 2019 · arXiv | 自动域随机化（ADR），灵巧手单手还原魔方，sim2real 里程碑 | [arXiv](https://arxiv.org/abs/1910.07113) |
| **Transporter Networks** · Rearranging the Visual World for Robotic Manipulation | 2020 · CoRL'20 | 空间特征“搬运”的平移等变结构，少量示教学会桌面重排 | [arXiv](https://arxiv.org/abs/2010.14406) |
| **Where2Act** · From Pixels to Actions for Articulated 3D Objects | 2021 · ICCV'21 | 逐像素预测铰接物体（抽屉、门）的可交互位置与动作 | [arXiv](https://arxiv.org/abs/2101.02692) |
| **Contact-GraspNet** · Efficient 6-DoF Grasp Generation in Cluttered Scenes | 2021 · ICRA'21 | 以接触点表示 6-DoF 抓取，在杂乱场景中从深度图直接生成抓取 | [arXiv](https://arxiv.org/abs/2103.14127) |
| **DexMV** · Imitation Learning for Dexterous Manipulation from Human Videos | 2021 · ECCV'22 | 从人类视频中估计手-物位姿并重定向到灵巧手，作为示教加速 RL | [arXiv](https://arxiv.org/abs/2108.05877) |
| ⭐ **CLIPort** · What and Where Pathways for Robotic Manipulation | 2021 · CoRL'21 | CLIP 语义通路 + Transporter 空间通路，语言条件桌面操作 | [arXiv](https://arxiv.org/abs/2109.12098) · [代码](https://github.com/cliport/cliport) |
| ⭐ **PerAct** · Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation | 2022 · CoRL'22 | 体素化 3D 观测 + Perceiver Transformer 预测下一关键位姿，少量示教完成多任务 6-DoF 操作 | [arXiv](https://arxiv.org/abs/2209.05451) · [代码](https://github.com/peract/peract) |
| **DexGraspNet** · A Large-Scale Robotic Dexterous Grasp Dataset | 2022 · ICRA'23 | 基于可微力闭合优化生成 132 万个灵巧手抓取，覆盖 5000+ 物体 | [arXiv](https://arxiv.org/abs/2210.02697) |
| **In-Hand Object Rotation** · via Rapid Motor Adaptation | 2022 · CoRL'22 | 把 RMA 思路用到灵巧手，仅凭本体感知旋转各种形状物体 | [arXiv](https://arxiv.org/abs/2210.04887) |
| **Visual Dexterity** · In-Hand Reorientation of Novel and Complex Object Shapes | 2022 · Science Robotics | 深度相机 + 实时点云策略，手掌朝下重定向任意新物体 | [arXiv](https://arxiv.org/abs/2211.11744) |
| **AnyGrasp** · Robust and Efficient Grasp Perception in Spatial and Temporal Domains | 2022 · T-RO'23 | 稠密 7-DoF 抓取检测 + 时序关联，可抓动态物体，工业可用 | [arXiv](https://arxiv.org/abs/2212.08333) |

## 🚀 最新进展（2023 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **RoboPianist** · Dexterous Piano Playing with Deep RL | 2023 · CoRL'23 | 双灵巧手弹钢琴的高维控制基准与 RL 基线 | [arXiv](https://arxiv.org/abs/2304.04150) |
| **RVT** · Robotic View Transformer for 3D Object Manipulation | 2023 · CoRL'23 | 把点云重渲染成多个虚拟视角再做 Transformer，比 PerAct 更快更准 | [arXiv](https://arxiv.org/abs/2306.14896) · [代码](https://github.com/NVlabs/RVT) |
| **Act3D** · 3D Feature Field Transformers for Multi-Task Robotic Manipulation | 2023 · CoRL'23 | 自适应 3D 特征场采样定位末端位姿，提升高精度多任务操作 | [arXiv](https://arxiv.org/abs/2306.17817) |
| ⭐ **3D Diffuser Actor** · Policy Diffusion with 3D Scene Representations | 2024 · CoRL'24 | 3D 场景 tokens + 扩散动作生成，在 RLBench / CALVIN 上大幅领先 | [arXiv](https://arxiv.org/abs/2402.10885) · [代码](https://github.com/nickgkan/3d_diffuser_actor) |
| ⭐ **DexterityGen** · Foundation Controller for Unprecedented Dexterity | 2025 · arXiv | RL 预训练大规模灵巧运动原语，作为“基础控制器”接收遥操作/策略的粗指令，稳定性提升 10~100 倍 | [arXiv](https://arxiv.org/abs/2502.04307) |
| **Grasp, Slide, Roll** · Comparative Analysis of Contact Modes for Tactile-Based Shape Reconstruction | 2026 · arXiv | 比较抓放、指尖滑动、掌心滚动三种触觉接触模式，滑动/滚动少用约 34% 接触完成纯触觉形状重建 | [arXiv](https://arxiv.org/abs/2602.23206) |
| **SPARR** · Simulation-based Policies with Asymmetric Real-world Residuals for Assembly | 2026 · ICRA'26 | 仿真状态基策略 + 真机视觉残差策略，无需示教在装配任务上达到 95~100% 成功率 | [arXiv](https://arxiv.org/abs/2602.23253) · [主页](https://research.nvidia.com/labs/srl/projects/sparr/) |
| **HANDFUL** · Sequential Grasp-Conditioned Dexterous Manipulation with Resource Awareness | 2026 · arXiv | 研究“手里握着一个物体的同时再做另一个操作”的序列灵巧操作，LEAP 手真机验证 | [arXiv](https://arxiv.org/abs/2604.25126) |
| **Human2Dex** · Dexterous Robot Learning from Wrist-Centric Human Demonstrations | 2026 · arXiv | 人与机器人共享 21 点手部表示，把腕部视角的人类示教重定向到各种灵巧手 | [arXiv](https://arxiv.org/abs/2610.13119) |
| **HandMimicX** · Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos | 2026 · arXiv | 以物体运动（而非手部轨迹）定义 RL 目标，从第一视角人类视频学习灵巧技能 | [arXiv](https://arxiv.org/abs/2610.41336) |
