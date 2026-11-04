# 📦 数据集

> 只收录**公开可下载**的数据集。规模数字以论文/官网发布时为准，注明来源便于后续核对。
> 新增条目：复制表格行 `| [名称](链接) | 本体 | 模态 | 规模 | 论文 | 备注 |`。

## 机器人操作（真机轨迹）

| 数据集 | 本体 | 模态 | 规模（发布时） | 论文 | 备注 |
|---|---|---|---|---|---|
| [Open X-Embodiment](https://robotics-transformer-x.github.io/) | 22 种机器人 | RGB、语言、动作 | 100 万+ 条轨迹，60 个子数据集 | [arXiv](https://arxiv.org/abs/2310.08864) | RLDS 格式，VLA 预训练标配 |
| [DROID](https://droid-dataset.github.io/) | Franka | 多视角 RGB、深度、语言 | 7.6 万条轨迹，564 个场景 | [arXiv](https://arxiv.org/abs/2403.12945) | 场景多样性高 |
| [BridgeData V2](https://rail-berkeley.github.io/bridgedata/) | WidowX | RGB、语言 | 6 万条轨迹，24 个环境 | [arXiv](https://arxiv.org/abs/2308.12952) | 学术界最常用的低成本数据 |
| [AgiBot World](https://agibot-world.com/) | 双臂人形（AgiBot G1） | 多视角 RGB、深度、语言等 | 100 万+ 条轨迹，217 个任务 | [arXiv](https://arxiv.org/abs/2503.06669) | 含 5 类部署场景 |
| [RoboNet](https://www.robonet.wiki/) | 7 种机械臂 | RGB、动作 | 1500 万帧 | [arXiv](https://arxiv.org/abs/1910.11215) | 早期跨本体数据集 |
| [LeRobot Hub](https://huggingface.co/lerobot) | 多种（含 ALOHA、SO-100 等） | RGB、动作 | 社区持续增长 | — | LeRobot 统一格式，可直接训练 |

## 人类动作与第一视角视频

| 数据集 | 内容 | 规模（发布时） | 论文 | 备注 |
|---|---|---|---|---|
| [AMASS](https://amass.is.tue.mpg.de/) | 统一为 SMPL 格式的人体动捕合集 | 40+ 小时，300+ 人 | [arXiv](https://arxiv.org/abs/1904.03278) | 人形动作跟踪（PHC、OmniH2O 等）的主要来源 |
| [Ego4D](https://ego4d-data.org/) | 第一视角日常视频 | 3670 小时 | [arXiv](https://arxiv.org/abs/2110.07058) | R3M 等视觉表征预训练 |

## 抓取与灵巧手

| 数据集 | 内容 | 规模（发布时） | 论文 | 备注 |
|---|---|---|---|---|
| [DexGraspNet](https://pku-epic.github.io/DexGraspNet/) | 灵巧手抓取姿态（仿真生成） | 132 万抓取，5355 个物体 | [arXiv](https://arxiv.org/abs/2210.02697) | ShadowHand |
| [GraspNet-1Billion](https://graspnet.net/) | 平行夹爪 6-DoF 抓取标注 | 10 亿抓取位姿，190 个场景 | CVPR 2020 | AnyGrasp 基于此 |

## 导航与场景

| 数据集 | 内容 | 规模（发布时） | 论文 | 备注 |
|---|---|---|---|---|
| [R2R](https://bringmeaspoon.org/) | 视觉语言导航指令 | 2.1 万条指令，90 栋建筑 | [arXiv](https://arxiv.org/abs/1711.07280) | Matterport3D 场景 |
| [HM3D](https://aihabitat.org/datasets/hm3d/) | 3D 室内场景扫描 | 1000 个场景 | [arXiv](https://arxiv.org/abs/2109.08238) | Habitat ObjectNav 主力场景 |

## 待补方向
- [ ] 触觉数据集
- [ ] 人形全身遥操作数据（OmniH2O、TWIST 等发布的数据）
- [ ] 产业场景数据（仓储、零售、物流）
