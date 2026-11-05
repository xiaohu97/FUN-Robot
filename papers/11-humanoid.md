# 11 · 人形机器人（运动、全身控制、移动操作与遥操作）

> 人形机器人的核心难题：高自由度、欠驱动、需要同时“走 + 干活”。主流路线是 **“人类动作数据 → 重定向 → 仿真 RL 跟踪 → sim2real”**，2026 年快速走向**人形移动操作（loco-manipulation）**与大规模动作预训练。
> 主线：**DeepMimic / AMP → PHC → H2O / HumanPlus（全身遥操作）→ HOVER / ASAP → BeyondMimic / GMT（通用跟踪）→ 2026：Humanoid-GPT（十亿级动作预训练）、Ψ0 / X-WBC（基础模型）、HumanX / HuMI（从人类视频与无机器人示教学交互）**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **DeepMimic** · Example-Guided Deep RL of Physics-Based Character Skills | 2018 · SIGGRAPH'18 | 以跟踪参考动作为奖励的 RL，物理角色学会翻跟头、武术等技能；“动作模仿”范式之源 | [arXiv](https://arxiv.org/abs/1804.02717) |
| ⭐ **AMP** · Adversarial Motion Priors for Stylized Physics-Based Character Control | 2021 · SIGGRAPH'21 | 用对抗判别器学习动作风格先验，无需逐帧跟踪也能产生自然动作 | [arXiv](https://arxiv.org/abs/2104.02180) |
| **ASE** · Large-Scale Reusable Adversarial Skill Embeddings | 2022 · SIGGRAPH'22 | 从大量动作数据中学习可复用的潜在技能空间，上层任务只需在潜空间中控制 | [arXiv](https://arxiv.org/abs/2205.01906) |
| ⭐ **Real-World Humanoid Locomotion** · Real-World Humanoid Locomotion with Reinforcement Learning | 2023 · Science Robotics | 因果 Transformer 策略在仿真中大规模训练，零样本部署到 Digit 户外行走 | [arXiv](https://arxiv.org/abs/2303.03381) |
| ⭐ **PHC** · Perpetual Humanoid Control for Real-time Simulated Avatars | 2023 · ICCV'23 | 渐进式乘法控制策略跟踪整个 AMASS 动作库，可从摔倒中自动恢复，后续人形跟踪工作的基础 | [arXiv](https://arxiv.org/abs/2305.06456) · [代码](https://github.com/ZhengyiLuo/PHC) |

## 🚀 最新进展（2024 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **ExBody** · Expressive Whole-Body Control for Humanoid Robots | 2024 · RSS'24 | 上半身模仿人类动作、下半身稳健跟踪速度指令，实现富表现力全身动作 | [arXiv](https://arxiv.org/abs/2402.16796) |
| **Humanoid Locomotion as Next Token Prediction** | 2024 · NeurIPS'24 | 把运动控制当作传感器-动作序列的自回归预测，可利用无动作的视频数据 | [arXiv](https://arxiv.org/abs/2402.19469) |
| **H2O** · Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation | 2024 · IROS'24 | sim-to-data 过滤不可行动作 + RL 跟踪，RGB 相机实时全身遥操作 | [arXiv](https://arxiv.org/abs/2403.04436) |
| **Humanoid-Gym** · RL for Humanoid Robot with Zero-Shot Sim2Real Transfer | 2024 · arXiv | 开源人形 RL 训练框架，带 Isaac Gym → MuJoCo 的 sim2sim 验证流程 | [arXiv](https://arxiv.org/abs/2404.05695) · [代码](https://github.com/roboterax/humanoid-gym) |
| **OmniH2O** · Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning | 2024 · CoRL'24 | 统一运动学接口支持 VR / RGB / 语言等多种遥操作方式，并发布人形全身数据集 | [arXiv](https://arxiv.org/abs/2406.08858) |
| ⭐ **HumanPlus** · Humanoid Shadowing and Imitation from Humans | 2024 · CoRL'24 | 单 RGB 相机实时“影子”遥操作采集数据，再模仿学习自主技能（叠衣、打字等） | [arXiv](https://arxiv.org/abs/2406.10454) |
| **iDP3** · Generalizable Humanoid Manipulation with 3D Diffusion Policies | 2024 · arXiv | 自我中心 3D 表征的改进版 DP3，单一场景数据即可泛化到多场景人形操作 | [arXiv](https://arxiv.org/abs/2410.10803) |
| ⭐ **HOVER** · Versatile Neural Whole-Body Controller for Humanoid Robots | 2024 · ICRA'25 | 多模式指令空间（关节/根节点/关键点）统一为一个控制器，由 oracle 策略蒸馏 | [arXiv](https://arxiv.org/abs/2410.21229) |
| **ExBody2** · Advanced Expressive Humanoid Whole-Body Control | 2024 · arXiv | 动作数据可行性筛选 + 教师-学生蒸馏，提升高动态全身动作的跟踪精度 | [arXiv](https://arxiv.org/abs/2412.13196) |
| ⭐ **ASAP** · Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills | 2025 · RSS'25 | 用真机数据训练 delta action 模型补偿 sim-real 动力学差异，实现跳投、后仰等敏捷技能 | [arXiv](https://arxiv.org/abs/2502.01143) · [代码](https://github.com/LeCAR-Lab/ASAP) |
| **HugWBC** · A Unified and General Humanoid Whole-Body Controller | 2025 · RSS'25 | 单一策略支持走、跑、跳、单脚跳等步态及步频/抬脚高度等精细参数调节 | [arXiv](https://arxiv.org/abs/2502.03206) |
| **HoST** · Learning Humanoid Standing-up Control across Diverse Postures | 2025 · RSS'25 | 多 critic + 地形课程 RL，从各种倒地姿态起身，直接部署到 Unitree G1 | [arXiv](https://arxiv.org/abs/2502.08378) · [代码](https://github.com/OpenRobotLab/HoST) |
| **TWIST** · Teleoperated Whole-Body Imitation System | 2025 · CoRL'25 | RL + BC 训练的单一全身控制器，动捕实时遥操作完成全身操作与舞蹈 | [arXiv](https://arxiv.org/abs/2505.02833) |
| **KungfuBot** · Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills | 2025 · NeurIPS'25 | 视频动作提取 + 物理过滤 + 自适应跟踪容差，G1 完成功夫、舞蹈等高动态动作 | [arXiv](https://arxiv.org/abs/2506.12851) |
| **GMT** · General Motion Tracking for Humanoid Whole-Body Control | 2025 · arXiv | 自适应采样 + 动作混合专家（MoE），单一策略跟踪大规模动捕数据 | [arXiv](https://arxiv.org/abs/2506.14770) · [代码](https://github.com/zixuan417/humanoid-general-motion-tracking) |
| ⭐ **BeyondMimic** · From Motion Tracking to Versatile Humanoid Control via Guided Diffusion | 2025 · arXiv | 高动态动作跟踪（侧手翻、旋转跳）+ 蒸馏为可引导扩散策略，测试时用代价函数完成导航、避障等任务 | [arXiv](https://arxiv.org/abs/2508.08241) |
| **OmniRetarget** · Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation | 2025 · arXiv | 用交互网格保持人-物-地形关系的重定向，一条示教生成大量可行变体，支撑 30 秒长程技能 | [arXiv](https://arxiv.org/abs/2509.26633) |
| **WholeBodyVLA** · Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control | 2025 · arXiv | 统一潜在动作的 VLA，把移动与操作放进同一人形全身策略 | [arXiv](https://arxiv.org/abs/2512.11047) |
| **Deep Whole-body Parkour** | 2026 · arXiv | 把外感知融入全身动作跟踪，人形在不平地形上完成高动态非行走类动作 | [arXiv](https://arxiv.org/abs/2601.07701) |
| **Hiking in the Wild** · A Scalable Perceptive Parkour Framework for Humanoids | 2026 · arXiv | 端到端感知跑酷框架：深度 + 本体感知直接映射动作，配合落脚安全机制，人形在复杂野外地形以 2.5 m/s 行进 | [arXiv](https://arxiv.org/abs/2601.07718) |
| **TTT-Parkour** · Rapid Test-Time Training for Perceptive Robot Parkour | 2026 · arXiv | 测试时快速训练，让人形在预训练未见过的复杂地形上完成感知跑酷 | [arXiv](https://arxiv.org/abs/2602.02331) |
| **HumanX** · Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos | 2026 · arXiv | XGen（从单目视频生成物理可行的交互数据）+ XMimic（交互优先的模仿学习），无需逐任务设计即可从人类视频学到交互技能 | [arXiv](https://arxiv.org/abs/2602.02473) |
| **HuMI** · Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations | 2026 · arXiv | 便携式无机器人全身动作采集 + 分层学习，人形学会跪、蹲、抛掷、双臂操作等全身操作任务 | [arXiv](https://arxiv.org/abs/2602.06643) |
| **TextOp** · Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control | 2026 · arXiv | 实时文本驱动的人形动作生成与控制，执行中可流式修改语言指令并平滑切换动作 | [arXiv](https://arxiv.org/abs/2602.07439) |
| **Perceptive Humanoid Parkour** · Chaining Dynamic Human Skills via Motion Matching | 2026 · arXiv | 动作匹配串联重定向后的人类高动态技能，结合视觉感知自主完成长程人形跑酷 | [arXiv](https://arxiv.org/abs/2602.15827) |
| **Iterative Closed-Loop Motion Synthesis** · for Scaling the Capabilities of Humanoid Control | 2026 · arXiv | “训练 → 评估 → 再合成动作数据”闭环，持续扩展人形控制能力 | [arXiv](https://arxiv.org/abs/2602.21599) |
| **LessMimic** · Long-Horizon Humanoid Interaction with Unified Distance Field Representations | 2026 · arXiv | 统一距离场表示人-物交互，提升长时程、多接触交互的泛化 | [arXiv](https://arxiv.org/abs/2602.21723) |
| **Humanizing Robot Gaze Shifts** · A Framework for Natural Gaze Shifts in Humanoid Robots | 2026 · arXiv | 让人形机器人的注视转移更接近人类，面向导览、陪护等社交场景 | [arXiv](https://arxiv.org/abs/2602.21983) |
| **OmniXtreme** · Breaking the Generality Barrier in High-Dynamic Humanoid Control | 2026 · arXiv | 把通用运动技能学习（大容量 flow matching 策略）与执行器感知的 sim2real 精调解耦，突破高动态人形控制的通用性瓶颈 | [arXiv](https://arxiv.org/abs/2602.23843) |
| **Ψ0** · An Open Foundation Model Towards Universal Humanoid Loco-Manipulation | 2026 · arXiv | 开源人形移动操作基础模型：先用高质量第一视角人类操作数据预训练，再用真机人形轨迹后训练，优于混合噪声数据训练 | [arXiv](https://arxiv.org/abs/2603.12263) |
| **UniT** · Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling | 2026 · arXiv | 以视觉锚定的统一潜在动作 tokenizer 作为人与人形之间的“物理语言”，同时服务策略学习（VLA-UniT）与世界建模 | [arXiv](https://arxiv.org/abs/2604.19734) |
| **Humanoid-GPT** · Scaling Data and Structure for Zero-Shot Motion Tracking | 2026 · CVPR'26 | 在十亿级动作语料上训练 GPT 式因果 Transformer 做全身动作跟踪，零样本泛化到未见动作与控制任务 | [arXiv](https://arxiv.org/abs/2606.03985) |
| **Perceptive Behavior Foundation Model** · Adapting Human Motion Priors to Robot-Centric Terrain | 2026 · arXiv | 让以动作为中心的行为基础模型感知地形，解决参考动作与环境不匹配的问题 | [arXiv](https://arxiv.org/abs/2606.08059) |
| **X-WBC** · A Cross-Embodiment Foundation Model for Humanoid Whole-Body Control | 2026 · CoRL'26 | 因果 Transformer 从多机器人混合数据中学习可复用的运动结构，一个模型控制多种人形 | [arXiv](https://arxiv.org/abs/2609.15213) |
| **InterEvolve** · Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation | 2026 · arXiv | 测试时进化奖励程序，复用冻结的物体感知行为基础模型完成从未训练过的人形移动操作任务 | [arXiv](https://arxiv.org/abs/2610.02196) |
| **Reflex** · Visually Grounded Reactive Humanoid Control | 2026 · arXiv | 三阶段学习视觉驱动的反应式人形控制，仅凭第一视角 RGB-D 接住抛来的箱子（仿真成功率 85.7%） | [arXiv](https://arxiv.org/abs/2610.12772) |

## 🔗 相关

> 人形 VLA（GR00T 等）见 [`01`](./01-vla-foundation-models.md)；行为基础模型综述见 [`18`](./18-surveys.md)。

> 📅 **2026 年本方向全部 626 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#11)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
