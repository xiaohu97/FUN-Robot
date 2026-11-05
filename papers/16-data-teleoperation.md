# 16 · 数据采集、遥操作与人类视频

> 数据是具身智能的最大瓶颈。三条路线：**真机遥操作**（ALOHA、GELLO、VR）、**无机器人采集**（UMI、手机采集）、**人类视频**（第一视角视频 → 机器人数据），以及自动数据生成（MimicGen）。2026 年人类视频规模达到百万小时级。
> 数据集详细字段见 [`datasets/README.md`](../datasets/README.md)。

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **RoboTurk** · A Crowdsourcing Platform for Robotic Skill Learning through Imitation | 2018 · CoRL'18 | 用手机做众包遥操作，低成本大规模采集示教数据 | [arXiv](https://arxiv.org/abs/1811.02790) |
| **RoboNet** · Large-Scale Multi-Robot Learning | 2019 · CoRL'19 | 7 种机器人、1500 万帧的多机器人数据集，早期跨本体数据探索 | [arXiv](https://arxiv.org/abs/1910.11215) |

## 🚀 最新进展（2023 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **AnyTeleop** · A General Vision-Based Dexterous Robot Arm-Hand Teleoperation System | 2023 · RSS'23 | 仅用相机做手部姿态估计，统一遥操作多种机械臂 + 灵巧手 | [arXiv](https://arxiv.org/abs/2307.04577) |
| **BridgeData V2** · A Dataset for Robot Learning at Scale | 2023 · CoRL'23 | 6 万条轨迹、24 个环境的低成本 WidowX 数据集，学术界常用预训练数据 | [arXiv](https://arxiv.org/abs/2308.12952) |
| **GELLO** · A General, Low-Cost, and Intuitive Teleoperation Framework | 2023 · IROS'24 | 3D 打印 + 舵机做成与机械臂同构的主手，几百美元实现直观遥操作 | [arXiv](https://arxiv.org/abs/2309.13037) |
| ⭐ **MimicGen** · A Data Generation System for Scalable Robot Learning | 2023 · CoRL'23 | 把约 200 条人类示教按物体坐标系切分重组，自动生成 5 万条新示教 | [arXiv](https://arxiv.org/abs/2310.17596) |
| ⭐ **Mobile ALOHA** · Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation | 2024 · CoRL'24 | 低成本全身遥操作移动双臂平台，与静态 ALOHA 数据协同训练完成炒菜等任务 | [arXiv](https://arxiv.org/abs/2401.02117) · [代码](https://github.com/MarkFzp/mobile-aloha) |
| ⭐ **UMI** · Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots | 2024 · RSS'24 | 手持夹爪 + GoPro 在任意场景采集示教，不需要机器人在场，策略可直接迁移到真机 | [arXiv](https://arxiv.org/abs/2402.10329) · [代码](https://github.com/real-stanford/universal_manipulation_interface) |
| **DexCap** · Scalable and Portable Mocap Data Collection System for Dexterous Manipulation | 2024 · RSS'24 | 便携动捕手套 + 相机采集人手数据，用于训练灵巧手策略 | [arXiv](https://arxiv.org/abs/2403.07788) |
| ⭐ **DROID** · A Large-Scale In-The-Wild Robot Manipulation Dataset | 2024 · RSS'24 | 13 家机构、564 个场景、7.6 万条轨迹的真实世界多样化操作数据集 | [arXiv](https://arxiv.org/abs/2403.12945) |
| **Open-TeleVision** · Teleoperation with Immersive Active Visual Feedback | 2024 · CoRL'24 | VR 头显 + 随动立体相机的沉浸式遥操作，可跨地域控制人形机器人 | [arXiv](https://arxiv.org/abs/2407.01512) |
| **ALOHA Unleashed** · A Simple Recipe for Robot Dexterity | 2024 · CoRL'24 | 大规模 ALOHA 数据 + 扩散策略，完成系鞋带、挂衣服等高难双臂任务 | [arXiv](https://arxiv.org/abs/2410.13126) |
| **DexMimicGen** · Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning | 2024 · ICRA'25 | 把 MimicGen 扩展到双臂灵巧手人形，从少量示教生成大规模数据 | [arXiv](https://arxiv.org/abs/2410.24185) |
| ⭐ **AgiBot World** · Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems | 2025 · arXiv | 100+ 台真机、217 个任务、100 万+ 条轨迹的双臂操作数据平台，配套 GO-1 通用策略 | [arXiv](https://arxiv.org/abs/2503.06669) · [代码](https://github.com/OpenDriveLab/AgiBot-World) |
| **EgoHumanoid** · Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration | 2026 · arXiv | 首个用大量第一视角人类示教 + 少量机器人数据协同训练 VLA 的框架，人形在多样真实环境完成移动操作 | [arXiv](https://arxiv.org/abs/2602.10106) |
| **GrandTour** · A Legged Robotics Dataset in the Wild for Multi-Modal Perception and State Estimation | 2026 · arXiv | ANYmal-D + 多模态传感器载荷在野外与室内采集的足式机器人数据集，用于感知与状态估计评测 | [arXiv](https://arxiv.org/abs/2602.18164) |
| ⭐ **LeRobot** · An Open-Source Library for End-to-End Robot Learning | 2026 · arXiv | Hugging Face LeRobot 论文：覆盖电机通信、数据采集存储与流式加载、策略训练到部署的端到端开源机器人学习库 | [arXiv](https://arxiv.org/abs/2602.22818) |
| **RoboPocket** · Improve Robot Policies Instantly with Your Phone | 2026 · CoRL'26 | 手机即可做无机器人的策略迭代：AR 实时显示策略预测轨迹并引导纠正式采集，样本效率最高提升 2 倍 | [arXiv](https://arxiv.org/abs/2603.05504) |
| **Kimodo** · Scaling Controllable Human Motion Generation | 2026 · arXiv | 700 小时光学动捕训练的可控人体动作扩散模型，支持文本与关键帧、路径等多种运动学约束，可为人形提供动作数据 | [arXiv](https://arxiv.org/abs/2603.15546) |
| **EgoVerse** · An Egocentric Human Dataset for Robot Learning from Around the World | 2026 · arXiv | 全球协作的第一视角人类示教平台：首批 1362 小时、8 万条、1965 个任务，统一格式与操作相关标注 | [arXiv](https://arxiv.org/abs/2604.07607) |
| **HumanNet** · Scaling Human-centric Video Learning to One Million Hours | 2026 · arXiv | 百万小时级以人为中心的视频语料，实验显示 1000 小时第一视角人类视频的增益超过 100 小时真机数据 | [arXiv](https://arxiv.org/abs/2605.06747) |
| **Open-AoE** · An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning | 2026 · arXiv | 开放的第一视角操作数据集与工具链：从手机采集到跨本体重定向、VLA / WAM / 世界模型训练配方 | [arXiv](https://arxiv.org/abs/2607.14183) |
| **Ego2Robot** · Scalable Robot Data Synthesis from Egocentric Human Data | 2026 · arXiv | 把第一视角人类操作视频转成机器人训练数据（动作重定向 + 机械臂画面合成 + 多级质量筛选），提升分布外泛化 | [arXiv](https://arxiv.org/abs/2608.02580) |

> 📅 **2026 年本方向全部 451 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#16)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
