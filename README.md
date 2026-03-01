<center>
  <h1>🤖 FUN-Robot</h1>
  <p>人形机器人论文与开源项目导航（Humanoid Robot Paper & Open-Source Collection）</p>
  <p>
    <a href="./humanoid-awesome/papers/papers.md">📚 论文可读版（30条）</a> ·
    <a href="./humanoid-awesome/projects/projects.md">🛠 开源项目可读版（20条）</a> ·
    <a href="./humanoid-awesome/taxonomy.md">🧭 分类目录</a>
  </p>
</center>

---

## 项目定位
参考 [funNLP](https://github.com/fighting41love/funNLP) 的组织方式，做一个**分类清晰、持续更新、中文友好**的人形机器人资料库。

适合人群：
- 想快速入门人形机器人方向的同学
- 想找可复现开源项目的开发者
- 想做产业研究（批发/零售/仓储/快递/运输）的分析者

---

## 目录（Table of Contents）

| 模块 | 内容 | 链接 |
|---|---|---|
| 分类目录 | 全局知识结构与方向树 | [taxonomy.md](./humanoid-awesome/taxonomy.md) |
| 论文合集 | 30条论文可读版（每条2~3行中文解读+标签） | [papers.md](./humanoid-awesome/papers/papers.md) |
| 2026 Jan-Feb arXiv专题 | humanoid关键词检索，逐篇简介+链接+方向分类（109篇） | [arxiv-2026-01-02-humanoid.md](./humanoid-awesome/papers/arxiv-2026-01-02-humanoid.md) |
| 项目合集 | 20条开源项目可读版（解读+应用标签） | [projects.md](./humanoid-awesome/projects/projects.md) |
| 数据集 | 数据集收录模板（待扩展） | [datasets/README.md](./humanoid-awesome/datasets/README.md) |
| Benchmark | 基准收录模板（待扩展） | [benchmarks/README.md](./humanoid-awesome/benchmarks/README.md) |
| 条目模板 | 论文/项目统一模板 | [entry-template.md](./humanoid-awesome/templates/entry-template.md) |

---

## 当前收录

✅ 论文：30 条（可读版）  
✅ 开源项目：20 条（可读版）  
✅ 总计：50 条初版骨架已升级为可读版

重点覆盖方向：
- 运动控制与全身控制
- 灵巧操作与双臂协作
- VLA（视觉-语言-动作）
- 数据与仿真（Sim2Real）
- 人机交互（HRI）
- 产业应用（零售/仓储/物流等）

---

## 📌 2026年1-2月 arXiv humanoid 统计（新增）

- 检索口径：`all:humanoid OR all:"humanoid robot"`
- 时间范围：2026-01-01 ~ 2026-02-28
- 总篇数：**109篇**（**1月 40篇**，**2月 69篇**）
- 已完成：按研究方向分类，并为每篇给出简短介绍 + 论文链接
- 详单入口：[`humanoid-awesome/papers/arxiv-2026-01-02-humanoid.md`](./humanoid-awesome/papers/arxiv-2026-01-02-humanoid.md)

---

## 🔥 精选条目预览区

### 精选论文（建议先看）

| 论文 | 方向 | 为什么值得看 |
|---|---|---|
| [EmbodMocap](https://arxiv.org/abs/2602.23205) | 数据与4D重建 | 低成本真实场景数据采集，对具身训练数据基础设施价值高 |
| [LessMimic](https://arxiv.org/abs/2602.21723) | 长时任务控制 | 聚焦人形长时交互与多任务泛化，贴近真实落地需求 |
| [Humanizing Robot Gaze Shifts](https://arxiv.org/abs/2602.21983) | 人机交互 | 解决社交交互自然度问题，直接影响服务场景体验 |
| [RT-2](https://arxiv.org/abs/2307.15818) | VLA | 视觉语言能力与机器人动作融合的代表性工作 |
| [AMP](https://arxiv.org/abs/2104.02180) | 人形运动控制 | 人形动作自然化与稳定性提升的经典路线 |

### 精选开源项目（建议先跑）

| 项目 | 类型 | 适合做什么 |
|---|---|---|
| [LeRobot](https://github.com/huggingface/lerobot) | 训练框架 | 快速搭建“数据→策略→评估”流水线 |
| [IsaacLab](https://github.com/isaac-sim/IsaacLab) | 仿真平台 | 做大规模仿真训练和 sim2real 实验 |
| [humanoid-gym](https://github.com/roboterax/humanoid-gym) | 人形控制 | 人形步态/平衡控制入门与基线 |
| [MoveIt 2](https://github.com/moveit/moveit2) | 运动规划 | 机械臂与全身规划任务落地 |
| [RoboMimic](https://github.com/ARISE-Initiative/robomimic) | 模仿学习 | 基于示教数据训练操作策略 |

---

## 标签体系（示例）

- 任务标签：`locomotion` `manipulation` `whole-body-control` `imitation-learning` `VLA`
- 场景标签：`factory` `warehouse` `retail` `delivery` `service`
- 形态标签：`sim` `sim2real` `real-world`
- 状态标签：`sota` `classic` `reproducible` `todo`

---

## 更新节奏建议

- **每日**：补 3~5 条增量（arXiv / GitHub）
- **每周**：整理 Top 10 值得精读 + 值得复现
- **每月**：产出行业版观察（批发、零售、仓储、快递、运输）

---

## 贡献方式

欢迎 PR / Issue：
- 论文条目建议补充：摘要3行、代码链接、应用价值、是否值得细读
- 项目条目建议补充：活跃度、可复现性、适用行业场景

---

## License

默认遵循仓库 License（如未设置，建议补充 MIT License）。

---

## 🧾 2026年1-2月 arXiv「humanoid」论文整理（全文内嵌）

> 以下内容同步自 `humanoid-awesome/papers/arxiv-2026-01-02-humanoid.md`


- 检索口径：`all:humanoid OR all:"humanoid robot"`
- 时间范围：2026-01-01 ~ 2026-02-28（按 arXiv submittedDate 过滤）
- 总篇数：**109**（1月 **40**，2月 **69**）
- 说明：该清单按关键词检索，可能包含少量“非严格人形”但相关条目。

## 运动控制与步态（54篇）

1. **[Locomotion Beyond Feet](https://arxiv.org/abs/2601.03607v1)**  
   - 日期：2026-01-07  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Most locomotion methods for humanoid robots focus on leg-based gaits, yet natural bipeds frequently rely on hands, knees, and elbows to establish additional contacts for stability 
2. **[SKATER: Synthesized Kinematics for Advanced Traversing Efficiency on a Humanoid Robot via Roller Skate Swizzles](https://arxiv.org/abs/2601.04948v1)**  
   - 日期：2026-01-08  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Although recent years have seen significant progress of humanoid robots in walking and running, the frequent foot strikes with ground during these locomotion gaits inevitably gener
3. **[Hindsight Preference Replay Improves Preference-Conditioned Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2601.11604v1)**  
   - 日期：2026-01-08  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Multi-objective reinforcement learning (MORL) enables agents to optimize vector-valued rewards while respecting user preferences.
4. **[Walk the PLANC: Physics-Guided RL for Agile Humanoid Locomotion on Constrained Footholds](https://arxiv.org/abs/2601.06286v1)**  
   - 日期：2026-01-09  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Bipedal humanoid robots must precisely coordinate balance, timing, and contact decisions when locomoting on constrained footholds such as stepping stones, beams, and planks -- even
5. **[Deep Whole-body Parkour](https://arxiv.org/abs/2601.07701v1)**  
   - 日期：2026-01-12  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Current approaches to humanoid control generally fall into two paradigms: perceptive locomotion, which handles terrain well but is limited to pedal gaits, and general motion tracki
6. **[Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids](https://arxiv.org/abs/2601.07718v1)**  
   - 日期：2026-01-12  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception to proactive perception.
7. **[Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations](https://arxiv.org/abs/2601.09518v1)**  
   - 日期：2026-01-14  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Enabling humanoid robots to physically interact with humans is a critical frontier, but progress is hindered by the scarcity of high-quality Human-Humanoid Interaction (HHoI) data.
8. **[FastStair: Learning to Run Up Stairs with Humanoid Robots](https://arxiv.org/abs/2601.10365v1)**  
   - 日期：2026-01-15  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Running up stairs is effortless for humans but remains extremely challenging for humanoid robots due to the simultaneous requirements of high agility and strict stability.
9. **[FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation](https://arxiv.org/abs/2601.12790v1)**  
   - 日期：2026-01-19  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Robust local navigation in unstructured and dynamic environments remains a significant challenge for humanoid robots, requiring a delicate balance between long-range navigation tar
10. **[FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions](https://arxiv.org/abs/2601.12799v1)**  
   - 日期：2026-01-19  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humanoid robots are capable of performing various actions such as greeting, dancing and even backflipping.
11. **[Collision-Free Humanoid Traversal in Cluttered Indoor Scenes](https://arxiv.org/abs/2601.16035v2)**  
   - 日期：2026-01-22  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：We study the problem of collision-free humanoid traversal in cluttered indoor scenes, such as hurdling over objects scattered on the floor, crouching under low-hanging obstacles, o
12. **[PILOT: A Perceptive Integrated Low-level Controller for Loco-manipulation over Unstructured Scenes](https://arxiv.org/abs/2601.17440v1)**  
   - 日期：2026-01-24  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humanoid robots hold great potential for diverse interactions and daily service tasks within human-centered environments, necessitating controllers that seamlessly integrate precis
13. **[Fauna Sprout: A lightweight, approachable, developer-ready humanoid robot](https://arxiv.org/abs/2601.18963v1)**  
   - 日期：2026-01-26  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Recent advances in learned control, large-scale simulation, and generative models have accelerated progress toward general-purpose robotic controllers, yet the field still lacks pl
14. **[Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control](https://arxiv.org/abs/2601.21363v3)**  
   - 日期：2026-01-29  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel
15. **[Robust and Generalized Humanoid Motion Tracking](https://arxiv.org/abs/2601.23080v1)**  
   - 日期：2026-01-30  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Learning a general humanoid whole-body controller is challenging because practical reference motions can exhibit noise and inconsistencies after being transferred to the robot doma
16. **[ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control](https://arxiv.org/abs/2602.00401v1)**  
   - 日期：2026-01-30  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Achieving robust, human-like whole-body control on humanoid robots for agile, contact-rich behaviors remains a central challenge, demanding heavy per-skill engineering and a brittl
17. **[TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour](https://arxiv.org/abs/2602.02331v1)**  
   - 日期：2026-02-02  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Achieving highly dynamic humanoid parkour on unseen, complex terrains remains a challenge in robotics.
18. **[HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos](https://arxiv.org/abs/2602.02473v1)**  
   - 日期：2026-02-02  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Enabling humanoid robots to perform agile and adaptive interactive tasks has long been a core challenge in robotics.
19. **[Flow Policy Gradients for Robot Control](https://arxiv.org/abs/2602.02481v1)**  
   - 日期：2026-02-02  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Likelihood-based policy gradient methods are the dominant approach for training robot control policies from rewards.
20. **[Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control](https://arxiv.org/abs/2602.02960v1)**  
   - 日期：2026-02-03  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humanoid Whole-Body Controllers trained with reinforcement learning (RL) have recently achieved remarkable performance, yet many target a single robot embodiment.
21. **[RPL: Learning Robust Humanoid Perceptive Locomotion on Challenging Terrains](https://arxiv.org/abs/2602.03002v1)**  
   - 日期：2026-02-03  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humanoid perceptive locomotion has made significant progress and shows great promise, yet achieving robust multi-directional locomotion on complex terrains remains underexplored.
22. **[HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control](https://arxiv.org/abs/2602.03205v1)**  
   - 日期：2026-02-03  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：While current humanoid whole-body control frameworks predominantly rely on the static environment assumptions, addressing tasks characterized by high dynamism and complex interacti
23. **[CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains](https://arxiv.org/abs/2602.03511v1)**  
   - 日期：2026-02-03  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Robust disturbance rejection remains a longstanding challenge in humanoid locomotion, particularly on unstructured terrains where sensing is unreliable and model mismatch is pronou
24. **[EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models](https://arxiv.org/abs/2602.04515v1)**  
   - 日期：2026-02-04  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information
25. **[Learning Soccer Skills for Humanoid Robots: A Progressive Perception-Action Framework](https://arxiv.org/abs/2602.05310v1)**  
   - 日期：2026-02-05  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Soccer presents a significant challenge for humanoid robots, demanding tightly integrated perception-action capabilities for tasks like perception-guided kicking and whole-body bal
26. **[TOLEBI: Learning Fault-Tolerant Bipedal Locomotion via Online Status Estimation and Fallibility Rewards](https://arxiv.org/abs/2602.05596v1)**  
   - 日期：2026-02-05  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：With the growing employment of learning algorithms in robotic applications, research on reinforcement learning for bipedal locomotion has become a central topic for humanoid roboti
27. **[Scalable and General Whole-Body Control for Cross-Humanoid Locomotion](https://arxiv.org/abs/2602.05791v1)**  
   - 日期：2026-02-05  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Learning-based whole-body controllers have become a key driver for humanoid robots, yet most existing approaches require robot-specific training.
28. **[A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion](https://arxiv.org/abs/2602.05855v1)**  
   - 日期：2026-02-05  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Reliable terrain perception is a critical prerequisite for the deployment of humanoid robots in unstructured, human-centric environments.
29. **[InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions](https://arxiv.org/abs/2602.06035v1)**  
   - 日期：2026-02-05  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humans rarely plan whole-body interactions with objects at the level of explicit whole-body movements.
30. **[HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid Loco-Manipulation](https://arxiv.org/abs/2602.06341v1)**  
   - 日期：2026-02-06  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humanoid loco-manipulation requires executing precise manipulation tasks while maintaining dynamic stability amid base motion and impacts.
31. **[Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels](https://arxiv.org/abs/2602.06382v1)**  
   - 日期：2026-02-06  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Achieving robust vision-based humanoid locomotion remains challenging due to two fundamental issues: the sim-to-real gap introduces significant perception noise that degrades perfo
32. **[ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking](https://arxiv.org/abs/2602.06445v1)**  
   - 日期：2026-02-06  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Achieving stable and energy-efficient locomotion is essential for humanoid robots to operate continuously in real-world applications.
33. **[Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](https://arxiv.org/abs/2602.06643v2)**  
   - 日期：2026-02-06  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Current approaches for humanoid whole-body manipulation, primarily relying on teleoperation or visual sim-to-real reinforcement learning, are hindered by hardware logistics and com
34. **[TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control](https://arxiv.org/abs/2602.07439v1)**  
   - 日期：2026-02-07  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Recent advances in humanoid whole-body motion tracking have enabled the execution of diverse and highly coordinated motions on real hardware.
35. **[Learning Human-Like Badminton Skills for Humanoid Robots](https://arxiv.org/abs/2602.08370v1)**  
   - 日期：2026-02-09  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Realizing versatile and human-like performance in high-demand sports like badminton remains a formidable challenge for humanoid robotics.
36. **[MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation](https://arxiv.org/abs/2602.08594v2)**  
   - 日期：2026-02-09  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Generalist humanoid motion trackers have recently achieved strong simulation metrics by scaling data and training, yet often remain brittle on hardware during sustained teleoperati
37. **[TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior](https://arxiv.org/abs/2602.09628v1)**  
   - 日期：2026-02-10  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Real-time whole-body teleoperation is a critical method for humanoid robots to perform complex tasks in unstructured environments.
38. **[APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots](https://arxiv.org/abs/2602.11143v1)**  
   - 日期：2026-02-11  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humanoid locomotion has advanced rapidly with deep reinforcement learning (DRL), enabling robust feet-based traversal over uneven terrain.
39. **[ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control](https://arxiv.org/abs/2602.11321v1)**  
   - 日期：2026-02-11  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Building a low-latency humanoid teleoperation system is essential for collecting diverse reactive and dynamic demonstrations.
40. **[HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model](https://arxiv.org/abs/2602.11758v1)**  
   - 日期：2026-02-12  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humanoid robots show promise for complex whole-body tasks in unstructured environments.
41. **[General Humanoid Whole-Body Control via Pretraining and Fast Adaptation](https://arxiv.org/abs/2602.11929v1)**  
   - 日期：2026-02-12  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Learning a general whole-body controller for humanoid robots remains challenging due to the diversity of motion distributions, the difficulty of fast adaptation, and the need for r
42. **[PMG: Parameterized Motion Generator for Human-like Locomotion Control](https://arxiv.org/abs/2602.12656v2)**  
   - 日期：2026-02-13  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Recent advances in data-driven reinforcement learning and motion tracking have substantially improved humanoid locomotion, yet critical practical challenges remain.
43. **[CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation](https://arxiv.org/abs/2602.15060v2)**  
   - 日期：2026-02-13  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids.
44. **[A Kung Fu Athlete Bot That Can Do It All Day: Highly Dynamic, Balance-Challenging Motion Dataset and Autonomous Fall-Resilient Tracking](https://arxiv.org/abs/2602.13656v1)**  
   - 日期：2026-02-14  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Current humanoid motion tracking systems can execute routine and moderately dynamic behaviors, yet significant gaps remain near hardware performance limits and algorithmic robustne
45. **[Impact-Robust Posture Optimization for Aerial Manipulation](https://arxiv.org/abs/2602.13762v2)**  
   - 日期：2026-02-14  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：We present a novel method for optimizing the posture of kinematically redundant torque-controlled robots to improve robustness during impacts.
46. **[Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement](https://arxiv.org/abs/2602.13850v3)**  
   - 日期：2026-02-14  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：We investigate a skill-based framework for humanoid box rearrangement that enables long-horizon execution by sequencing reusable skills at the task level.
47. **[AdaptManip: Learning Adaptive Whole-Body Object Lifting and Delivery with Online Recurrent State Estimation](https://arxiv.org/abs/2602.14363v1)**  
   - 日期：2026-02-16  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：This paper presents Adaptive Whole-body Loco-Manipulation, AdaptManip, a fully autonomous framework for humanoid robots to perform integrated navigation, object lifting, and delive
48. **[MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction](https://arxiv.org/abs/2602.15733v1)**  
   - 日期：2026-02-17  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humanoid motion control has witnessed significant breakthroughs in recent years, with deep reinforcement learning (RL) emerging as a primary catalyst for achieving complex, human-l
49. **[Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching](https://arxiv.org/abs/2602.15827v1)**  
   - 日期：2026-02-17  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility and adaptivity of highly dynamic human motions remains an open c
50. **[VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety](https://arxiv.org/abs/2602.16511v1)**  
   - 日期：2026-02-18  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Reliable fall recovery is critical for humanoids operating in cluttered environments.
51. **[Habilis-$β$: A Fast-Motion and Long-Lasting On-Device Vision-Language-Action Model](https://arxiv.org/abs/2602.18813v1)**  
   - 日期：2026-02-21  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：We introduce Habilis-$β$, a fast-motion and long-lasting on-device vision-language-action (VLA) model designed for real-world deployment.
52. **[Generalizing from References using a Multi-Task Reference and Goal-Driven RL Framework](https://arxiv.org/abs/2602.20375v1)**  
   - 日期：2026-02-23  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Learning agile humanoid behaviors from human motion offers a powerful route to natural, coordinated control, but existing approaches face a persistent trade-off: reference-tracking
53. **[Biomechanical Comparisons Reveal Divergence of Human and Humanoid Gaits](https://arxiv.org/abs/2602.21666v1)**  
   - 日期：2026-02-25  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：It remains challenging to achieve human-like locomotion in legged robots due to fundamental discrepancies between biological and mechanical structures.
54. **[LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations](https://arxiv.org/abs/2602.21723v1)**  
   - 日期：2026-02-25  
   - 简介：该文聚焦运动控制与步态，核心问题与方法可概括为：Humanoid robots that autonomously interact with physical environments over extended horizons represent a central goal of embodied intelligence.

## 操作与灵巧手（25篇）

1. **[Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot](https://arxiv.org/abs/2601.02078v1)**  
   - 日期：2026-01-05  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：The development of robust and generalizable robot learning models is critically contingent upon the availability of large-scale, diverse training data and reliable evaluation bench
2. **[Soft Responsive Materials Enhance Humanoid Safety](https://arxiv.org/abs/2601.02857v1)**  
   - 日期：2026-01-06  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Humanoid robots are envisioned as general-purpose platforms in human-centered environments, yet their deployment is limited by vulnerability to falls and the risks posed by rigid m
3. **[PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation](https://arxiv.org/abs/2601.03782v1)**  
   - 日期：2026-01-07  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Humans anticipate, from a glance and a contemplated action of their bodies, how the 3D world will respond, a capability that is equally vital for robotic manipulation.
4. **[Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation](https://arxiv.org/abs/2601.09031v1)**  
   - 日期：2026-01-13  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Humanoid robot manipulation is a crucial research area for executing diverse human-level tasks, involving high-level semantic reasoning and low-level action generation.
5. **[ProjecTA: A Semi-Humanoid Robotic Teaching Assistant with In-Situ Projection for Guided Tours](https://arxiv.org/abs/2601.11328v2)**  
   - 日期：2026-01-16  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Robotic teaching assistants (TAs) often use body-mounted screens to deliver content.
6. **[HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation](https://arxiv.org/abs/2601.14874v1)**  
   - 日期：2026-01-21  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Humanoid robots must adapt their contact behavior to diverse objects and tasks, yet most controllers rely on fixed, hand-tuned impedance gains and gripper settings.
7. **[Walk through Paintings: Egocentric World Models from Internet Priors](https://arxiv.org/abs/2601.15284v1)**  
   - 日期：2026-01-21  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：What if a video generation model could not only imagine a plausible future, but the correct one, accurately reflecting how the world changes with each action?
8. **[Learning a Unified Latent Space for Cross-Embodiment Robot Control](https://arxiv.org/abs/2601.15419v1)**  
   - 日期：2026-01-21  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：We present a scalable framework for cross-embodiment humanoid robot control by learning a shared latent representation that unifies motion across humans and diverse humanoid platfo
9. **[MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions](https://arxiv.org/abs/2601.17507v1)**  
   - 日期：2026-01-24  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Humanoid robot loco-manipulation remains constrained by the semantic-physical gap.
10. **[Shallow-π: Knowledge Distillation for Flow-based VLAs](https://arxiv.org/abs/2601.20262v1)**  
   - 日期：2026-01-28  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：The growing demand for real-time robotic deployment necessitates fast and on-device inference for vision-language-action (VLA) models.
11. **[RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing](https://arxiv.org/abs/2601.22517v1)**  
   - 日期：2026-01-30  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Achieving human-level competitive intelligence and physical agility in humanoid robots remains a major challenge, particularly in contact-rich and highly dynamic tasks such as boxi
12. **[A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation](https://arxiv.org/abs/2602.01632v1)**  
   - 日期：2026-02-02  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Retargeting human motion to robot poses is a practical approach for teleoperating bimanual humanoid robot arms, but existing methods can be suboptimal and slow, often causing undes
13. **[Act, Sense, Act: Learning Non-Markovian Active Perception Strategies from Large-Scale Egocentric Human Data](https://arxiv.org/abs/2602.04600v1)**  
   - 日期：2026-02-04  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Achieving generalizable manipulation in unconstrained environments requires the robot to proactively resolve information uncertainty, i.e., the capability of active perception.
14. **[A Framework for Combining Optimization-Based and Analytic Inverse Kinematics](https://arxiv.org/abs/2602.05092v1)**  
   - 日期：2026-02-04  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Analytic and optimization methods for solving inverse kinematics (IK) problems have been deeply studied throughout the history of robotics.
15. **[DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization](https://arxiv.org/abs/2602.06827v1)**  
   - 日期：2026-02-06  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：In this paper, we introduce DynaRetarget, a complete pipeline for retargeting human motions to humanoid control policies.
16. **[Humanoid Factors: Design Principles for AI Humanoids in Human Worlds](https://arxiv.org/abs/2602.10069v1)**  
   - 日期：2026-02-10  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Human factors research has long focused on optimizing environments, tools, and systems to account for human performance.
17. **[EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106v1)**  
   - 日期：2026-02-10  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Human demonstrations offer rich environmental diversity and scale naturally, making them an appealing alternative to robot teleoperation.
18. **[MotionWeaver: Holistic 4D-Anchored Framework for Multi-Humanoid Image Animation](https://arxiv.org/abs/2602.13326v1)**  
   - 日期：2026-02-11  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Character image animation, which synthesizes videos of reference characters driven by pose sequences, has advanced rapidly but remains largely limited to single-human settings.
19. **[Towards Learning a Generalizable 3D Scene Representation from 2D Observations](https://arxiv.org/abs/2602.10943v1)**  
   - 日期：2026-02-11  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：We introduce a Generalizable Neural Radiance Field approach for predicting 3D workspace occupancy from egocentric robot observations.
20. **[Adding internal audio sensing to internal vision enables human-like in-hand fabric recognition with soft robotic fingertips](https://arxiv.org/abs/2602.12918v1)**  
   - 日期：2026-02-13  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Distinguishing the feel of smooth silk from coarse cotton is a trivial everyday task for humans.
21. **[Replanning Human-Robot Collaborative Tasks with Vision-Language Models via Semantic and Physical Dual-Correction](https://arxiv.org/abs/2602.14551v1)**  
   - 日期：2026-02-16  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Human-Robot Collaboration (HRC) plays an important role in assembly tasks by enabling robots to plan and adjust their motions based on interactive, real-time human instructions.
22. **[Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation](https://arxiv.org/abs/2602.16705v2)**  
   - 日期：2026-02-18  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Visual loco-manipulation of arbitrary objects in the wild with humanoid robots requires accurate end-effector (EE) control and a generalizable understanding of the scene via visual
23. **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
   - 日期：2026-02-21  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：Synthetic data generated by video generative models has shown promise for robot learning as a scalable pipeline, but it often suffers from inconsistent action quality due to imperf
24. **[Energy-Based Injury Protection Database: Including Shearing Contact Thresholds for Hand and Finger Using Porcine Surrogates](https://arxiv.org/abs/2602.20362v1)**  
   - 日期：2026-02-23  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：While robotics research continues to propose strategies for collision avoidance in human-robot interaction, the reality of constrained environments and future humanoid systems make
25. **[Task-oriented grasping for dexterous robots using postural synergies and reinforcement learning](https://arxiv.org/abs/2602.20915v1)**  
   - 日期：2026-02-24  
   - 简介：该文聚焦操作与灵巧手，核心问题与方法可概括为：In this paper, we address the problem of task-oriented grasping for humanoid robots, emphasizing the need to align with human social norms and task-specific objectives.

## 感知与视觉语言（15篇）

1. **[WaveMan: mmWave-Based Room-Scale Human Interaction Perception for Humanoid Robots](https://arxiv.org/abs/2601.07454v1)**  
   - 日期：2026-01-12  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Reliable humanoid-robot interaction (HRI) in household environments is constrained by two fundamental requirements, namely robustness to unconstrained user positions and preservati
2. **[Heterogeneous computing platform for real-time robotics](https://arxiv.org/abs/2601.09755v1)**  
   - 日期：2026-01-13  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：After Industry 4.0 has embraced tight integration between machinery (OT), software (IT), and the Internet, creating a web of sensors, data, and algorithms in service of efficient a
3. **[Vision-Language Models on the Edge for Real-Time Robotic Perception](https://arxiv.org/abs/2601.14921v1)**  
   - 日期：2026-01-21  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Vision-Language Models (VLMs) enable multimodal reasoning for robotic perception and interaction, but their deployment in real-world systems remains constrained by latency, limited
4. **[Real-Time Synchronized Interaction Framework for Emotion-Aware Humanoid Robots](https://arxiv.org/abs/2601.17287v1)**  
   - 日期：2026-01-24  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：As humanoid robots increasingly introduced into social scene, achieving emotionally synchronized multimodal interaction remains a significant challenges.
5. **[Dynamic Worlds, Dynamic Humans: Generating Virtual Human-Scene Interaction Motion in Dynamic Scenes](https://arxiv.org/abs/2601.19484v1)**  
   - 日期：2026-01-27  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Scenes are continuously undergoing dynamic changes in the real world.
6. **[Green-VLA: Staged Vision-Language-Action Model for Generalist Robots](https://arxiv.org/abs/2602.00919v1)**  
   - 日期：2026-01-31  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：We introduce Green-VLA, a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid robot while maintaining generalization across diverse embodi
7. **[T2M Mamba: Motion Periodicity-Saliency Coupling Approach for Stable Text-Driven Motion Generation](https://arxiv.org/abs/2602.01352v1)**  
   - 日期：2026-02-01  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Text-to-motion generation, which converts motion language descriptions into coherent 3D human motion sequences, has attracted increasing attention in fields, such as avatar animati
8. **[RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots](https://arxiv.org/abs/2602.01515v1)**  
   - 日期：2026-02-02  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Deploying learned control policies on humanoid robots is challenging: policies that appear robust in simulation can execute confidently in out-of-distribution (OOD) states after Si
9. **[Learning Physiology-Informed Vocal Spectrotemporal Representations for Speech Emotion Recognition](https://arxiv.org/abs/2602.13259v1)**  
   - 日期：2026-02-03  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Speech emotion recognition (SER) is essential for humanoid robot tasks such as social robotic interactions and robotic psychological diagnosis, where interpretable and efficient mo
10. **[HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation](https://arxiv.org/abs/2602.04412v2)**  
   - 日期：2026-02-04  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Humanoid robots can suffer significant performance drops under small changes in dynamics, task specifications, or environment setup.
11. **[Bridging Speech, Emotion, and Motion: a VLM-based Multimodal Edge-deployable Framework for Humanoid Robots](https://arxiv.org/abs/2602.07434v1)**  
   - 日期：2026-02-07  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Effective human-robot interaction requires emotionally rich multimodal expressions, yet most humanoid robots lack coordinated speech, facial expressions, and gestures.
12. **[Future Mining: Learning for Safety and Security](https://arxiv.org/abs/2602.11472v1)**  
   - 日期：2026-02-12  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Mining is rapidly evolving into an AI driven cyber physical ecosystem where safety and operational reliability depend on robust perception, trustworthy distributed intelligence, an
13. **[ProAct: A Dual-System Framework for Proactive Embodied Social Agents](https://arxiv.org/abs/2602.14048v1)**  
   - 日期：2026-02-15  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Embodied social agents have recently advanced in generating synchronized speech and gestures.
14. **[Humanizing Robot Gaze Shifts: A Framework for Natural Gaze Shifts in Humanoid Robots](https://arxiv.org/abs/2602.21983v1)**  
   - 日期：2026-02-25  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Leveraging auditory and visual feedback for attention reorientation is essential for natural gaze shifts in social interaction.
15. **[EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents](https://arxiv.org/abs/2602.23205v1)**  
   - 日期：2026-02-26  
   - 简介：该文聚焦感知与视觉语言，核心问题与方法可概括为：Human behaviors in the real world naturally encode rich, long-term contextual information that can be leveraged to train embodied agents for perception, understanding, and acting.

## 仿真与Sim2Real（3篇）

1. **[RSLCPP -- Deterministic Simulations Using ROS 2](https://arxiv.org/abs/2601.07052v1)**  
   - 日期：2026-01-11  
   - 简介：该文聚焦仿真与Sim2Real，核心问题与方法可概括为：Simulation is crucial in real-world robotics, offering safe, scalable, and efficient environments for developing applications, ranging from humanoid robots to autonomous vehicles a
2. **[HumanoidTurk: Expanding VR Haptics with Humanoids for Driving Simulations](https://arxiv.org/abs/2601.18975v1)**  
   - 日期：2026-01-26  
   - 简介：该文聚焦仿真与Sim2Real，核心问题与方法可概括为：We explore how humanoid robots can be repurposed as haptic media, extending beyond their conventional role as social, assistive, collaborative agents.
3. **[Human-in-the-Loop Failure Recovery with Adaptive Task Allocation](https://arxiv.org/abs/2602.03603v1)**  
   - 日期：2026-02-03  
   - 简介：该文聚焦仿真与Sim2Real，核心问题与方法可概括为：Since the recent Covid-19 pandemic, mobile manipulators and humanoid assistive robots with higher levels of autonomy have increasingly been adopted for patient care and living assi

## 硬件设计与安全（6篇）

1. **[AdaMorph: Unified Motion Retargeting via Embodiment-Aware Adaptive Transformers](https://arxiv.org/abs/2601.07284v1)**  
   - 日期：2026-01-12  
   - 简介：该文聚焦硬件设计与安全，核心问题与方法可概括为：Retargeting human motion to heterogeneous robots is a fundamental challenge in robotics, primarily due to the severe kinematic and dynamic discrepancies between varying embodiments
2. **[FlowAct-R1: Towards Interactive Humanoid Video Generation](https://arxiv.org/abs/2601.10103v1)**  
   - 日期：2026-01-15  
   - 简介：该文聚焦硬件设计与安全，核心问题与方法可概括为：Interactive humanoid video generation aims to synthesize lifelike visual agents that can engage with humans through continuous and responsive video.
3. **[Whether We Care, How We Reason: The Dual Role of Anthropomorphism and Moral Foundations in Robot Abuse](https://arxiv.org/abs/2601.19826v1)**  
   - 日期：2026-01-27  
   - 简介：该文聚焦硬件设计与安全，核心问题与方法可概括为：As robots become increasingly integrated into daily life, understanding responses to robot mistreatment carries important ethical and design implications.
4. **[Cerebellar-Inspired Residual Control for Fault Recovery: From Inference-Time Adaptation to Structural Consolidation](https://arxiv.org/abs/2602.07227v1)**  
   - 日期：2026-02-06  
   - 简介：该文聚焦硬件设计与安全，核心问题与方法可概括为：Robotic policies deployed in real-world environments often encounter post-training faults, where retraining, exploration, or system identification are impractical.
5. **[VividFace: Real-Time and Realistic Facial Expression Shadowing for Humanoid Robots](https://arxiv.org/abs/2602.07506v2)**  
   - 日期：2026-02-07  
   - 简介：该文聚焦硬件设计与安全，核心问题与方法可概括为：Humanoid facial expression shadowing enables robots to realistically imitate human facial expressions in real time, which is critical for lifelike, facially expressive humanoid rob
6. **[Characteristics, Management, and Utilization of Muscles in Musculoskeletal Humanoids: Empirical Study on Kengoro and Musashi](https://arxiv.org/abs/2602.08518v1)**  
   - 日期：2026-02-09  
   - 简介：该文聚焦硬件设计与安全，核心问题与方法可概括为：Various musculoskeletal humanoids have been developed so far, and numerous studies on control mechanisms have been conducted to leverage the advantages of their biomimetic bodies.

## 评测/综述/数据集（3篇）

1. **[DreamActor-M2: Universal Character Image Animation via Spatiotemporal In-Context Learning](https://arxiv.org/abs/2601.21716v1)**  
   - 日期：2026-01-29  
   - 简介：该文聚焦评测/综述/数据集，核心问题与方法可概括为：Character image animation aims to synthesize high-fidelity videos by transferring motion from a driving sequence to a static reference image.
2. **[Zero-Shot Off-Policy Learning](https://arxiv.org/abs/2602.01962v1)**  
   - 日期：2026-02-02  
   - 简介：该文聚焦评测/综述/数据集，核心问题与方法可概括为：Off-policy learning methods seek to derive an optimal policy directly from a fixed dataset of prior interactions.
3. **[Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control](https://arxiv.org/abs/2602.21599v1)**  
   - 日期：2026-02-25  
   - 简介：该文聚焦评测/综述/数据集，核心问题与方法可概括为：Physics-based humanoid control relies on training with motion datasets that have diverse data distributions.

## 其他与综合方法（3篇）

1. **[Task-Centric Policy Optimization from Misaligned Motion Priors](https://arxiv.org/abs/2601.19411v2)**  
   - 日期：2026-01-27  
   - 简介：该文聚焦其他与综合方法，核心问题与方法可概括为：Humanoid control often leverages motion priors from human demonstrations to encourage natural behaviors.
2. **[PDF-HR: Pose Distance Fields for Humanoid Robots](https://arxiv.org/abs/2602.04851v1)**  
   - 日期：2026-02-04  
   - 简介：该文聚焦其他与综合方法，核心问题与方法可概括为：Pose and motion priors play a crucial role in humanoid robotics.
3. **[WIMLE: Uncertainty-Aware World Models with IMLE for Sample-Efficient Continuous Control](https://arxiv.org/abs/2602.14351v1)**  
   - 日期：2026-02-15  
   - 简介：该文聚焦其他与综合方法，核心问题与方法可概括为：Model-based reinforcement learning promises strong sample efficiency but often underperforms in practice due to compounding model error, unimodal world models that average over mul
