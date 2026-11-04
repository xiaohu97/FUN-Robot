# 10 · 数据采集、遥操作与大规模数据集

> 数据是具身智能的最大瓶颈。三条路线：**真机遥操作**（ALOHA、GELLO、VR）、**无机器人采集**（UMI、DexCap、人类视频）、**自动数据生成/增广**（MimicGen）。
> 数据集详细字段（规模、模态、许可证）见 [`datasets/README.md`](../datasets/README.md)。

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
| **Open-TeleVision** · Teleoperation with Immersive Active Visual Feedback | 2024 · CoRL'24 | VR 头显 + 随动立体相机的沉浸式遥操作，可跨地域控制人形机器人 | [arXiv](https://arxiv.org/abs/2407.01465) |
| **ALOHA Unleashed** · A Simple Recipe for Robot Dexterity | 2024 · CoRL'24 | 大规模 ALOHA 数据 + 扩散策略，完成系鞋带、挂衣服等高难双臂任务 | [arXiv](https://arxiv.org/abs/2410.13126) |
| **DexMimicGen** · Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning | 2024 · ICRA'25 | 把 MimicGen 扩展到双臂灵巧手人形，从少量示教生成大规模数据 | [arXiv](https://arxiv.org/abs/2410.24185) |
| ⭐ **AgiBot World** · Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems | 2025 · arXiv | 100+ 台真机、217 个任务、100 万+ 条轨迹的双臂操作数据平台，配套 GO-1 通用策略 | [arXiv](https://arxiv.org/abs/2503.06669) · [代码](https://github.com/OpenDriveLab/AgiBot-World) |
