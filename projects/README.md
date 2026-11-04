# 🛠 开源项目

> 能跑起来的代码比论文更重要。按用途分类，上手难度：🟢 低 / 🟡 中 / 🔴 高。
> 新增条目格式见 [`templates/project-entry.md`](../templates/project-entry.md)。

## 训练框架与通用策略

| 项目 | 类型 | 能做什么 | 标签 | 上手 |
|---|---|---|---|---|
| [LeRobot](https://github.com/huggingface/lerobot) | 训练框架 | Hugging Face 的“数据集 → 策略（ACT / Diffusion / π0 / SmolVLA）→ 真机部署”全链路，支持低成本机械臂 | `imitation-learning` `VLA` `open-source` | 🟢 |
| [openpi](https://github.com/Physical-Intelligence/openpi) | 策略模型 | Physical Intelligence 开源的 π0 / π0-FAST / π0.5 权重与微调代码 | `VLA` `open-weights` | 🟡 |
| [Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) | 策略模型 | NVIDIA GR00T 人形基础模型权重、微调与推理脚本 | `VLA` `humanoid` `open-weights` | 🟡 |
| [OpenVLA](https://github.com/openvla/openvla) | 策略模型 | 7B 开源 VLA 的训练、LoRA 微调与部署 | `VLA` `open-weights` | 🟡 |
| [Octo](https://github.com/octo-models/octo) | 策略模型 | 轻量通用 Transformer 策略，适合作为跨本体微调基线 | `VLA` `cross-embodiment` | 🟢 |
| [diffusion_policy](https://github.com/real-stanford/diffusion_policy) | 算法实现 | Diffusion Policy 官方实现，仿真与真机配置齐全 | `diffusion` `imitation-learning` | 🟢 |
| [robomimic](https://github.com/ARISE-Initiative/robomimic) | 学习框架 | 离线示教学习的算法库与基准（BC、BC-RNN 等） | `imitation-learning` | 🟢 |

## 仿真器与训练环境

| 项目 | 类型 | 能做什么 | 标签 | 上手 |
|---|---|---|---|---|
| [MuJoCo](https://github.com/google-deepmind/mujoco) | 物理引擎 | 高效接触仿真，RL 与控制研究最常用的引擎之一；MJX 支持 GPU | `sim` `RL` | 🟢 |
| [MuJoCo Playground](https://github.com/google-deepmind/mujoco_playground) | 训练环境 | 基于 MJX 的四足/人形/灵巧手 GPU 训练环境，含 sim2real 配置 | `sim2real` `locomotion` | 🟢 |
| [Isaac Lab](https://github.com/isaac-sim/IsaacLab) | 仿真 + 训练 | NVIDIA 机器人学习框架（Isaac Gym 继任者），大规模并行 RL、模仿学习、传感器仿真 | `sim` `sim2real` `RL` | 🟡 |
| [IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs) | 任务环境 | Isaac Gym 时代的经典并行 RL 任务集合（已停止维护，建议迁移到 Isaac Lab） | `RL` `sim` | 🟡 |
| [Genesis](https://github.com/Genesis-Embodied-AI/Genesis) | 物理仿真 | Python 原生的通用物理仿真平台，强调速度与易用性 | `sim` | 🟢 |
| [ManiSkill](https://github.com/haosulab/ManiSkill) | 仿真 + 基准 | GPU 并行的操作/移动操作仿真与基准 | `manipulation` `benchmark` | 🟢 |
| [RLBench](https://github.com/stepjam/RLBench) | 基准 | 100 个操作任务，3D 操作策略标准评测 | `manipulation` `benchmark` | 🟡 |
| [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO) | 基准 | VLA 微调最常用的仿真评测 | `benchmark` `VLA` | 🟢 |
| [Habitat-Lab](https://github.com/facebookresearch/habitat-lab) | 具身仿真 | 导航、重排、人机协作等具身任务 | `navigation` `sim` | 🟡 |
| [OmniGibson](https://github.com/StanfordVL/OmniGibson) | 交互仿真 | BEHAVIOR-1K 所用的高真实感家庭场景仿真 | `household` `sim` | 🔴 |

## 足式与人形运动控制

| 项目 | 类型 | 能做什么 | 标签 | 上手 |
|---|---|---|---|---|
| [legged_gym](https://github.com/leggedrobotics/legged_gym) | 训练框架 | 四足/双足 RL 运动控制经典代码，很多人形项目的起点 | `locomotion` `sim2real` | 🟢 |
| [rsl_rl](https://github.com/leggedrobotics/rsl_rl) | RL 库 | 面向 GPU 并行仿真的轻量 PPO 实现，legged_gym / Isaac Lab 默认使用 | `RL` | 🟢 |
| [humanoid-gym](https://github.com/roboterax/humanoid-gym) | 训练框架 | 人形 RL 训练 + MuJoCo sim2sim 验证 | `humanoid` `locomotion` | 🟢 |
| [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym) | 训练框架 | 宇树 G1/H1/Go2 的官方 RL 训练与部署示例 | `humanoid` `quadruped` `sim2real` | 🟢 |
| [ASAP](https://github.com/LeCAR-Lab/ASAP) | 算法实现 | 人形敏捷全身技能 + sim-real 动力学对齐 | `humanoid` `whole-body-control` | 🟡 |
| [PHC](https://github.com/ZhengyiLuo/PHC) | 算法实现 | 大规模人体动作跟踪控制器，人形动作重定向常用工具链 | `motion-tracking` | 🟡 |

## 机器人系统与底层库

| 项目 | 类型 | 能做什么 | 标签 | 上手 |
|---|---|---|---|---|
| [ROS 2](https://github.com/ros2/ros2) | 中间件 | 机器人系统工程的事实标准：通信、节点管理、生态插件 | `middleware` | 🟡 |
| [MoveIt 2](https://github.com/moveit/moveit2) | 运动规划 | 机械臂运动规划、碰撞检测、逆运动学 | `planning` `manipulation` | 🟡 |
| [Pinocchio](https://github.com/stack-of-tasks/pinocchio) | 动力学库 | 高性能刚体动力学，适合全身控制、MPC | `dynamics` `control` | 🟡 |
| [Drake](https://github.com/RobotLocomotion/drake) | 建模与优化 | 多体动力学建模、轨迹优化、仿真验证 | `optimization` `control` | 🔴 |
| [Unitree SDK2](https://github.com/unitreerobotics/unitree_sdk2) | 硬件 SDK | 宇树机器人底层控制接口，实机部署必备 | `hardware` `real-world` | 🟡 |
| [OpenRAVE / IKFast](http://openrave.org/) | 规划工具 | 经典规划框架，IKFast 解析逆运动学求解仍很常用 | `planning` `IK` | 🔴 |

## 数据集工具

| 项目 | 类型 | 能做什么 | 标签 | 上手 |
|---|---|---|---|---|
| [Open X-Embodiment](https://github.com/google-deepmind/open_x_embodiment) | 数据集 | 跨本体机器人数据集与 RT-X 模型 | `dataset` `cross-embodiment` | 🟡 |
| [UMI](https://github.com/real-stanford/universal_manipulation_interface) | 采集系统 | 手持夹爪数据采集 + 策略训练全流程 | `teleoperation` `dataset` | 🟡 |
| [Mobile ALOHA](https://github.com/MarkFzp/mobile-aloha) | 采集系统 | 低成本移动双臂遥操作硬件与训练代码 | `teleoperation` `bimanual` | 🔴 |
