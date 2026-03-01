# 开源项目可读版（20条）

> 字段：类型｜中文解读（2-3行）｜应用标签｜链接

### 1. LeRobot
- 类型：数据与训练框架
- 解读：Hugging Face 推的机器人训练工具链，强调“数据集-策略-部署”闭环。对快速搭建实验流水线很友好。
- 应用标签：`training` `imitation` `warehouse` `retail`
- 链接：https://github.com/huggingface/lerobot

### 2. OpenPI
- 类型：通用机器人策略
- 解读：面向通用控制策略研究的开源项目，适合作为基线与二次开发入口。
- 应用标签：`foundation-policy` `generalist`
- 链接：https://github.com/Physical-Intelligence/openpi

### 3. IsaacLab
- 类型：仿真与训练
- 解读：NVIDIA 新一代机器人研发栈，和 Isaac Sim / Omniverse 生态深度绑定，产业落地友好。
- 应用标签：`sim` `sim2real` `factory` `warehouse`
- 链接：https://github.com/isaac-sim/IsaacLab

### 4. IsaacGymEnvs
- 类型：任务环境库
- 解读：大规模并行仿真训练常用环境集合，适合做强化学习高吞吐训练。
- 应用标签：`RL` `sim` `benchmark`
- 链接：https://github.com/NVIDIA-Omniverse/IsaacGymEnvs

### 5. legged_gym
- 类型：运动控制训练
- 解读：四足/双足运动控制经典开源库，很多人形步态方案可借鉴其训练范式。
- 应用标签：`locomotion` `sim2real`
- 链接：https://github.com/leggedrobotics/legged_gym

### 6. humanoid-gym
- 类型：人形运动训练
- 解读：聚焦人形机器人运动与平衡控制，适合做步态与全身控制入门。
- 应用标签：`humanoid` `locomotion`
- 链接：https://github.com/roboterax/humanoid-gym

### 7. Unitree SDK2
- 类型：硬件 SDK
- 解读：宇树机器人官方控制接口，做实机部署时几乎必用。稳定性和接口文档很关键。
- 应用标签：`hardware` `deployment` `real-world`
- 链接：https://github.com/unitreerobotics/unitree_sdk2

### 8. Unitree 官方示例集合
- 类型：策略示例/工具
- 解读：包含不同机器人型号的示例代码，适合快速打通“跑起来”的第一步。
- 应用标签：`quickstart` `real-robot`
- 链接：https://github.com/unitreerobotics

### 9. ROS 2
- 类型：机器人中间件
- 解读：机器人系统工程事实标准，设备通信、节点管理、生态插件都很成熟。
- 应用标签：`middleware` `integration` `all-scenarios`
- 链接：https://github.com/ros2/ros2

### 10. MoveIt 2
- 类型：运动规划
- 解读：机械臂/全身路径规划核心工具链，工业与科研都广泛使用。
- 应用标签：`planning` `manipulation` `factory`
- 链接：https://github.com/moveit/moveit2

### 11. Pinocchio
- 类型：动力学库
- 解读：高性能刚体动力学计算库，适合全身控制、模型预测控制等底层算法。
- 应用标签：`dynamics` `control`
- 链接：https://github.com/stack-of-tasks/pinocchio

### 12. Drake
- 类型：控制与规划平台
- 解读：偏学术与高可靠工程路线，适合复杂系统建模、优化控制、仿真验证。
- 应用标签：`control` `optimization` `simulation`
- 链接：https://github.com/RobotLocomotion/drake

### 13. MuJoCo
- 类型：物理引擎
- 解读：强化学习和控制领域最常用物理引擎之一，速度快、生态广。
- 应用标签：`physics` `RL` `sim`
- 链接：https://github.com/google-deepmind/mujoco

### 14. ManiSkill
- 类型：操作仿真基准
- 解读：聚焦操作任务的高质量仿真与评测，适合抓取、装配等场景基线对比。
- 应用标签：`manipulation` `benchmark` `warehouse`
- 链接：https://github.com/haosulab/ManiSkill

### 15. RLBench
- 类型：操作任务基准
- 解读：经典多任务操作 benchmark，适合评估泛化与样本效率。
- 应用标签：`benchmark` `multi-task` `manipulation`
- 链接：https://github.com/stepjam/RLBench

### 16. Open X-Embodiment
- 类型：数据生态
- 解读：Google 生态下的大规模具身数据方向，常用于训练通用策略模型。
- 应用标签：`dataset` `foundation-policy`
- 链接：https://robotics-transformer-x.github.io/

### 17. Habitat-Lab
- 类型：具身仿真平台
- 解读：偏导航、交互和具身任务研究，适合做多模态智能体评估。
- 应用标签：`embodied-ai` `navigation` `simulation`
- 链接：https://github.com/facebookresearch/habitat-lab

### 18. OmniGibson
- 类型：交互式仿真
- 解读：强调真实感交互场景，适合做家庭/服务场景中的复杂任务模拟。
- 应用标签：`service-robot` `home` `simulation`
- 链接：https://github.com/StanfordVL/OmniGibson

### 19. RoboMimic
- 类型：模仿学习工具链
- 解读：IL 训练与评测管线清晰，适合从示教数据快速训练可运行策略。
- 应用标签：`imitation-learning` `manipulation`
- 链接：https://github.com/ARISE-Initiative/robomimic

### 20. OpenRAVE / IKFast
- 类型：规划与逆解工具
- 解读：经典机器人规划工具链，IKFast 在高性能逆运动学求解上仍很实用。
- 应用标签：`planning` `IK` `industrial`
- 链接：http://openrave.org/
