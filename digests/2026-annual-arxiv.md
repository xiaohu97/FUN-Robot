# 2026 年 arXiv 机器人与具身智能论文年度总览

> ⬅️ [进展速递索引](./README.md)
>
> 范围：2026-01-01 ~ 2026-11-05，共 **14960** 篇（cs.RO 全部 + 其他分类的具身智能论文）。 排序按热度 = 引用数（Semantic Scholar，统计于 2026-11-05）+ 0.5×Hugging Face 点赞数。

## 月度 × 方向统计

| 方向 | [1月](./2026-01-arxiv.md) | [2月](./2026-02-arxiv.md) | [3月](./2026-03-arxiv.md) | [4月](./2026-04-arxiv.md) | [5月](./2026-05-arxiv.md) | [6月](./2026-06-arxiv.md) | [7月](./2026-07-arxiv.md) | [8月](./2026-08-arxiv.md) | [9月](./2026-09-arxiv.md) | [10月](./2026-10-arxiv.md) | [11月](./2026-11-arxiv.md) | 合计 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [01 · VLA 与机器人基础模型](#01) | 48 | 84 | 105 | 63 | 136 | 149 | 96 | 110 | 214 | 232 | 23 | 1260 |
| [02 · 世界动作模型（WAM）](#02) | 0 | 2 | 5 | 9 | 12 | 31 | 22 | 44 | 61 | 85 | 6 | 277 |
| [03 · 世界模型与视频生成](#03) | 20 | 33 | 39 | 21 | 39 | 64 | 41 | 46 | 87 | 106 | 9 | 505 |
| [04 · 具身推理与任务规划](#04) | 53 | 81 | 97 | 77 | 79 | 81 | 64 | 79 | 106 | 97 | 11 | 825 |
| [05 · 机器人智能体与自我进化](#05) | 1 | 3 | 9 | 3 | 6 | 15 | 5 | 19 | 48 | 69 | 4 | 182 |
| [06 · 模仿学习与策略学习](#06) | 18 | 31 | 50 | 35 | 51 | 66 | 37 | 37 | 81 | 106 | 9 | 521 |
| [07 · 强化学习与后训练](#07) | 33 | 48 | 73 | 35 | 70 | 66 | 41 | 39 | 63 | 81 | 10 | 559 |
| [08 · 奖励模型、失败检测与恢复](#08) | 5 | 6 | 13 | 7 | 14 | 22 | 10 | 12 | 21 | 24 | 1 | 135 |
| [09 · 记忆与长时程任务](#09) | 14 | 23 | 56 | 32 | 49 | 69 | 56 | 57 | 100 | 119 | 12 | 587 |
| [10 · 足式运动控制](#10) | 22 | 42 | 59 | 36 | 35 | 44 | 30 | 33 | 74 | 62 | 2 | 439 |
| [11 · 人形机器人](#11) | 26 | 46 | 69 | 27 | 34 | 80 | 47 | 38 | 108 | 135 | 16 | 626 |
| [12 · 操作、抓取与灵巧手](#12) | 63 | 108 | 149 | 82 | 112 | 173 | 114 | 114 | 257 | 234 | 22 | 1428 |
| [13 · 触觉与接触感知](#13) | 22 | 29 | 47 | 27 | 32 | 50 | 48 | 53 | 70 | 68 | 12 | 458 |
| [14 · 具身导航与移动操作](#14) | 69 | 66 | 129 | 64 | 85 | 86 | 97 | 66 | 117 | 155 | 9 | 943 |
| [15 · 视觉表征与 3D 场景理解](#15) | 22 | 37 | 51 | 37 | 47 | 37 | 35 | 31 | 71 | 50 | 5 | 423 |
| [16 · 数据采集、遥操作与人类视频](#16) | 27 | 35 | 54 | 46 | 43 | 55 | 48 | 30 | 50 | 54 | 9 | 451 |
| [17 · 仿真、Sim2Real 与评测基准](#17) | 21 | 22 | 36 | 28 | 44 | 46 | 29 | 41 | 66 | 78 | 7 | 418 |
| [18 · 综述与教程](#18) | 14 | 7 | 10 | 20 | 12 | 4 | 13 | 6 | 12 | 10 | 1 | 109 |
| [19 · 自动驾驶](#19) | 45 | 66 | 94 | 75 | 91 | 94 | 71 | 72 | 106 | 89 | 8 | 811 |
| [20 · 空中、水下与空间机器人](#20) | 55 | 86 | 96 | 64 | 84 | 85 | 98 | 79 | 145 | 109 | 7 | 908 |
| [21 · SLAM、定位与建图](#21) | 48 | 54 | 103 | 71 | 73 | 97 | 77 | 59 | 109 | 100 | 11 | 802 |
| [22 · 运动规划与控制](#22) | 37 | 71 | 98 | 77 | 96 | 83 | 81 | 71 | 121 | 129 | 10 | 874 |
| [23 · 多机器人与人机交互](#23) | 31 | 57 | 68 | 55 | 57 | 51 | 47 | 53 | 76 | 58 | 7 | 560 |
| [24 · 医疗、软体与特种机器人](#24) | 31 | 46 | 71 | 34 | 24 | 42 | 28 | 44 | 67 | 44 | 10 | 441 |
| [99 · 其他](#99) | 24 | 39 | 38 | 33 | 32 | 32 | 32 | 36 | 72 | 73 | 7 | 418 |
| **合计** | **749** | **1122** | **1619** | **1058** | **1357** | **1622** | **1267** | **1269** | **2302** | **2367** | **228** | **14960** |

## 🏆 年度最热 Top 100

1. **[World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922)** · 2026-02-17 · Seonghyeon Ye et al. · 引用 604 · 👍 20 · [02 世界动作模型（WAM）](#02)
   > DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone, is introduced, a World Action Model (WAM) built upon a pretrained video diffusion backbone that enables few-shot embodiment adaptat…
2. **[Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666)** · 2026-03-17 · Tianyuan Yuan et al. · 引用 468 · [02 世界动作模型（WAM）](#02)
   > The proposed Fast-WAM architecture, a WAM architecture that retains video co-training during training but skips future prediction at test time, suggests that the main value of video prediction in WAMs may lie in improvi…
3. **[Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163)** · 2026-01-22 · Moo Jin Kim et al. · 引用 445 · 👍 15 · [06 模仿学习与策略学习](#06)
   > Cosmos Policy is introduced, a simple approach for adapting a large pretrained video model (Cosmos-Predict2) into an effective robot policy through a single stage of post-training on the robot demonstration data collect…
4. **[Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998)** · 2026-01-29 · Lin Li et al. · 引用 422 · 👍 32 · [03 世界模型与视频生成](#03)
   > LingBot-VA is introduced, an autoregressive diffusion framework that learns frame prediction and policy execution simultaneously, and shows significant promise in long-horizon manipulation, data efficiency in post-train…
5. **[Cosmos 3: Omnimodal World Models for Physical AI](https://arxiv.org/abs/2606.02800)** · 2026-06-01 ·  NVIDIA et al. · 引用 217 · 👍 142 · [03 世界模型与视频生成](#03)
   > This report introduces Cosmos 3, a family of omnimodal world models designed to jointly process and generate language, image, video, audio, and action sequences within a unified mixture-of-transformers architecture and…
6. **[MolmoAct2: Action Reasoning Models for Real-world Deployment](https://arxiv.org/abs/2605.02881)** · 2026-05-04 · Haoquan Fang et al. · 引用 98 · 👍 234 · [04 具身推理与任务规划](#04)
   > In the most extensive empirical study of any open VLA to date, spanning 7 simulation and real-world benchmarks, MolmoAct2 outperforms strong baselines including Pi-05, while MolmoER surpasses GPT-5 and Gemini Robotics E…
7. **[$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](https://arxiv.org/abs/2604.15483)** · 2026-04-16 · Physical Intelligence et al. · 引用 199 · [01 VLA 与机器人基础模型](#01)
   > A new robotic foundation model is presented that can enable strong out-of-the-box performance in a wide range of scenarios, and is conditioned not just on a language command that describes what it should do, but on addi…
8. **[DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://arxiv.org/abs/2602.06949)** · 2026-02-06 · Shenyuan Gao et al. · 引用 175 · 👍 37 · [03 世界模型与视频生成](#03)
   > Systematic evaluation on multiple challenging out-of-distribution (OOD) benchmarks verifies the significance of the method for simulating open-world, contact-rich tasks, paving the way for general-purpose robot world mo…
9. **[StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing](https://arxiv.org/abs/2604.05014)** · 2026-04-06 · StarVLA Community · 引用 190 · [01 VLA 与机器人基础模型](#01)
   > To the best knowledge, StarVLA is one of the most comprehensive open-source VLA frameworks available, and is expected to lower the barrier for reproducing existing methods and prototyping new ones.
10. **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482)** · 2026-03-15 · Lorenzo Mur-Labadia et al. · 引用 160 · 👍 40 · [15 视觉表征与 3D 场景理解](#15)
   > V-JEPA 2.1 is presented, a family of self-supervised models that learn dense, high-quality visual representations for both images and videos while retaining strong global scene understanding and world modeling and demon…
11. **[GigaWorld-Policy: An Efficient Action-Centered World--Action Model](https://arxiv.org/abs/2603.17240)** · 2026-03-18 · Angen Ye et al. · 引用 162 · 👍 28 · [02 世界动作模型（WAM）](#02)
   > GigaWorld-Policy is introduced, an action-centered WAM that learns 2D pixel-action dynamics while enabling efficient action decoding, with optional video generation, and runs 9x faster than the leading WAM baseline, Mot…
12. **[RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356)** · 2026-03-04 · Soroush Nasiriany et al. · 引用 165 · [17 仿真、Sim2Real 与评测基准](#17)
   > RoboCasa365, a comprehensive simulation benchmark for household mobile manipulation, is presented, designed to support systematic evaluations for different problem settings, including multi-task learning, robot foundati…
13. **[A Pragmatic VLA Foundation Model](https://arxiv.org/abs/2601.18692)** · 2026-01-26 · Wei Wu et al. · 引用 139 · 👍 50 · [01 VLA 与机器人基础模型](#01)
   > This work develops LingBot-VLA with around 20,000 hours of real-world data from 9 popular dual-arm robot configurations, achieving clear superiority over competitors, and provides open access to the code, base model, an…
14. **[Green-VLA: Staged Vision-Language-Action Model for Generalist Robots](https://arxiv.org/abs/2602.00919)** · 2026-01-31 · I. Apanasevich et al. · 引用 8 · 👍 311 · [01 VLA 与机器人基础模型](#01)
   > Green-VLA, a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid robot while maintaining generalization across diverse embodiments, shows strong generalization and performance g…
15. **[EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](https://arxiv.org/abs/2602.16710)** · 2026-02-18 · Ruijie Zheng et al. · 引用 163 · [12 操作、抓取与灵巧手](#12)
   > The final policy improves average success rate by 54% over a no pretraining baseline using a 22 DoF dexterous robotic hand, and transfers effectively to robots with lower DoF hands, indicating that large scale human mot…
16. **[VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model](https://arxiv.org/abs/2602.10098)** · 2026-02-10 · Jingwen Sun et al. · 引用 147 · 👍 25 · [03 世界模型与视频生成](#03)
   > By predicting in latent space rather than pixel space, VLA-JEPA learns dynamics abstractions that are robust to camera motion and irrelevant background changes, and achieves consistent gains in generalization and robust…
17. **[CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435)** · 2026-03-23 · Letian Fu et al. · 引用 159 · [05 机器人智能体与自我进化](#05)
   > CaP-X is presented, an open-access framework for systematically studying Code-as-Policy agents in robot manipulation, and CaP-Agent0, a training-free framework that recovers human-level reliability on several manipulati…
18. **[ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning](https://arxiv.org/abs/2602.11236)** · 2026-02-11 · Yandan Yang et al. · 引用 139 · 👍 13 · [01 VLA 与机器人基础模型](#01)
   > ABot-M0 is presented, a framework that builds a systematic data curation pipeline while jointly optimizing model architecture and training strategies, enabling end-to-end transformation of heterogeneous raw data into un…
19. **[Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](https://arxiv.org/abs/2605.30280)** · 2026-05-28 · Qiuyue Wang et al. · 引用 65 · 👍 144 · [01 VLA 与机器人基础模型](#01)
   > Qwen-VLA is presented, a unified embodied foundation model that extends Qwen's vision-language modeling stack from perception, understanding, and reasoning to continuous action and trajectory generation through a DiT-ba…
20. **[LeRobot: An Open-Source Library for End-to-End Robot Learning](https://arxiv.org/abs/2602.22818)** · 2026-02-26 · Remi Cadene et al. · 引用 132 · [16 数据采集、遥操作与人类视频](#16)
   > An open-source library that integrates across the entire robot learning stack, from low-level middleware communication for motor controls to large-scale dataset collection, storage and streaming, designed for accessibil…
21. **[Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993)** · 2026-01-19 · Hao Luo et al. · 引用 92 · 👍 77 · [01 VLA 与机器人基础模型](#01)
   > This work introduces Being-H0.5, a foundational Vision-Language-Action model designed for robust cross-embodiment generalization across diverse robotic platforms, and designs a unified sequential modeling and multi-task…
22. **[Utonia: Toward One Encoder for All Point Clouds](https://arxiv.org/abs/2603.03283)** · 2026-03-03 · Yujia Zhang et al. · 引用 39 · 👍 174 · [15 视觉表征与 3D 场景理解](#15)
   > Utonia is presented, a first step toward training a single self-supervised point transformer encoder across diverse domains, spanning remote sensing, outdoor LiDAR, indoor RGB-D sequences, object-centric CAD models, and…
23. **[A Very Big Video Reasoning Suite](https://arxiv.org/abs/2602.20159)** · 2026-02-23 · Maijunxian Wang et al. · 引用 32 · 👍 181 · [04 具身推理与任务规划](#04)
   > The Very Big Video Reasoning (VBVR) Dataset is introduced, an unprecedentedly large-scale resource spanning 200 curated reasoning tasks following a principled taxonomy and over one million video clips, approximately thr…
24. **[ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272)** · 2026-06-30 · Runyu Lu et al. · 引用 110 · 👍 24 · [05 机器人智能体与自我进化](#05)
   > ASIRE (Agentic Skill Programming through Iterative Robot Exploration), a continual learning system that autonomously writes and refines robot control programs in a code-as-policy paradigm while compounding experience in…
25. **[SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://arxiv.org/abs/2605.12500)** · 2026-05-12 · Haiwen Diao et al. · 引用 40 · 👍 152 · [04 具身推理与任务规划](#04)
   > This work introduces SenseNova-U1, a native unified multimodal paradigm built upon NEO-unify, in which understanding and generation evolve as synergistic views of a single underlying process that points toward a broader…
26. **[PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation](https://arxiv.org/abs/2601.03782)** · 2026-01-07 · Wenlong Huang et al. · 引用 114 · [03 世界模型与视频生成](#03)
   > It is demonstrated that a single pre-trained checkpoint enables a real-world Franka robot to perform rigid-body pushing, deformable and articulated object manipulation, and tool use, without requiring any demonstrations…
27. **[Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](https://arxiv.org/abs/2603.02115)** · 2026-03-02 · Anthony Liang et al. · 引用 110 · `RSS 2026` · [08 奖励模型、失败检测与恢复](#08)
   > Robometer is introduced, a scalable reward modeling framework that combines intra-trajectory progress supervision with inter-trajectory preference supervision, and learns more generalizable reward functions than prior m…
28. **[Being-H0.7: A Latent World-Action Model from Egocentric Videos](https://arxiv.org/abs/2605.00078)** · 2026-04-30 · Hao Luo et al. · 引用 109 · [02 世界动作模型（WAM）](#02)
   > Being-H0.7 is presented, a latent world-action model that brings future-aware reasoning into VLA-style policies without generating future frames, combining the predictive benefits of world models with the efficiency and…
29. **[LocateAnything: Fast and High-Quality Vision-Language Grounding with Parallel Box Decoding](https://arxiv.org/abs/2605.27365)** · 2026-05-26 · Shihao Wang et al. · 引用 37 · 👍 142 · [21 SLAM、定位与建图](#21)
   > LocateAnything, a unified generative grounding and detection framework based on Parallel Box Decoding (PBD), is introduced, achieving significantly higher decoding throughput while improving high-IoU localization qualit…
30. **[RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](https://arxiv.org/abs/2603.04639)** · 2026-03-04 · Yinpei Dai et al. · 引用 85 · 👍 31 · `ICML 2026` · [09 记忆与长时程任务](#09)
   > RoboMME is introduced: a large-scale standardized benchmark for evaluating and advancing VLA models in long-horizon, history-dependent scenarios and a suite of 14 memory-augmented VLA variants built on the {\pi}0.5 back…
31. **[RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269)** · 2026-05-05 · Dongyoung Kim et al. · 引用 46 · 👍 106 · [01 VLA 与机器人基础模型](#01)
   > This work introduces RLDX-1, a general-purpose robotic policy for dexterous manipulation built on the Multi-Stream Action Transformer (MSAT), an architecture that unifies these capabilities by integrating heterogeneous…
32. **[Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694)** · 2026-04-29 · Jun Guo et al. · 引用 95 · 👍 5 · [02 世界动作模型（WAM）](#02)
   > We propose X-WAM, a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis (video + 3D reconstruction) in a single framework, addressing the critical limitations of p…
33. **[RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies](https://arxiv.org/abs/2607.04434)** · 2026-07-05 · Tianxing Chen et al. · 引用 90 · 👍 15 · [17 仿真、Sim2Real 与评测基准](#17)
   > RoboDojo is introduced, a unified sim-and-real benchmark for comprehensive evaluation of generalist robot manipulation policies that integrates 30 policies into XPolicyLab and evaluates them on RoboDojo, establishing a…
34. **[MEM: Multi-Scale Embodied Memory for Vision Language Action Models](https://arxiv.org/abs/2603.03596)** · 2026-03-04 · Marcel Torne et al. · 引用 97 · [09 记忆与长时程任务](#09)
   > This work introduces Multi-Scale Embodied Memory (MEM), an approach for mixed-modal long-horizon memory in robot policies that combines video-based short-horizon memory, compressed via a video encoder, with text-based l…
35. **[EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World](https://arxiv.org/abs/2604.07607)** · 2026-04-08 · Ryan Punamiya et al. · 引用 96 · [16 数据采集、遥操作与人类视频](#16)
   > EgoVerse is introduced, a collaborative platform for human data-driven robot learning that unifies data collection, processing, and access under a shared framework, enabling contributions from individual researchers, ac…
36. **[World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090)** · 2026-05-12 · Siyin Wang et al. · 引用 59 · 👍 73 · [02 世界动作模型（WAM）](#02)
   > Overall, this survey provides the first systematic account of the WAMs landscape, clarifies key architectural paradigms and their trade-offs, and identifies open challenges and future opportunities for this rapidly evol…
37. **[Zetta $ζ$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](https://arxiv.org/abs/2608.16590)** · 2026-08-17 · Xin Ding et al. · 引用 25 · 👍 140 · [05 机器人智能体与自我进化](#05)
   > Zetta is presented, a closed-loop embodied harness that evolves code-based runtime critics and recovery skills online while keeping the base policy frozen, and shows that closed-loop harness self-evolution opens a scali…
38. **[Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://arxiv.org/abs/2607.15330)** · 2026-07-16 ·  Xiaomi Robotics Team et al. · 引用 60 · 👍 69 · [01 VLA 与机器人基础模型](#01)
   > Xiao-Robotics-1 serves as a strong robot foundation policy that can be efficiently fine-tuned on complex, dexterous tasks with high data efficiency and across multiple simulation benchmarks, Xiaomi-Robotics-1 outperform…
39. **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)** · 2026-07-09 · Yixian Zhang et al. · 引用 94 · [09 记忆与长时程任务](#09)
   > Hness VLA is presented, a memory-augmented agentic framework that exposes a frozen VLA as a retryable contact-rich primitive and composes it with a small fixed library of analytic primitives for grounding, staging, tran…
40. **[DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation](https://arxiv.org/abs/2601.22153)** · 2026-01-29 · Haozhe Xie et al. · 引用 54 · 👍 77 · [01 VLA 与机器人基础模型](#01)
   > The Dynamic Object Manipulation (DOM) benchmark is introduced, built with an automated collection pipeline that gathers 200K synthetic episodes across 2.8K scenes and 206 objects, and enables fast collection of 2K real-…
41. **[DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control](https://arxiv.org/abs/2603.10448)** · 2026-03-11 · Teli Ma et al. · 引用 92 · [03 世界模型与视频生成](#03)
   > DiT4DiT, an end-to-end Video-Action Model that couples a video Diffusion Transformer with an action Diffusion Transformer in a unified cascaded framework, is introduced, demonstrating that video generation can serve as…
42. **[WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](https://arxiv.org/abs/2602.08971)** · 2026-02-09 · Yu Shang et al. · 引用 85 · [03 世界模型与视频生成](#03)
   > This work introduces WorldArena, a unified benchmark designed to systematically evaluate embodied world models across both perceptual and functional dimensions, and proposes EWMScore, a holistic metric integrating multi…
43. **[Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](https://arxiv.org/abs/2606.17846)** · 2026-06-16 · Haoqi Yuan et al. · 引用 68 · 👍 33 · [12 操作、抓取与灵巧手](#12)
   > Qwen-RobotManip substantially outperforms prior state-of-the-art models, including $\pi$0.5, across all OOD settings, ranks 1st in RoboChallenge with a 20% relative improvement, and is validated on real-robot platforms…
44. **[Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522)** · 2026-09-09 · Yanzhe Chen et al. · 引用 35 · 👍 99 · [05 机器人智能体与自我进化](#05)
   > Show-Harness, an Embodied Harness that enables VLMs to"play" robots through a compact semantic interface linking intent to action, and develops GUMI (GUI Manipulation Interface), which extends the same semantic action s…
45. **[mjlab: A Lightweight Framework for GPU-Accelerated Robot Learning](https://arxiv.org/abs/2601.22074)** · 2026-01-29 · Kevin Zakka et al. · 引用 84 · [12 操作、抓取与灵巧手](#12)
   > We present mjlab, a lightweight, open-source framework for robot learning that combines GPU-accelerated simulation with composable environments and minimal setup friction. mjlab adopts the manager-based API introduced b…
46. **[SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://arxiv.org/abs/2602.10116)** · 2026-02-10 · Hongchi Xia et al. · 引用 76 · 👍 14 · [16 数据采集、遥操作与人类视频](#16)
   > SAGE is presented, an agentic framework that, given a user-specified embodied task, understands the intent and automatically generates simulation-ready environments at scale, demonstrating the promise of simulation-driv…
47. **[RoboReward: General-Purpose Vision-Language Reward Models for Robotics](https://arxiv.org/abs/2601.00675)** · 2026-01-02 · Tony Lee et al. · 引用 81 · [08 奖励模型、失败检测与恢复](#08)
   > This work introduces RoboReward, a robotics reward dataset and benchmark built on large-scale real-robot corpora from Open X-Embodiment and RoboArena, and trains general-purpose 4B- and 8B-parameter models that outperfo…
48. **[HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://arxiv.org/abs/2604.07430)** · 2026-04-08 · Tencent Robotics X et al. · 引用 19 · 👍 116 · [04 具身推理与任务规划](#04)
   > This work introduces HY-Embodied-0.5, a family of foundation models specifically designed for real-world embodied agents, developed to enhance the core capabilities required by embodied intelligence: spatial and tempora…
49. **[Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046)** · 2026-06-15 · Jisang Han et al. · 引用 22 · 👍 110 · [12 操作、抓取与灵巧手](#12)
   > The Geometric Action Model (GAM), a language-conditioned manipulation policy that directly repurposes a pretrained geometric foundation model (GFM) as a shared substrate for perception, temporal prediction, and action d…
50. **[ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980)** · 2026-06-18 · Wenli Xiao et al. · 引用 70 · 👍 14 · [05 机器人智能体与自我进化](#05)
   > Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering, which becomes a central bottleneck in the pursuit of general physical intelligence.
51. **[OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)** · 2026-09-07 · Yuran Wang et al. · 引用 42 · 👍 69 · [02 世界动作模型（WAM）](#02)
   > This work introduces OpenWAM, an open research stack that turns world-action pretraining into a controlled experimental program, and releases the full stack, including infrastructure, evaluation protocols, pretrained mo…
52. **[PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381)** · 2026-10-27 · Hanqing Wang et al. · 引用 0 · 👍 153 · [01 VLA 与机器人基础模型](#01)
   > PDRVLA is introduced, whose lightweight Physical Dynamics Module extracts physical tokens from vision--language features to condition action generation without online video generation, andlations show improved future pr…
53. **[AHA-WAM:Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing](https://arxiv.org/abs/2606.09811)** · 2026-06-08 · Jisong Cai et al. · 引用 67 · 👍 15 · [02 世界动作模型（WAM）](#02)
   > This work proposes AHA-WAM, an Asynchronous Horizon-Adaptive World-Action Model built on a dual Diffusion Transformer (DiT) architecture that reorganizes world-action modeling around this temporal asymmetry, and introdu…
54. **[LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies](https://arxiv.org/abs/2606.15768)** · 2026-06-14 · Jialei Chen et al. · 引用 73 · 👍 3 · `CoRL 2026` · [02 世界动作模型（WAM）](#02)
   > LaWAM is a Latent World Action Model that exposes predictive dynamics to robot policies through compact latent visual subgoals instead of reconstructed future video and achieves up to 24x lower wall-clock latency than p…
55. **[RISE: Self-Improving Robot Policy with Compositional World Model](https://arxiv.org/abs/2602.11075)** · 2026-02-11 · Jiazhi Yang et al. · 引用 59 · 👍 30 · [03 世界模型与视频生成](#03)
   > RISE is a scalable framework of robotic reinforcement learning via imagination that predicts multi-view future via a controllable dynamics model, and evaluates imagined outcomes with a progress value model, producing in…
56. **[RMBench: Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design](https://arxiv.org/abs/2603.01229)** · 2026-03-01 · Tianxing Chen et al. · 引用 74 · [09 记忆与长时程任务](#09)
   > RMBench is introduced, a simulation benchmark comprising 9 manipulation tasks that span multiple levels of memory complexity, enabling systematic evaluation of policy memory capabilities and Mem-0, a modular manipulatio…
57. **[Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution](https://arxiv.org/abs/2602.12684)** · 2026-02-13 · Rui Cai et al. · 引用 69 · 👍 7 · [01 VLA 与机器人基础模型](#01)
   > Xiaomi-Robotics-0 is first pre-trained on large-scale cross-embodiment robot trajectories and vision-language data, endowing it with broad and generalizable action-generation capabilities while avoiding catastrophic for…
58. **[VisuoTactile 6D Pose Estimation of an In-Hand Object using Vision and Tactile Sensor Data](https://arxiv.org/abs/2601.01675)** · 2026-01-04 · Snehal s. Dikhale et al. · 引用 72 · `RA-L` · [13 触觉与接触感知](#13)
   > This paper presents a method that uses both tactile and vision data to estimate the pose of an object grasped in a robots hand, and presents results of simulated experiments suggesting that using tactile data in additio…
59. **[ABot-Earth 0.5: Generative 3D Earth Model](https://arxiv.org/abs/2606.09967)** · 2026-06-08 · Ming Qian et al. · 引用 2 · 👍 139 · [15 视觉表征与 3D 场景理解](#15)
   > ABot-Earth 0.5 significantly lowers the technical and financial barriers to large-scale 3D reconstruction and empowers the future of global digital earth visualization.
60. **[LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion](https://arxiv.org/abs/2602.12215)** · 2026-02-12 · Jiangran Lyu et al. · 引用 71 · `RSS 2026` · [01 VLA 与机器人基础模型](#01)
   > This work introduces LDA-1B, a robot foundation model that scales through universal embodied data ingestion by jointly learning dynamics, policy, and visual forecasting, assigning distinct roles to data of varying quali…
61. **[SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://arxiv.org/abs/2602.09153)** · 2026-02-09 · Nicholas Pfaff et al. · 引用 68 · 👍 5 · `ICML 2026` · [12 操作、抓取与灵巧手](#12)
   > SceneSmith is introduced, a hierarchical agentic framework that generates simulation-ready indoor environments from natural language prompts that achieves 92% average realism and 91% average prompt faithfulness win rate…
62. **[Edge-Assisted Multi-Robot Visual-Inertial SLAM with Efficient Communication](https://arxiv.org/abs/2603.11085)** · 2026-03-11 · Xin Liu et al. · 引用 69 · [21 SLAM、定位与建图](#21)
   > A lightweight SLAM method of optical flow tracking based on pyramid IMU prediction is implemented to track non-keyframes and can achieve high-precision joint positioning with a low amount of transmitted data to reduce t…
63. **[RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/abs/2604.23073)** · 2026-04-24 · Charles Xu et al. · 引用 69 · [01 VLA 与机器人基础模型](#01)
   > This work introduces a lightweight method that enables sample-efficient online RL fine-tuning of pretrained VLAs using just a few hours of real-world practice, and improves the speed on the hardest part of the task by u…
64. **[ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models](https://arxiv.org/abs/2601.11404)** · 2026-01-16 · Linqing Zhong et al. · 引用 58 · 👍 19 · `CVPR` · [01 VLA 与机器人基础模型](#01)
   > This paper introduces Action Chain-of-Thought (ACoT), a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy.
65. **[Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471)** · 2026-10-15 ·  SenseNova et al. · 引用 0 · 👍 135 · [05 机器人智能体与自我进化](#05)
   > GPT-6-Astra has largely crossed the threshold of embodied competence, but not yet that of practical embodied intelligence, and the next generation of embodied benchmarks are envisioned.
66. **[ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531)** · 2026-06-17 · Yuyang Zhang et al. · 引用 55 · 👍 24 · [02 世界动作模型（WAM）](#02)
   > This work proposes ImageWAM, a simple WAM framework that repurposes pretrained image editing models for robot action prediction, and outperforms standard VLA baselines and matching competitive WAMs without additional po…
67. **[Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players](https://arxiv.org/abs/2605.28816)** · 2026-05-27 · Fangfu Liu et al. · 引用 19 · 👍 95 · [23 多机器人与人机交互](#23)
   > Simplex Rotary Agent Encoding is introduced, a parameter-free extension of 3D RoPE that represents agents as vertices of a regular simplex in rotary angle space that gives each agent a distinct phase while making all ag…
68. **[InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](https://arxiv.org/abs/2601.02456)** · 2026-01-05 · Junhao Cai et al. · 引用 66 · [01 VLA 与机器人基础模型](#01)
   > This model employs a unified Mixture-of-Transformers architecture, coordinating three experts for scene understanding, visual foresight generation, and action execution, which shows that InternVLA-A1 consistently outper…
69. **[Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching](https://arxiv.org/abs/2602.15827)** · 2026-02-17 · Zhen Wu et al. · 引用 66 · [11 人形机器人](#11)
   > Perceptive Humanoid Parkour (PHP) is presented, a modular framework that enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses and enables autonomous, con…
70. **[Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998)** · 2026-05-11 · Seth Karten et al. · 引用 57 · 👍 18 · [05 机器人智能体与自我进化](#05)
   > Continual Harness removes the human fully from this loop: a reset-free self-improving harness for embodied agents that formalizes and automates what was observed.
71. **[RynnBrain: Open Embodied Foundation Models](https://arxiv.org/abs/2602.14979)** · 2026-02-13 · Ronghao Dang et al. · 引用 43 · 👍 44 · [04 具身推理与任务规划](#04)
   > The post-trained model suite further substantiates two key potentials of the RynnBrain foundation model: enabling physically grounded reasoning and planning, and serving as a strong pretrained backbone that can be effic…
72. **[Driving on Registers](https://arxiv.org/abs/2601.05083)** · 2026-01-08 · Ellington Kirby et al. · 引用 64 · [19 自动驾驶](#19)
   > The results show that a pure-transformer architecture, combined with targeted token compression, is sufficient for accurate, efficient, and adaptive end-to-end driving.
73. **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080)** · 2026-04-30 · Bohan Hou et al. · 引用 56 · 👍 16 · [18 综述与教程](#18)
   > This survey systematically reviews the rapidly growing literature on world models for robot learning, clarifies key paradigms and applications, and highlights major challenges and future directions for predictive modeli…
74. **[Rethinking Video Generation Model for the Embodied World](https://arxiv.org/abs/2601.15282)** · 2026-01-21 · Yufan Deng et al. · 引用 41 · 👍 45 · [03 世界模型与视频生成](#03)
   > A comprehensive robotics benchmark, RBench, designed to evaluate robot-oriented video generation across five task domains and four distinct embodiments, and a refined four-stage data pipeline, resulting in RoVid-X, the…
75. **[$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)** · 2026-03-12 · Songlin Wei et al. · 引用 63 · [11 人形机器人](#11)
   > It is demonstrated that pre-training on high-quality egocentric human manipulation data followed by post-training on domain-specific real-world humanoid trajectories yields superior performance, in contrast to approache…
76. **[EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106)** · 2026-02-10 · Modi Shi et al. · 引用 50 · 👍 23 · [16 数据采集、遥操作与人类视频](#16)
   > EgoHumanoid is presented, the first framework to co-train a vision-language-action policy using abundant egocentric human demonstrations together with a limited amount of robot data, enabling humanoids to perform loco-m…
77. **[Kimodo: Scaling Controllable Human Motion Generation](https://arxiv.org/abs/2603.15546)** · 2026-03-16 · Davis Rempe et al. · 引用 61 · [16 数据采集、遥操作与人类视频](#16)
   > Kimodo is introduced, an expressive and controllable kinematic motion diffusion model trained on 700 hours of optical motion capture data and enabled through a carefully designed motion representation and two-stage deno…
78. **[Motubrain: An Advanced World Action Model for Robot Control](https://arxiv.org/abs/2604.27792)** · 2026-04-30 ·  Motubrain Team et al. · 引用 61 · [02 世界动作模型（WAM）](#02)
   > Motubrain is presented, a unified World Action Model that jointly models video and action under a UniDiffuser formulation with a three-stream Mixture-of-Transformers architecture that can scale in generality, predictive…
79. **[StarVLA-$α$: Reducing Complexity in Vision-Language-Action Systems](https://arxiv.org/abs/2604.11757)** · 2026-04-13 · Jinhui Ye et al. · 引用 60 · `ECCV 2026` · [01 VLA 与机器人基础模型](#01)
   > This work introduces StarVLA-$\alpha, a simple yet strong baseline designed to study VLA design choices under controlled conditions that deliberately minimizes architectural and pipeline complexity to reduce experimenta…
80. **[RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies](https://arxiv.org/abs/2604.09860)** · 2026-04-10 · Jenai Xuning Yang et al. · 引用 55 · 👍 8 · [17 仿真、Sim2Real 与评测基准](#17)
   > This work introduces RoboLab, a simulation benchmarking framework designed to answer two questions: to what extent can the authors understand the performance of a real-world policy by analyzing its behavior in simulatio…
81. **[Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419)** · 2026-06-17 · Junyi Zhang et al. · 引用 35 · 👍 48 · [05 机器人智能体与自我进化](#05)
   > Experiments show that play-learned skills improve held-out downstream tasks over no-play and random-play baselines, with 20.6 and 17.0 percentage-point gains over CaP-Agent0 on LIBERO-PRO and MolmoSpaces, respectively.
82. **[RoboBrain 2.5: Depth in Sight, Time in Mind](https://arxiv.org/abs/2601.14352)** · 2026-01-20 · Huajie Tan et al. · 引用 52 · 👍 13 · [04 具身推理与任务规划](#04)
   > RoboBrain 2.5 introduces RoboBrain 2.5, a next-generation embodied AI foundation model that advances general perception, spatial reasoning, and temporal modeling through extensive training on high-quality spatiotemporal…
83. **[FASTER: Rethinking Real-Time Flow VLAs](https://arxiv.org/abs/2603.19199)** · 2026-03-19 · Yuxiang Lu et al. · 引用 29 · 👍 59 · [01 VLA 与机器人基础模型](#01)
   > This paper presents a systematic analysis of the factors governing reaction time and proposes Fast Action Sampling for ImmediaTE Reaction (FASTER), which substantially reduces the effective reaction latency on real robo…
84. **[Xiaomi OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation](https://arxiv.org/abs/2604.18486)** · 2026-04-20 · Jinghui Lu et al. · 引用 12 · 👍 93 · [04 具身推理与任务规划](#04)
   > Across four benchmarks, OneVL becomes the first latent CoT method to surpass explicit CoT, delivering superior accuracy at answer-only latency, and shows that with world model supervision, latent CoT produces more gener…
85. **[TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics](https://arxiv.org/abs/2602.19313)** · 2026-02-22 · Shirui Chen et al. · 引用 45 · 👍 26 · [08 奖励模型、失败检测与恢复](#08)
   > T TOPReward is introduced, a training-free progress reward method that probes pretrained Video-Language Models through their internal token probabilities rather than asking them to generate numerical progress values, an…
86. **[World Guidance: World Modeling in Condition Space for Action Generation](https://arxiv.org/abs/2602.22010)** · 2026-02-25 · Yue Su et al. · 引用 50 · 👍 16 · [01 VLA 与机器人基础模型](#01)
   > WoG (World Guidance), a framework that maps future observations into compact conditions by injecting them into the action inference pipeline, and demonstrates that modeling and predicting this condition space not only f…
87. **[Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](https://arxiv.org/abs/2601.09708)** · 2026-01-14 · Chi-Pin Huang et al. · 引用 31 · 👍 53 · [01 VLA 与机器人基础模型](#01)
   > Fast-ThinkAct is proposed, an efficient reasoning framework that achieves compact yet performant planning through verbalizable latent reasoning that enables reasoning-enhanced policy learning that effectively connects c…
88. **[Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning](https://arxiv.org/abs/2602.07845)** · 2026-02-08 · Yalcin Tur et al. · 引用 21 · 👍 71 · [01 VLA 与机器人基础模型](#01)
   > Recurrent-Depth VLA (RD-VLA), an architecture that achieves computational adaptivity via latent iterative refinement rather than explicit token generation, is introduced, replacing token-based reasoning with latent reas…
89. **[OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2603.19201)** · 2026-03-19 · Yuhang Zheng et al. · 引用 56 · [13 触觉与接触感知](#13)
   > Real-robot experiments across all six interaction categories show that OmniVTA outperforms existing methods and generalizes well to unseen objects and geometric configurations, confirming the value of combining predicti…
90. **[From Foundation to Application: Improving VLA Models in Practice](https://arxiv.org/abs/2607.06403)** · 2026-07-07 · Wei Wu et al. · 引用 46 · 👍 19 · [01 VLA 与机器人基础模型](#01)
   > Benefiting from the expanded pretraining data that covers whole-body degrees of freedom, LingBot-VLA-2.0 demonstrates strong cross-embodiment long-horizon mobile manipulation capability across the two robotic platforms.
91. **[Learning from Fleet Experience: Collective Experience Learning Across 96 Robots](https://arxiv.org/abs/2610.25736)** · 2026-10-19 · Chao Yu et al. · 引用 0 · 👍 111 · [12 操作、抓取与灵巧手](#12)
   > Results support CEL as a scalable approach to improving robot policy reliability through experience generated during deployment, in which robots pool execution experience to update a shared policy that returns to the fl…
92. **[Masked Depth Modeling for Spatial Perception](https://arxiv.org/abs/2601.17895)** · 2026-01-25 · Bin Tan et al. · 引用 40 · 👍 30 · [12 操作、抓取与灵巧手](#12)
   > It is argued that the inaccuracies from depth sensors can be viewed as "masked" signals that inherently reflect underlying geometric ambiguities that inherently reflect underlying geometric ambiguities.
93. **[In-the-Wild Compliant Manipulation with UMI-FT](https://arxiv.org/abs/2601.09988)** · 2026-01-15 · Hojung Choi et al. · 引用 54 · [12 操作、抓取与灵巧手](#12)
   > UMI-FT, a handheld data-collection platform that mounts compact, six-axis force/torque sensors on each finger, enabling finger-level wrench measurements alongside RGB, depth, and pose, enables policies that reliably reg…
94. **[WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](https://arxiv.org/abs/2602.13977)** · 2026-02-15 · Zhennan Jiang et al. · 引用 54 · [03 世界模型与视频生成](#03)
   > WoVR is proposed, a reliable world-model-based RL framework for post-training VLA policies that enables stable long-horizon imagined rollouts and effective policy optimization, achieving superior LIBERO performance and…
95. **[Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/abs/2603.22078)** · 2026-03-23 · Zhanguang Zhang et al. · 引用 51 · 👍 6 · [02 世界动作模型（WAM）](#02)
   > A comparative study of prominent state-of-the-art VLA policies and recently released WAMs is conducted and shows that WAMs achieve strong robustness, with LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and…
96. **[LangForce: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries](https://arxiv.org/abs/2601.15197)** · 2026-01-21 · Shijie Lian et al. · 引用 34 · 👍 38 · [01 VLA 与机器人基础模型](#01)
   > LangForce is a novel framework that enforces instruction following via Bayesian decomposition and significantly improves generalization in Vision-Language-Action models, including an 11.3% improvement on the challenging…
97. **[LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models](https://arxiv.org/abs/2603.28301)** · 2026-03-30 · Chanyoung Kim et al. · 引用 20 · 👍 65 · `EMNLP 2026` · [01 VLA 与机器人基础模型](#01)
   > This work introduces LIBERO-Para, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization in VLA models, and proposes PRIDE, a met…
98. **[ABot-N1: Toward a General Visual Language Navigation Foundation Model](https://arxiv.org/abs/2607.10383)** · 2026-07-11 · Ruiyan Gong et al. · 引用 11 · 👍 83 · [14 具身导航与移动操作](#14)
   > ABot-N1 establishes new state-of-the-art records, delivering massive gains specifically in urban-scale navigation: boosting POI arrival by 35.0% (to 77.3%) and achieving 95.4%/92.9% SR in complex indoor and outdoor scen…
99. **[Interactive World Simulator for Robot Policy Training and Evaluation](https://arxiv.org/abs/2603.08546)** · 2026-03-09 · Yixuan Wang et al. · 引用 52 · [17 仿真、Sim2Real 与评测基准](#17)
   > Through extensive real-world evaluation across diverse tasks involving rigid objects, deformable objects, object piles, and their interactions, this work establishes the Interactive World Simulator as a stable and physi…
100. **[ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](https://arxiv.org/abs/2608.10915)** · 2026-08-11 · Qianggang Ding et al. · 引用 6 · 👍 92 · [17 仿真、Sim2Real 与评测基准](#17)
   > Combodied Agents is introduced, a human-centered paradigm that perceives, models, predicts, and supports individual human-state trajectories over time, using software tools, sensors, wearables, robots, and human service…

## 各方向年度 Top 20

<a id="01"></a>
### 01 · VLA 与机器人基础模型（1260 篇） · 长期清单 [papers/01-vla-foundation-models.md](../papers/01-vla-foundation-models.md)

- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](https://arxiv.org/abs/2604.15483) · 2026-04-16 · 引用 199
- [StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing](https://arxiv.org/abs/2604.05014) · 2026-04-06 · 引用 190
- [A Pragmatic VLA Foundation Model](https://arxiv.org/abs/2601.18692) · 2026-01-26 · 引用 139 · 👍 50
- [Green-VLA: Staged Vision-Language-Action Model for Generalist Robots](https://arxiv.org/abs/2602.00919) · 2026-01-31 · 引用 8 · 👍 311
- [ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning](https://arxiv.org/abs/2602.11236) · 2026-02-11 · 引用 139 · 👍 13
- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](https://arxiv.org/abs/2605.30280) · 2026-05-28 · 引用 65 · 👍 144
- [Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993) · 2026-01-19 · 引用 92 · 👍 77
- [RLDX-1 Technical Report](https://arxiv.org/abs/2605.03269) · 2026-05-05 · 引用 46 · 👍 106
- [Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://arxiv.org/abs/2607.15330) · 2026-07-16 · 引用 60 · 👍 69
- [DynamicVLA: A Vision-Language-Action Model for Dynamic Object Manipulation](https://arxiv.org/abs/2601.22153) · 2026-01-29 · 引用 54 · 👍 77
- [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381) · 2026-10-27 · 引用 0 · 👍 153
- [Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution](https://arxiv.org/abs/2602.12684) · 2026-02-13 · 引用 69 · 👍 7
- [LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion](https://arxiv.org/abs/2602.12215) · 2026-02-12 · 引用 71 · `RSS 2026`
- [RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/abs/2604.23073) · 2026-04-24 · 引用 69
- [ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models](https://arxiv.org/abs/2601.11404) · 2026-01-16 · 引用 58 · 👍 19 · `CVPR`
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](https://arxiv.org/abs/2601.02456) · 2026-01-05 · 引用 66
- [StarVLA-$α$: Reducing Complexity in Vision-Language-Action Systems](https://arxiv.org/abs/2604.11757) · 2026-04-13 · 引用 60 · `ECCV 2026`
- [FASTER: Rethinking Real-Time Flow VLAs](https://arxiv.org/abs/2603.19199) · 2026-03-19 · 引用 29 · 👍 59
- [World Guidance: World Modeling in Condition Space for Action Generation](https://arxiv.org/abs/2602.22010) · 2026-02-25 · 引用 50 · 👍 16
- [Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning](https://arxiv.org/abs/2601.09708) · 2026-01-14 · 引用 31 · 👍 53

<a id="02"></a>
### 02 · 世界动作模型（WAM）（277 篇） · 长期清单 [papers/02-world-action-models.md](../papers/02-world-action-models.md)

- [World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922) · 2026-02-17 · 引用 604 · 👍 20
- [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666) · 2026-03-17 · 引用 468
- [GigaWorld-Policy: An Efficient Action-Centered World--Action Model](https://arxiv.org/abs/2603.17240) · 2026-03-18 · 引用 162 · 👍 28
- [Being-H0.7: A Latent World-Action Model from Egocentric Videos](https://arxiv.org/abs/2605.00078) · 2026-04-30 · 引用 109
- [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694) · 2026-04-29 · 引用 95 · 👍 5
- [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090) · 2026-05-12 · 引用 59 · 👍 73
- [OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398) · 2026-09-07 · 引用 42 · 👍 69
- [AHA-WAM:Asynchronous Horizon-Adaptive World-Action Modeling with Observation-Guided Context Routing](https://arxiv.org/abs/2606.09811) · 2026-06-08 · 引用 67 · 👍 15
- [LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies](https://arxiv.org/abs/2606.15768) · 2026-06-14 · 引用 73 · 👍 3 · `CoRL 2026`
- [ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531) · 2026-06-17 · 引用 55 · 👍 24
- [Motubrain: An Advanced World Action Model for Robot Control](https://arxiv.org/abs/2604.27792) · 2026-04-30 · 引用 61
- [Do World Action Models Generalize Better than VLAs? A Robustness Study](https://arxiv.org/abs/2603.22078) · 2026-03-23 · 引用 51 · 👍 6
- [ABot-M0.5: Unified Mobility-and-Manipulation World Action Model](https://arxiv.org/abs/2607.00678) · 2026-07-01 · 引用 43 · 👍 15
- [Native Video-Action Pretraining for Generalizable Robot Control](https://arxiv.org/abs/2607.08639) · 2026-07-09 · 引用 48
- [Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528) · 2026-10-07 · 引用 2 · 👍 92
- [When to Trust Imagination: Adaptive Action Execution for World Action Models](https://arxiv.org/abs/2605.06222) · 2026-05-07 · 引用 26 · 👍 38
- [World Action Modeling with Progressive Visual Planning](https://arxiv.org/abs/2610.02508) · 2026-10-01 · 引用 1 · 👍 83
- [Light-WAM: Efficient World Action Models with State-Fusion Action Decoding](https://arxiv.org/abs/2606.08242) · 2026-06-06 · 引用 34 · 👍 12
- [What Makes World Action Models Generalize? An Empirical Study of Test-Time Future Modeling](https://arxiv.org/abs/2609.34981) · 2026-09-28 · 引用 0 · 👍 78
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](https://arxiv.org/abs/2608.26103) · 2026-08-26 · 引用 26 · 👍 23

<a id="03"></a>
### 03 · 世界模型与视频生成（505 篇） · 长期清单 [papers/03-world-models.md](../papers/03-world-models.md)

- [Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998) · 2026-01-29 · 引用 422 · 👍 32
- [Cosmos 3: Omnimodal World Models for Physical AI](https://arxiv.org/abs/2606.02800) · 2026-06-01 · 引用 217 · 👍 142
- [DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://arxiv.org/abs/2602.06949) · 2026-02-06 · 引用 175 · 👍 37
- [VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model](https://arxiv.org/abs/2602.10098) · 2026-02-10 · 引用 147 · 👍 25
- [PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation](https://arxiv.org/abs/2601.03782) · 2026-01-07 · 引用 114
- [DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control](https://arxiv.org/abs/2603.10448) · 2026-03-11 · 引用 92
- [WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](https://arxiv.org/abs/2602.08971) · 2026-02-09 · 引用 85
- [RISE: Self-Improving Robot Policy with Compositional World Model](https://arxiv.org/abs/2602.11075) · 2026-02-11 · 引用 59 · 👍 30
- [Rethinking Video Generation Model for the Embodied World](https://arxiv.org/abs/2601.15282) · 2026-01-21 · 引用 41 · 👍 45
- [WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](https://arxiv.org/abs/2602.13977) · 2026-02-15 · 引用 54
- [VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model](https://arxiv.org/abs/2602.12063) · 2026-02-12 · 引用 50
- [Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://arxiv.org/abs/2607.07675) · 2026-07-08 · 引用 20 · 👍 59
- [GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning](https://arxiv.org/abs/2602.12099) · 2026-02-12 · 引用 13 · 👍 62
- [GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774) · 2026-10-13 · 引用 0 · 👍 88
- [Motion Attribution for Video Generation](https://arxiv.org/abs/2601.08828) · 2026-01-13 · 引用 5 · 👍 72
- [World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy](https://arxiv.org/abs/2602.06508) · 2026-02-06 · 引用 40
- [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030) · 2026-06-15 · 引用 16 · 👍 46
- [$τ_0$-WM: A Unified Video-Action World Model for Robotic Manipulation](https://arxiv.org/abs/2606.01027) · 2026-05-31 · 引用 36 · 👍 1
- [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489) · 2026-08-13 · 引用 8 · 👍 52
- [RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/abs/2607.06559) · 2026-07-07 · 引用 15 · 👍 36

<a id="04"></a>
### 04 · 具身推理与任务规划（825 篇） · 长期清单 [papers/04-embodied-reasoning-planning.md](../papers/04-embodied-reasoning-planning.md)

- [MolmoAct2: Action Reasoning Models for Real-world Deployment](https://arxiv.org/abs/2605.02881) · 2026-05-04 · 引用 98 · 👍 234
- [A Very Big Video Reasoning Suite](https://arxiv.org/abs/2602.20159) · 2026-02-23 · 引用 32 · 👍 181
- [SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](https://arxiv.org/abs/2605.12500) · 2026-05-12 · 引用 40 · 👍 152
- [HY-Embodied-0.5: Embodied Foundation Models for Real-World Agents](https://arxiv.org/abs/2604.07430) · 2026-04-08 · 引用 19 · 👍 116
- [RynnBrain: Open Embodied Foundation Models](https://arxiv.org/abs/2602.14979) · 2026-02-13 · 引用 43 · 👍 44
- [RoboBrain 2.5: Depth in Sight, Time in Mind](https://arxiv.org/abs/2601.14352) · 2026-01-20 · 引用 52 · 👍 13
- [Xiaomi OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation](https://arxiv.org/abs/2604.18486) · 2026-04-20 · 引用 12 · 👍 93
- [LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391) · 2026-07-06 · 引用 42 · 👍 16
- [Transferring the Intelligence of VLMs to Robotic Control](https://arxiv.org/abs/2609.22966) · 2026-09-19 · 引用 17 · 👍 59
- [VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning](https://arxiv.org/abs/2608.26105) · 2026-08-26 · 引用 8 · 👍 75
- [ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop](https://arxiv.org/abs/2605.18746) · 2026-05-18 · 引用 39 · 👍 6
- [HumanCLAW: Can Vision-Language Models Act Through a Body?](https://arxiv.org/abs/2607.27180) · 2026-07-29 · 引用 4 · 👍 72
- [VLS: Steering Pretrained Robot Policies via Vision-Language Models](https://arxiv.org/abs/2602.03973) · 2026-02-03 · 引用 28 · 👍 22
- [PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models](https://arxiv.org/abs/2609.14973) · 2026-09-14 · 引用 1 · 👍 60
- [ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](https://arxiv.org/abs/2610.37666) · 2026-10-27 · 引用 0 · 👍 58
- [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739) · 2026-08-12 · 引用 28
- [LLMs are General Asynchronous Agents](https://arxiv.org/abs/2609.35427) · 2026-09-28 · 引用 0 · 👍 53
- [LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation](https://arxiv.org/abs/2608.30935) · 2026-08-31 · 引用 10 · 👍 31
- [In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138) · 2026-09-16 · 引用 15 · 👍 20
- [OAT: Ordered Action Tokenization](https://arxiv.org/abs/2602.04215) · 2026-02-04 · 引用 24

<a id="05"></a>
### 05 · 机器人智能体与自我进化（182 篇） · 长期清单 [papers/05-robot-agents.md](../papers/05-robot-agents.md)

- [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435) · 2026-03-23 · 引用 159
- [ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272) · 2026-06-30 · 引用 110 · 👍 24
- [Zetta $ζ$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](https://arxiv.org/abs/2608.16590) · 2026-08-17 · 引用 25 · 👍 140
- [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522) · 2026-09-09 · 引用 35 · 👍 99
- [ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980) · 2026-06-18 · 引用 70 · 👍 14
- [Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471) · 2026-10-15 · 引用 0 · 👍 135
- [Continual Harness: Online Adaptation for Self-Improving Foundation Agents](https://arxiv.org/abs/2605.09998) · 2026-05-11 · 引用 57 · 👍 18
- [Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419) · 2026-06-17 · 引用 35 · 👍 48
- [PhysEvo: Astra Can Act, Let It](https://arxiv.org/abs/2610.08995) · 2026-10-06 · 引用 2 · 👍 85
- [Articraft: An Agentic System for Scalable Articulated 3D Asset Generation](https://arxiv.org/abs/2605.15187) · 2026-05-14 · 引用 43
- [An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond](https://arxiv.org/abs/2609.24170) · 2026-09-21 · 引用 42
- [HexaShell: A Universal Harness for Robot Coding Agents in Simulation and the Real World](https://arxiv.org/abs/2610.23479) · 2026-10-16 · 引用 2 · 👍 80
- [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](https://arxiv.org/abs/2607.05369) · 2026-07-06 · 引用 28 · 👍 5 · `CoRL`
- [RHO: Your Coding Agent is Secretly a Roboticist](https://arxiv.org/abs/2606.16458) · 2026-06-15 · 引用 30
- [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) · 2026-08-11 · 引用 22 · 👍 15
- [EmbodiSkill: Skill-Aware Reflection for Self-Evolving Embodied Agents](https://arxiv.org/abs/2605.10332) · 2026-05-11 · 引用 27
- [Guava: Distilling Frontier VLMs into a Compact Agent through a Robotic Manipulation Harness](https://arxiv.org/abs/2606.18363) · 2026-06-16 · 引用 12 · 👍 26
- [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](https://arxiv.org/abs/2610.01939) · 2026-10-01 · 引用 13 · 👍 22
- [Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies](https://arxiv.org/abs/2609.38537) · 2026-09-29 · 引用 14 · 👍 19
- [Recursive Harness Distillation across Agents for Robot Manipulation](https://arxiv.org/abs/2609.33378) · 2026-09-27 · 引用 3 · 👍 39

<a id="06"></a>
### 06 · 模仿学习与策略学习（521 篇） · 长期清单 [papers/06-imitation-learning.md](../papers/06-imitation-learning.md)

- [Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163) · 2026-01-22 · 引用 445 · 👍 15
- [In-Context Learning for Robots: Methods and Applications](https://arxiv.org/abs/2609.36012) · 2026-09-28 · 引用 2 · 👍 89
- [Real-Time Robot Execution with Masked Action Chunking](https://arxiv.org/abs/2601.20130) · 2026-01-27 · 引用 40
- [USER: A Unified and Extensible System for Real-World Online Policy Learning in Embodied AI](https://arxiv.org/abs/2602.07837) · 2026-02-08 · 引用 5 · 👍 57 · `RSS 2026`
- [Learning Native Continuation for Action Chunking Flow Policies](https://arxiv.org/abs/2602.12978) · 2026-02-13 · 引用 28 · 👍 3 · `RSS 2026`
- [Agent Priors-guided Policy Learning](https://arxiv.org/abs/2609.35690) · 2026-09-28 · 引用 1 · 👍 50
- [Scalable Behavior Cloning with Open Data, Training, and Evaluation](https://arxiv.org/abs/2606.27375) · 2026-06-25 · 引用 21
- [Tune to Learn: How Controller Gains Shape Robot Policy Learning](https://arxiv.org/abs/2604.02523) · 2026-04-02 · 引用 18
- [PACE: Phase-Aware Chunk Execution for Robot Policies with Action Chunking](https://arxiv.org/abs/2606.00537) · 2026-05-30 · 引用 17 · `NeurIPS 2026`
- [Why Does Action Chunking Improve Behavioral Cloning Performance in Robotic Control?](https://arxiv.org/abs/2608.02547) · 2026-08-03 · 引用 17
- [STEP: Warm-Started Visuomotor Policies with Spatiotemporal Consistency Prediction](https://arxiv.org/abs/2602.08245) · 2026-02-09 · 引用 13 · `ICML 2026`
- [One-Step Flow Policy: Self-Distillation for Fast Visuomotor Policies](https://arxiv.org/abs/2603.12480) · 2026-03-12 · 引用 13
- [Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077) · 2026-08-18 · 引用 9 · 👍 7
- [Enhancing Visual Domain Robustness in Behaviour Cloning via Saliency-Guided Augmentation](https://arxiv.org/abs/2608.11870) · 2026-08-12 · 引用 12 · `CoRL`
- [HiPolicy: Hierarchical Multi-Frequency Action Chunking for Policy Learning](https://arxiv.org/abs/2604.06067) · 2026-04-07 · 引用 11
- [FLASH: Efficient Visuomotor Policy via Sparse Sampling](https://arxiv.org/abs/2605.15492) · 2026-05-15 · 引用 11 · `NeurIPS 2026`
- [Point Bridge: 3D Representations for Cross Domain Policy Learning](https://arxiv.org/abs/2601.16212) · 2026-01-22 · 引用 10
- [You've Got a Golden Ticket: Improving Generative Robot Policies With A Single Noise Vector](https://arxiv.org/abs/2603.15757) · 2026-03-16 · 引用 10
- [One Demo is Worth a Thousand Trajectories: Action-View Augmentation for Visuomotor Policies](https://arxiv.org/abs/2606.19586) · 2026-06-17 · 引用 10 · `CoRL 2025`
- [FutureRTC: Real-Time Robot Execution with Anticipatory-Conditioned Action Chunking](https://arxiv.org/abs/2607.24008) · 2026-07-27 · 引用 10

<a id="07"></a>
### 07 · 强化学习与后训练（559 篇） · 长期清单 [papers/07-rl-post-training.md](../papers/07-rl-post-training.md)

- [Q-learning with Adjoint Matching](https://arxiv.org/abs/2601.14234) · 2026-01-20 · 引用 48
- [Reinforcement Learning-Based Energy-Aware Coverage Path Planning for Precision Agriculture](https://arxiv.org/abs/2601.16405) · 2026-01-23 · 引用 35
- [InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions](https://arxiv.org/abs/2602.06035) · 2026-02-05 · 引用 18 · 👍 23
- [Emergent Dexterity via Diverse Resets and Large-Scale Reinforcement Learning](https://arxiv.org/abs/2603.15789) · 2026-03-16 · 引用 25
- [Trust Region Q Adjoint Matching](https://arxiv.org/abs/2605.27079) · 2026-05-26 · 引用 6 · 👍 24
- [From Prior to Pro: Efficient Skill Mastery via Distribution Contractive RL Finetuning](https://arxiv.org/abs/2603.10263) · 2026-03-10 · 引用 16 · 👍 3
- [FlashSAC: Fast and Stable Off-Policy Reinforcement Learning for High-Dimensional Robot Control](https://arxiv.org/abs/2604.04539) · 2026-04-06 · 引用 17
- [Failure-Aware RL: Reliable Offline-to-Online Reinforcement Learning with Self-Recovery for Real-World Manipulation](https://arxiv.org/abs/2601.07821) · 2026-01-12 · 引用 14
- [Q-Learning with Scalar Adjoint Matching](https://arxiv.org/abs/2610.10437) · 2026-10-07 · 引用 0 · 👍 24
- [From Passive Observer to Active Critic: Reinforcement Learning Elicits Process Reasoning for Robotic Manipulation](https://arxiv.org/abs/2603.15600) · 2026-03-16 · 引用 9 · 👍 4 · `ECCV 2026`
- [TwinRL: Digital Twin-Driven Reinforcement Learning for Real-World Robotic Manipulation](https://arxiv.org/abs/2602.09023) · 2026-02-09 · 引用 9
- [Regularized Latent Dynamics Prediction is a Strong Baseline For Behavioral Foundation Models](https://arxiv.org/abs/2603.15857) · 2026-03-16 · 引用 9
- [Learning-guided Prioritized Planning for Lifelong Multi-Agent Path Finding in Warehouse Automation](https://arxiv.org/abs/2603.23838) · 2026-03-25 · 引用 9
- [SpeedTuning: Speeding Up Policy Execution with Lightweight Reinforcement Learning](https://arxiv.org/abs/2608.09138) · 2026-08-10 · 引用 9 · `ICRA`
- [OGPO: One-Step Generative Policy Optimization for Real-Time Robot Control](https://arxiv.org/abs/2601.20701) · 2026-01-28 · 引用 8 · `ACM MM 2026`
- [Hierarchical Entity-centric Reinforcement Learning with Factored Subgoal Diffusion](https://arxiv.org/abs/2602.02722) · 2026-02-02 · 引用 8
- [High-Speed Vision-Based Flight in Clutter with Safety-Shielded Reinforcement Learning](https://arxiv.org/abs/2602.08653) · 2026-02-09 · 引用 8
- [HALO: Learning Human-Robot Collaboration via Heterogeneous-Agent Lyapunov Policy Optimization](https://arxiv.org/abs/2603.03741) · 2026-03-04 · 引用 8
- [Synthesis and Deployment of Maximal Robust Control Barrier Functions through Adversarial Reinforcement Learning](https://arxiv.org/abs/2604.13192) · 2026-04-14 · 引用 8
- [ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models](https://arxiv.org/abs/2610.18596) · 2026-10-13 · 引用 0 · 👍 16

<a id="08"></a>
### 08 · 奖励模型、失败检测与恢复（135 篇） · 长期清单 [papers/08-reward-failure-recovery.md](../papers/08-reward-failure-recovery.md)

- [Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons](https://arxiv.org/abs/2603.02115) · 2026-03-02 · 引用 110 · `RSS 2026`
- [RoboReward: General-Purpose Vision-Language Reward Models for Robotics](https://arxiv.org/abs/2601.00675) · 2026-01-02 · 引用 81
- [TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics](https://arxiv.org/abs/2602.19313) · 2026-02-22 · 引用 45 · 👍 26
- [ViVa: A Video-Generative Value Model for Robot Reinforcement Learning](https://arxiv.org/abs/2604.08168) · 2026-04-09 · 引用 14 · 👍 15
- [Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring](https://arxiv.org/abs/2605.30834) · 2026-05-29 · 引用 17 · 👍 8
- [ProcVLM: Learning Procedure-Grounded Progress Rewards for Robotic Manipulation](https://arxiv.org/abs/2605.08774) · 2026-05-09 · 引用 19
- [Large Reward Models: Generalizable Online Robot Reward Generation with Vision-Language Models](https://arxiv.org/abs/2603.16065) · 2026-03-17 · 引用 17
- [From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation](https://arxiv.org/abs/2605.11951) · 2026-05-12 · 引用 17 · `RSS 2026`
- [PRM-as-a-Judge 1.5: A Toolkit for Robot Process Assessment](https://arxiv.org/abs/2608.14284) · 2026-08-14 · 引用 5 · 👍 15
- [Self-Refining Vision Language Model for Robotic Failure Detection and Reasoning](https://arxiv.org/abs/2602.12405) · 2026-02-12 · 引用 12
- [When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering](https://arxiv.org/abs/2602.22474) · 2026-02-25 · 引用 12
- [PRM-as-a-Judge: A Dense Evaluation Paradigm for Fine-Grained Robotic Auditing](https://arxiv.org/abs/2603.21669) · 2026-03-23 · 引用 12
- [Rewind-IL: Online Failure Detection and State Respawning for Imitation Learning](https://arxiv.org/abs/2604.16683) · 2026-04-17 · 引用 12
- [Sentinel-VLA: A Metacognitive VLA Model with Active Status Monitoring for Dynamic Reasoning and Error Recovery](https://arxiv.org/abs/2605.01191) · 2026-05-02 · 引用 12
- [VLA-FAIL: Efficient Task Failure Detection for Finetuned Vision-Language-Action Models](https://arxiv.org/abs/2606.21386) · 2026-06-19 · 引用 11
- [World Value Models for Robotic Manipulation](https://arxiv.org/abs/2606.24742) · 2026-06-23 · 引用 8 · 👍 5
- [RoboValue: A Fine-Grained Sim-and-Real Benchmark for Unified Evaluation of Robotic Value Models](https://arxiv.org/abs/2610.26663) · 2026-10-19 · 引用 0 · 👍 21
- [SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation](https://arxiv.org/abs/2606.10305) · 2026-06-09 · 引用 10
- [AEROS: A Single-Agent Operating Architecture with Embodied Capability Modules](https://arxiv.org/abs/2604.07039) · 2026-04-08 · 引用 9
- [Position: Good Embodied Reward Models Need Bad Behavior Data](https://arxiv.org/abs/2606.01036) · 2026-05-31 · 引用 9 · `ICML 2026`

<a id="09"></a>
### 09 · 记忆与长时程任务（587 篇） · 长期清单 [papers/09-memory-long-horizon.md](../papers/09-memory-long-horizon.md)

- [RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies](https://arxiv.org/abs/2603.04639) · 2026-03-04 · 引用 85 · 👍 31 · `ICML 2026`
- [MEM: Multi-Scale Embodied Memory for Vision Language Action Models](https://arxiv.org/abs/2603.03596) · 2026-03-04 · 引用 97
- [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448) · 2026-07-09 · 引用 94
- [RMBench: Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design](https://arxiv.org/abs/2603.01229) · 2026-03-01 · 引用 74
- [RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558) · 2026-03-12 · 引用 51
- [PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2601.07060) · 2026-01-11 · 引用 47
- [BagelVLA: Enhancing Long-Horizon Manipulation via Interleaved Vision-Language-Action Generation](https://arxiv.org/abs/2602.09849) · 2026-02-10 · 引用 37 · 👍 16
- [EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies](https://arxiv.org/abs/2606.20092) · 2026-06-18 · 引用 42 · 👍 3
- [ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries](https://arxiv.org/abs/2603.12942) · 2026-03-13 · 引用 42
- [RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark](https://arxiv.org/abs/2605.10921) · 2026-05-11 · 引用 41 · 👍 2
- [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350) · 2026-07-11 · 引用 2 · 👍 70
- [Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2607.07608) · 2026-07-08 · 引用 7 · 👍 55
- [BPP: Long-Context Robot Imitation Learning by Focusing on Key History Frames](https://arxiv.org/abs/2602.15010) · 2026-02-16 · 引用 31
- [Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory](https://arxiv.org/abs/2608.29910) · 2026-08-30 · 引用 20 · 👍 18
- [Global Prior Meets Local Consistency: Dual-Memory Augmented Vision-Language-Action Model for Efficient Robotic Manipulation](https://arxiv.org/abs/2602.20200) · 2026-02-22 · 引用 27 · `CVPR 2026`
- [VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation](https://arxiv.org/abs/2606.07723) · 2026-06-05 · 引用 23 · 👍 6
- [Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory](https://arxiv.org/abs/2610.19366) · 2026-10-14 · 引用 0 · 👍 49
- [ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation](https://arxiv.org/abs/2607.08741) · 2026-07-09 · 引用 19 · 👍 10
- [Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](https://arxiv.org/abs/2606.23085) · 2026-06-22 · 引用 17 · 👍 12
- [Explore with Long-term Memory: A Benchmark and Multimodal LLM-based Reinforcement Learning Framework for Embodied Exploration](https://arxiv.org/abs/2601.10744) · 2026-01-11 · 引用 21 · `CVPR 2026`

<a id="10"></a>
### 10 · 足式运动控制（439 篇） · 长期清单 [papers/10-legged-locomotion.md](../papers/10-legged-locomotion.md)

- [GrandTour: A Legged Robotics Dataset in the Wild for Multi-Modal Perception and State Estimation](https://arxiv.org/abs/2602.18164) · 2026-02-20 · 引用 30
- [Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding](https://arxiv.org/abs/2601.08485) · 2026-01-13 · 引用 28 · `T-RO`
- [Deep Whole-body Parkour](https://arxiv.org/abs/2601.07701) · 2026-01-12 · 引用 16
- [OmniQuad: a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels](https://arxiv.org/abs/2610.38502) · 2026-10-28 · 引用 16
- [Whole-Brain Connectomic Graph Model Enables Whole-Body Locomotion Control in Fruit Fly](https://arxiv.org/abs/2602.17997) · 2026-02-20 · 引用 10
- [TERRA: Terrain-Aware Reconstruction, Retargeting and Control for Musculoskeletal Locomotion](https://arxiv.org/abs/2609.38653) · 2026-09-29 · 引用 0 · 👍 19
- [Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion](https://arxiv.org/abs/2602.00678) · 2026-01-31 · 引用 7 · `RSS`
- [TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour](https://arxiv.org/abs/2602.02331) · 2026-02-02 · 引用 7
- [Agile perceptive multi-skill locomotion for quadrupedal robots in the wild](https://arxiv.org/abs/2607.13579) · 2026-07-15 · 引用 7 · `Science Robotics`
- [Advances, challenges, and opportunities for legged robots](https://arxiv.org/abs/2607.28952) · 2026-07-31 · 引用 7 · `Science Robotics`
- [Rapid Embodiment Adaptation for Quadrupedal Locomotion](https://arxiv.org/abs/2608.01506) · 2026-08-02 · 引用 7
- [Learning Quadrupedal Locomotion for a Heavy Hydraulic Robot Using an Actuator Model](https://arxiv.org/abs/2601.11143) · 2026-01-16 · 引用 6 · `RA-L`
- [PUMA: Perception-driven Unified Foothold Prior for Mobility Augmented Quadruped Parkour](https://arxiv.org/abs/2601.15995) · 2026-01-22 · 引用 6
- [Scaling Rough Terrain Locomotion with Automatic Curriculum Reinforcement Learning](https://arxiv.org/abs/2601.17428) · 2026-01-24 · 引用 6
- [Attention-Based Neural-Augmented Kalman Filter for Legged Robot State Estimation](https://arxiv.org/abs/2601.18569) · 2026-01-26 · 引用 6 · `RA-L`
- [Gait Asymmetry from Unilateral Weakness and Improvement With Ankle Assistance: a Reinforcement Learning based Simulation Study](https://arxiv.org/abs/2602.18862) · 2026-02-21 · 引用 6
- [Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds](https://arxiv.org/abs/2607.18135) · 2026-07-20 · 引用 6 · `CASE`
- [Lunar Rover Cargo Transport: Mission Concept and Field Test](https://arxiv.org/abs/2601.03371) · 2026-01-06 · 引用 5
- [Efficiently Learning Robust Torque-based Locomotion Through Reinforcement with Model-Based Supervision](https://arxiv.org/abs/2601.16109) · 2026-01-22 · 引用 5
- [Learning-based Adaptive Control of Quadruped Robots for Active Stabilization on Moving Platforms](https://arxiv.org/abs/2602.03367) · 2026-02-03 · 引用 5 · `IROS`

<a id="11"></a>
### 11 · 人形机器人（626 篇） · 长期清单 [papers/11-humanoid.md](../papers/11-humanoid.md)

- [Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching](https://arxiv.org/abs/2602.15827) · 2026-02-17 · 引用 66
- [$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263) · 2026-03-12 · 引用 63
- [FlowAct-R1: Towards Interactive Humanoid Video Generation](https://arxiv.org/abs/2601.10103) · 2026-01-15 · 引用 10 · 👍 78
- [Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking](https://arxiv.org/abs/2606.03985) · 2026-06-02 · 引用 22 · 👍 41 · `CVPR 2026`
- [Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations](https://arxiv.org/abs/2602.06643) · 2026-02-06 · 引用 39
- [Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids](https://arxiv.org/abs/2601.07718) · 2026-01-12 · 引用 38
- [OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control](https://arxiv.org/abs/2602.23843) · 2026-02-27 · 引用 38
- [UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734) · 2026-04-21 · 引用 20 · 👍 31
- [HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos](https://arxiv.org/abs/2602.02473) · 2026-02-02 · 引用 35
- [TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control](https://arxiv.org/abs/2602.07439) · 2026-02-07 · 引用 35
- [Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking](https://arxiv.org/abs/2604.17335) · 2026-04-19 · 引用 33
- [ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control](https://arxiv.org/abs/2602.00401) · 2026-01-30 · 引用 31
- [RPL: Learning Robust Humanoid Perceptive Locomotion on Challenging Terrains](https://arxiv.org/abs/2602.03002) · 2026-02-03 · 引用 31
- [cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots](https://arxiv.org/abs/2603.05493) · 2026-03-05 · 引用 31
- [Learning Athletic Humanoid Tennis Skills from Imperfect Human Motion Data](https://arxiv.org/abs/2603.12686) · 2026-03-13 · 引用 28
- [ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2603.03279) · 2026-03-03 · 引用 26
- [ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control](https://arxiv.org/abs/2604.27711) · 2026-04-30 · 引用 5 · 👍 39
- [Reflex: Visually Grounded Reactive Humanoid Control](https://arxiv.org/abs/2610.12772) · 2026-10-08 · 引用 0 · 👍 47
- [Scaling Behavior Foundation Model for Humanoid Robots](https://arxiv.org/abs/2607.15163) · 2026-07-16 · 引用 22
- [Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot](https://arxiv.org/abs/2601.02078) · 2026-01-05 · 引用 20

<a id="12"></a>
### 12 · 操作、抓取与灵巧手（1428 篇） · 长期清单 [papers/12-manipulation-dexterous.md](../papers/12-manipulation-dexterous.md)

- [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](https://arxiv.org/abs/2602.16710) · 2026-02-18 · 引用 163
- [Qwen-RobotManip Technical Report: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](https://arxiv.org/abs/2606.17846) · 2026-06-16 · 引用 68 · 👍 33
- [mjlab: A Lightweight Framework for GPU-Accelerated Robot Learning](https://arxiv.org/abs/2601.22074) · 2026-01-29 · 引用 84
- [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046) · 2026-06-15 · 引用 22 · 👍 110
- [SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://arxiv.org/abs/2602.09153) · 2026-02-09 · 引用 68 · 👍 5 · `ICML 2026`
- [Learning from Fleet Experience: Collective Experience Learning Across 96 Robots](https://arxiv.org/abs/2610.25736) · 2026-10-19 · 引用 0 · 👍 111
- [Masked Depth Modeling for Spatial Perception](https://arxiv.org/abs/2601.17895) · 2026-01-25 · 引用 40 · 👍 30
- [In-the-Wild Compliant Manipulation with UMI-FT](https://arxiv.org/abs/2601.09988) · 2026-01-15 · 引用 54
- [DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo](https://arxiv.org/abs/2605.16257) · 2026-05-15 · 引用 23 · 👍 54
- [SimToolReal: An Object-Centric Policy for Zero-Shot Dexterous Tool Manipulation](https://arxiv.org/abs/2602.16863) · 2026-02-18 · 引用 39 · 👍 18
- [ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation](https://arxiv.org/abs/2603.15169) · 2026-03-16 · 引用 46 · `CVPR 2026`
- [HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone](https://arxiv.org/abs/2607.25895) · 2026-07-28 · 引用 15 · 👍 59
- [Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems](https://arxiv.org/abs/2611.05275) · 2026-11-03 · 引用 0 · 👍 86
- [PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572) · 2026-05-20 · 引用 14 · 👍 52
- [SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation](https://arxiv.org/abs/2606.28276) · 2026-06-26 · 引用 31 · 👍 15
- [Towards Generalizable Robotic Manipulation in Dynamic Environments](https://arxiv.org/abs/2603.15620) · 2026-03-16 · 引用 36 · 👍 3 · `ECCV 2026`
- [$χ_{0}$: Resource-Aware Robust Manipulation via Taming Distributional Inconsistencies](https://arxiv.org/abs/2602.09021) · 2026-02-09 · 引用 24 · 👍 20
- [MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation](https://arxiv.org/abs/2603.16861) · 2026-03-17 · 引用 29 · 👍 10
- [Do as I Do: Dexterous Manipulation Data from Everyday Human Videos](https://arxiv.org/abs/2606.19333) · 2026-06-17 · 引用 34
- [PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation](https://arxiv.org/abs/2606.28128) · 2026-06-26 · 引用 8 · 👍 51

<a id="13"></a>
### 13 · 触觉与接触感知（458 篇） · 长期清单 [papers/13-tactile.md](../papers/13-tactile.md)

- [VisuoTactile 6D Pose Estimation of an In-Hand Object using Vision and Tactile Sensor Data](https://arxiv.org/abs/2601.01675) · 2026-01-04 · 引用 72 · `RA-L`
- [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2603.19201) · 2026-03-19 · 引用 56
- [$N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens](https://arxiv.org/abs/2607.23782) · 2026-07-26 · 引用 15 · 👍 65
- [Dream-Tac: A Unified Tactile World Action Model for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2606.08737) · 2026-06-07 · 引用 42
- [UniVTAC: A Unified Simulation Platform for Visuo-Tactile Manipulation Data Generation, Learning, and Benchmarking](https://arxiv.org/abs/2602.10093) · 2026-02-10 · 引用 41
- [TacVLA: Contact-Aware Tactile Fusion for Robust Vision-Language-Action Manipulation](https://arxiv.org/abs/2603.12665) · 2026-03-13 · 引用 40
- [Visuo-Tactile World Models](https://arxiv.org/abs/2602.06001) · 2026-02-05 · 引用 36
- [T-Rex: Tactile-Reactive Dexterous Manipulation](https://arxiv.org/abs/2606.17055) · 2026-06-15 · 引用 35
- [AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception](https://arxiv.org/abs/2602.09617) · 2026-02-10 · 引用 34 · `ICLR 2026`
- [TaF-VLA: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation](https://arxiv.org/abs/2601.20321) · 2026-01-28 · 引用 32
- [FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation](https://arxiv.org/abs/2606.13102) · 2026-06-11 · 引用 29
- [$N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2607.23783) · 2026-07-26 · 引用 6 · 👍 46
- [VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs](https://arxiv.org/abs/2603.23481) · 2026-03-24 · 引用 23 · 👍 7
- [HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing](https://arxiv.org/abs/2603.15257) · 2026-03-16 · 引用 26
- [TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation](https://arxiv.org/abs/2606.11184) · 2026-06-09 · 引用 26
- [TouchGuide: Inference-Time Steering of Visuomotor Policies via Touch Guidance](https://arxiv.org/abs/2601.20239) · 2026-01-28 · 引用 24
- [TactAlign: Human-to-Robot Policy Transfer via Tactile Alignment](https://arxiv.org/abs/2602.13579) · 2026-02-14 · 引用 18 · 👍 11
- [AT-VLA: Adaptive Tactile Injection for Enhanced Feedback Reaction in Vision-Language-Action Models](https://arxiv.org/abs/2605.07308) · 2026-05-08 · 引用 23
- [FlexiTac: A Low-Cost, Open-Source, Scalable Tactile Sensing Solution for Robotic Systems](https://arxiv.org/abs/2604.28156) · 2026-04-30 · 引用 22
- [VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2607.02503) · 2026-07-02 · 引用 22

<a id="14"></a>
### 14 · 具身导航与移动操作（943 篇） · 长期清单 [papers/14-navigation.md](../papers/14-navigation.md)

- [ABot-N1: Toward a General Visual Language Navigation Foundation Model](https://arxiv.org/abs/2607.10383) · 2026-07-11 · 引用 11 · 👍 83
- [HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations](https://arxiv.org/abs/2603.03243) · 2026-03-03 · 引用 41
- [SuperNav: An Agentic Navigation System for Any Task in Any Scene](https://arxiv.org/abs/2610.12126) · 2026-10-08 · 引用 1 · 👍 77
- [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112) · 2026-06-16 · 引用 23 · 👍 30
- [MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation](https://arxiv.org/abs/2602.11337) · 2026-02-11 · 引用 33 · 👍 9
- [Sparse Video Generation Propels Real-World Beyond-the-View Vision-Language Navigation](https://arxiv.org/abs/2602.05827) · 2026-02-05 · 引用 17 · 👍 17
- [Hierarchical Semantic-Augmented Navigation: Optimal Transport and Graph-Driven Reasoning for Vision-Language Navigation](https://arxiv.org/abs/2606.01565) · 2026-06-01 · 引用 25 · `NeurIPS 2025`
- [ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation](https://arxiv.org/abs/2610.25690) · 2026-10-19 · 引用 0 · 👍 38
- [Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting](https://arxiv.org/abs/2604.12626) · 2026-04-14 · 引用 10 · 👍 16 · `ECCV 2026`
- [MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives](https://arxiv.org/abs/2604.24833) · 2026-04-27 · 引用 18
- [FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation](https://arxiv.org/abs/2601.13976) · 2026-01-20 · 引用 6 · 👍 22
- [NavDreamer: Video Models as Zero-Shot 3D Navigators](https://arxiv.org/abs/2602.09765) · 2026-02-10 · 引用 17
- [Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation](https://arxiv.org/abs/2608.17512) · 2026-08-18 · 引用 1 · 👍 32
- [PanoVLN: Towards Effective Panoramic Vision-and-Language Navigation](https://arxiv.org/abs/2609.34759) · 2026-09-28 · 引用 0 · 👍 33
- [PlannerRFT: Reinforcing Diffusion Planners through Closed-Loop and Sample-Efficient Fine-Tuning](https://arxiv.org/abs/2601.12901) · 2026-01-19 · 引用 16
- [Language-Conditioned World Modeling for Visual Navigation](https://arxiv.org/abs/2603.26741) · 2026-03-23 · 引用 16 · `NeurIPS 2026`
- [SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation](https://arxiv.org/abs/2601.06806) · 2026-01-11 · 引用 15
- [AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation](https://arxiv.org/abs/2605.22816) · 2026-05-21 · 引用 15 · `CVPR 2026`
- [OmniEcho: Audio-Visual Spatial Understanding for Omni-Modal Embodied Agents](https://arxiv.org/abs/2609.23407) · 2026-09-20 · 引用 2 · 👍 26
- [Three-Step Nav: A Hierarchical Global-Local Planner for Zero-Shot Vision-and-Language Navigation](https://arxiv.org/abs/2604.26946) · 2026-04-29 · 引用 13

<a id="15"></a>
### 15 · 视觉表征与 3D 场景理解（423 篇） · 长期清单 [papers/15-perception-representation.md](../papers/15-perception-representation.md)

- [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482) · 2026-03-15 · 引用 160 · 👍 40
- [Utonia: Toward One Encoder for All Point Clouds](https://arxiv.org/abs/2603.03283) · 2026-03-03 · 引用 39 · 👍 174
- [ABot-Earth 0.5: Generative 3D Earth Model](https://arxiv.org/abs/2606.09967) · 2026-06-08 · 引用 2 · 👍 139
- [Generation Models Know Space: Unleashing Implicit 3D Priors for Scene Understanding](https://arxiv.org/abs/2603.19235) · 2026-03-19 · 引用 15 · 👍 57 · `ECCV 2026`
- [Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling](https://arxiv.org/abs/2608.30821) · 2026-08-31 · 引用 5 · 👍 64
- [3D Scene Graphs: Open Challenges and Future Directions](https://arxiv.org/abs/2606.19383) · 2026-06-15 · 引用 11
- [Conflict-Aware Active Perception and Control in 3D Gaussian Splatting Fields via Control Barrier Functions](https://arxiv.org/abs/2605.20566) · 2026-05-19 · 引用 7
- [How to Relieve Distribution Shifts in Semantic Segmentation for Off-Road Environments](https://arxiv.org/abs/2605.29599) · 2026-05-28 · 引用 7 · `RA-L`
- [Uncertainty-driven 3D Gaussian Splatting Active Mapping via Anisotropic Visibility Field](https://arxiv.org/abs/2605.30342) · 2026-05-28 · 引用 7 · `CVPR 2026`
- [RAG-3DSG: Enhancing 3D Scene Graphs with Re-Shot Guided Retrieval-Augmented Generation](https://arxiv.org/abs/2601.10168) · 2026-01-15 · 引用 6 · `ECCV`
- [Generative Event Pretraining with Foundation Model Alignment](https://arxiv.org/abs/2603.23032) · 2026-03-24 · 引用 6 · `CVPR 2026`
- [Pandora: Articulated 3D Scene Graphs from Egocentric Vision](https://arxiv.org/abs/2603.28732) · 2026-03-30 · 引用 6
- [FOUND-IT: Foundation-model-first Task-driven 3D Scene Graphs with Granularity on Demand](https://arxiv.org/abs/2605.25371) · 2026-05-25 · 引用 6
- [SM4RT: Learning Structured Motion Geometry for 4D Reconstruction](https://arxiv.org/abs/2607.22534) · 2026-07-24 · 引用 6
- [Singularity Analysis for the Perspective-Four and Five-Line Problems](https://arxiv.org/abs/2609.29417) · 2026-09-24 · 引用 6
- [VG3S: Visual Geometry Grounded Gaussian Splatting for Semantic Occupancy Prediction](https://arxiv.org/abs/2603.06210) · 2026-03-06 · 引用 5 · `IROS 2026`
- [Panoramic Affordance Prediction](https://arxiv.org/abs/2603.15558) · 2026-03-16 · 引用 0 · 👍 10
- [Efficient Onboard Spacecraft Pose Estimation with Event Cameras and Neuromorphic Hardware](https://arxiv.org/abs/2604.04117) · 2026-04-05 · 引用 5
- [Learning to Identify Out-of-Distribution Objects for 3D LiDAR Anomaly Segmentation](https://arxiv.org/abs/2604.23604) · 2026-04-26 · 引用 2 · 👍 6 · `CVPR`
- [Temporally Consistent Object 6D Pose Estimation for Robot Control](https://arxiv.org/abs/2605.02708) · 2026-05-04 · 引用 5

<a id="16"></a>
### 16 · 数据采集、遥操作与人类视频（451 篇） · 长期清单 [papers/16-data-teleoperation.md](../papers/16-data-teleoperation.md)

- [LeRobot: An Open-Source Library for End-to-End Robot Learning](https://arxiv.org/abs/2602.22818) · 2026-02-26 · 引用 132
- [EgoVerse: An Egocentric Human Dataset for Robot Learning from Around the World](https://arxiv.org/abs/2604.07607) · 2026-04-08 · 引用 96
- [SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://arxiv.org/abs/2602.10116) · 2026-02-10 · 引用 76 · 👍 14
- [EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106) · 2026-02-10 · 引用 50 · 👍 23
- [Kimodo: Scaling Controllable Human Motion Generation](https://arxiv.org/abs/2603.15546) · 2026-03-16 · 引用 61
- [Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning](https://arxiv.org/abs/2607.14183) · 2026-07-15 · 引用 7 · 👍 64
- [UniDex: A Robot Foundation Suite for Universal Dexterous Hand Control from Egocentric Human Videos](https://arxiv.org/abs/2603.22264) · 2026-03-23 · 引用 36 · `CVPR 2026`
- [HumanNet: Scaling Human-centric Video Learning to One Million Hours](https://arxiv.org/abs/2605.06747) · 2026-05-07 · 引用 9 · 👍 53
- [EgoSim: Egocentric World Simulator for Embodied Interaction Generation](https://arxiv.org/abs/2604.01001) · 2026-04-01 · 引用 15 · 👍 30
- [RoboPocket: Improve Robot Policies Instantly with Your Phone](https://arxiv.org/abs/2603.05504) · 2026-03-05 · 引用 12 · 👍 34 · `CoRL 2026`
- [Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://arxiv.org/abs/2608.02580) · 2026-08-03 · 引用 18 · 👍 21
- [PhysForge: Generating Physics-Grounded 3D Assets for Interactive Virtual World](https://arxiv.org/abs/2605.05163) · 2026-05-06 · 引用 10 · 👍 36 · `ICML 2026`
- [HumanEgo: Zero-Shot Robot Learning from Minutes of Human Egocentric Videos](https://arxiv.org/abs/2605.24934) · 2026-05-24 · 引用 25
- [ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine](https://arxiv.org/abs/2607.28625) · 2026-07-30 · 引用 3 · 👍 43
- [EgoLive: A Large-Scale Egocentric Dataset from Real-World Human Tasks](https://arxiv.org/abs/2604.23570) · 2026-04-26 · 引用 23
- [MA-EgoQA: Question Answering over Egocentric Videos from Multiple Embodied Agents](https://arxiv.org/abs/2603.09827) · 2026-03-10 · 引用 7 · 👍 30
- [ConLA: Contrastive Latent Action Learning from Human Videos for Robotic Manipulation](https://arxiv.org/abs/2602.00557) · 2026-01-31 · 引用 21
- [GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed](https://arxiv.org/abs/2609.39600) · 2026-09-30 · 引用 5 · 👍 31
- [Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics](https://arxiv.org/abs/2604.21017) · 2026-04-22 · 引用 17
- [EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations](https://arxiv.org/abs/2606.12604) · 2026-06-10 · 引用 15

<a id="17"></a>
### 17 · 仿真、Sim2Real 与评测基准（418 篇） · 长期清单 [papers/17-simulation-benchmarks.md](../papers/17-simulation-benchmarks.md)

- [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots](https://arxiv.org/abs/2603.04356) · 2026-03-04 · 引用 165
- [RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies](https://arxiv.org/abs/2607.04434) · 2026-07-05 · 引用 90 · 👍 15
- [RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies](https://arxiv.org/abs/2604.09860) · 2026-04-10 · 引用 55 · 👍 8
- [Interactive World Simulator for Robot Policy Training and Evaluation](https://arxiv.org/abs/2603.08546) · 2026-03-09 · 引用 52
- [ComBodied Agents: a New Paradigm of Human-Centric Agentic AI](https://arxiv.org/abs/2608.10915) · 2026-08-11 · 引用 6 · 👍 92
- [Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669) · 2026-03-17 · 引用 16 · 👍 47
- [Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698) · 2026-10-20 · 引用 0 · 👍 71
- [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](https://arxiv.org/abs/2604.11689) · 2026-04-13 · 引用 16 · 👍 21
- [HSImul3R: Physics-in-the-Loop Reconstruction of Simulation-Ready Human-Scene Interactions](https://arxiv.org/abs/2603.15612) · 2026-03-16 · 引用 3 · 👍 44
- [ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs](https://arxiv.org/abs/2609.10895) · 2026-09-09 · 引用 1 · 👍 46
- [Advances in Global Solvers for 3D Vision](https://arxiv.org/abs/2602.14662) · 2026-02-16 · 引用 19
- [NVIDIA Isaac Sim: Enabling Scalable, GPU-Accelerated Simulation for Robotics](https://arxiv.org/abs/2606.03551) · 2026-06-02 · 引用 19
- [RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments](https://arxiv.org/abs/2610.10409) · 2026-10-07 · 引用 2 · 👍 34
- [GameplayQA: A Benchmarking Framework for Decision-Dense POV-Synced Multi-Video Understanding of 3D Virtual Agents](https://arxiv.org/abs/2603.24329) · 2026-03-25 · 引用 3 · 👍 23 · `ACL 2026`
- [MATTERIX: toward a digital twin for robotics-assisted chemistry laboratory automation](https://arxiv.org/abs/2601.13232) · 2026-01-19 · 引用 14
- [Solving Physics Olympiad via Reinforcement Learning on Physics Simulators](https://arxiv.org/abs/2604.11805) · 2026-04-13 · 引用 6 · 👍 16
- [Text-to-CAD Evaluation with CADTests](https://arxiv.org/abs/2605.07807) · 2026-05-08 · 引用 14
- [What Are We Actually Benchmarking in Robot Manipulation?](https://arxiv.org/abs/2606.04233) · 2026-06-02 · 引用 14
- [DeFM: Learning Foundation Representations from Depth for Robotics](https://arxiv.org/abs/2601.18923) · 2026-01-26 · 引用 11 · 👍 4 · `T-RO`
- [Does LeWorldModel Preserve Local Action Geometry?](https://arxiv.org/abs/2610.31716) · 2026-10-22 · 引用 0 · 👍 26 · `NeurIPS 2026`

<a id="18"></a>
### 18 · 综述与教程（109 篇） · 长期清单 [papers/18-surveys.md](../papers/18-surveys.md)

- [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080) · 2026-04-30 · 引用 56 · 👍 16
- [Progress Reward Modeling for Robotic Learning: A Comprehensive Survey](https://arxiv.org/abs/2607.21655) · 2026-07-22 · 引用 6 · 👍 78
- [World Action Models: A Survey](https://arxiv.org/abs/2606.20781) · 2026-06-18 · 引用 13 · 👍 58
- [GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation](https://arxiv.org/abs/2607.02642) · 2026-07-02 · 引用 16 · 👍 37
- [GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation](https://arxiv.org/abs/2605.27491) · 2026-05-26 · 引用 19 · 👍 15
- [Data Pyramid for Embodied Manipulation: A Survey](https://arxiv.org/abs/2607.24744) · 2026-07-27 · 引用 9 · 👍 34
- [Embodied Foundation Models at the Edge: A Survey of Deployment Constraints and Mitigation Strategies](https://arxiv.org/abs/2603.16952) · 2026-03-16 · 引用 13
- [Robotic Video World Models: A Survey of Applications, Research Challenges, Future Directions](https://arxiv.org/abs/2601.07823) · 2026-01-12 · 引用 11
- [Vision-and-Language Navigation for UAVs: Progress, Challenges, and a Research Roadmap](https://arxiv.org/abs/2604.13654) · 2026-04-15 · 引用 10
- [Backup-Based Safety Filters: A Comparative Review of Backup CBF, Model Predictive Shielding, and gatekeeper](https://arxiv.org/abs/2604.02401) · 2026-04-02 · 引用 9
- [Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines](https://arxiv.org/abs/2604.23001) · 2026-04-24 · 引用 9
- [From Human Videos to Robot Manipulation: A Survey on Scalable Vision-Language-Action Learning with Human-Centric Data](https://arxiv.org/abs/2606.00054) · 2026-05-18 · 引用 9 · `IJCAI 2026`
- [Robot Learning from Human Videos: A Survey](https://arxiv.org/abs/2604.27621) · 2026-04-30 · 引用 8
- [A Comprehensive Review of Generative Physical Artificial Intelligence](https://arxiv.org/abs/2609.18111) · 2026-09-16 · 引用 8
- [A Comprehensive Review of Bio-Inspired Approaches to Coordination, Communication, and System Architecture in Underwater Swarm Robotics](https://arxiv.org/abs/2601.12244) · 2026-01-18 · 引用 7
- [How Do We Research Human-Robot Interaction in the Age of Large Language Models? A Systematic Review](https://arxiv.org/abs/2602.15063) · 2026-02-13 · 引用 7
- [Large Language Model-Assisted UAV Operations and Communications: A Multifaceted Survey and Tutorial](https://arxiv.org/abs/2602.19534) · 2026-02-23 · 引用 7
- [From Shallow Waters to Mariana Trench: A Survey of Bio-inspired Underwater Soft Robots](https://arxiv.org/abs/2601.12353) · 2026-01-18 · 引用 6
- [Is Your Safe Controller Actually Safe? A Critical Review of CBF Tautologies and Hidden Assumptions](https://arxiv.org/abs/2603.06954) · 2026-03-07 · 引用 6
- [Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses](https://arxiv.org/abs/2605.02900) · 2026-03-28 · 引用 6

<a id="19"></a>
### 19 · 自动驾驶（811 篇）

- [Driving on Registers](https://arxiv.org/abs/2601.05083) · 2026-01-08 · 引用 64
- [DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving](https://arxiv.org/abs/2602.06521) · 2026-02-06 · 引用 44
- [UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving](https://arxiv.org/abs/2604.02190) · 2026-04-02 · 引用 20 · 👍 25
- [LaST-VLA: Thinking in Latent Spatio-Temporal Space for Vision-Language-Action in Autonomous Driving](https://arxiv.org/abs/2603.01928) · 2026-03-02 · 引用 31
- [Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures](https://arxiv.org/abs/2603.01063) · 2026-03-01 · 引用 30
- [DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving](https://arxiv.org/abs/2601.01528) · 2026-01-04 · 引用 21 · 👍 16
- [NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159) · 2026-06-02 · 引用 18 · 👍 21
- [DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving](https://arxiv.org/abs/2602.14577) · 2026-02-16 · 引用 24
- [Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.24581) · 2026-03-25 · 引用 24
- [Fail2Drive: Benchmarking Closed-Loop Driving Generalization](https://arxiv.org/abs/2604.08535) · 2026-04-09 · 引用 24
- [Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs](https://arxiv.org/abs/2608.01755) · 2026-08-03 · 引用 5 · 👍 33
- [CoordLight: Learning Decentralized Coordination for Network-Wide Traffic Signal Control](https://arxiv.org/abs/2603.24366) · 2026-03-25 · 引用 21
- [MeanFuser: Fast One-Step Multi-Modal Trajectory Generation and Adaptive Reconstruction via MeanFlow for End-to-End Autonomous Driving](https://arxiv.org/abs/2602.20060) · 2026-02-23 · 引用 19 · `CVPR 2026`
- [Devil is in Narrow Policy: Unleashing Exploration in Driving VLA Models](https://arxiv.org/abs/2603.06049) · 2026-03-06 · 引用 19
- [DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587) · 2026-03-25 · 引用 18
- [ExploreVLA: Dense World Modeling and Exploration for End-to-End Autonomous Driving](https://arxiv.org/abs/2604.02714) · 2026-04-03 · 引用 18 · `ECCV 2026`
- [DVGT-2: Vision-Geometry-Action Model for Autonomous Driving at Scale](https://arxiv.org/abs/2604.00813) · 2026-04-01 · 引用 17
- [DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving](https://arxiv.org/abs/2603.11041) · 2026-03-11 · 引用 16
- [Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving](https://arxiv.org/abs/2605.23163) · 2026-05-22 · 引用 7 · 👍 16
- [Boreas Road Trip: A Multi-Sensor Autonomous Driving Dataset on Challenging Roads](https://arxiv.org/abs/2602.16870) · 2026-02-18 · 引用 14 · `IJRR`

<a id="20"></a>
### 20 · 空中、水下与空间机器人（908 篇）

- [AirBender: Adaptive Transportation of Bendable Objects Using Dual UAVs](https://arxiv.org/abs/2605.07003) · 2026-05-07 · 引用 51
- [CARLA-Air: Fly Drones Inside a CARLA World -- A Unified Infrastructure for Air-Ground Embodied Intelligence](https://arxiv.org/abs/2603.28032) · 2026-03-30 · 引用 7 · 👍 39
- [Precise Aggressive Aerial Maneuvers with Sensorimotor Policies](https://arxiv.org/abs/2604.05828) · 2026-04-07 · 引用 13
- [Agentic AI Meets Edge Computing in Autonomous UAV Swarms](https://arxiv.org/abs/2601.14437) · 2026-01-20 · 引用 11
- [AUV Trajectory Learning for Underwater Acoustic Energy Transfer and Age Minimization](https://arxiv.org/abs/2601.08491) · 2026-01-13 · 引用 8
- [ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments](https://arxiv.org/abs/2603.03198) · 2026-03-03 · 引用 8
- [Learn Structure, Adapt on the Fly: Multi-Scale Residual Learning and Online Adaptation for Aerial Manipulators](https://arxiv.org/abs/2603.11638) · 2026-03-12 · 引用 8
- [AeroGrab: A Unified Framework for Aerial Grasping in Cluttered Environments](https://arxiv.org/abs/2603.15097) · 2026-03-16 · 引用 8
- [ESARBench: A Benchmark for Agentic UAV Embodied Search and Rescue](https://arxiv.org/abs/2605.01371) · 2026-05-02 · 引用 5 · 👍 5
- [Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied Intelligence](https://arxiv.org/abs/2607.12477) · 2026-07-14 · 引用 5 · 👍 5
- [AirHunt: Bridging VLM Semantics and Continuous Planning for Efficient Aerial Object Navigation](https://arxiv.org/abs/2601.12742) · 2026-01-19 · 引用 7
- [MonoRace: Winning Champion-Level Drone Racing with Robust Monocular AI](https://arxiv.org/abs/2601.15222) · 2026-01-21 · 引用 7
- [Learning Agile Quadrotor Flight in the Real World](https://arxiv.org/abs/2602.10111) · 2026-02-10 · 引用 7
- [AeroPlace-Flow: Language-Grounded Object Placement for Aerial Manipulators via Visual Foresight and Object Flow](https://arxiv.org/abs/2603.07744) · 2026-03-08 · 引用 7
- [SAGA: A Robust Self-Attention and Goal-Aware Anchor-based Planner for Safe UAV Autonomous Navigation](https://arxiv.org/abs/2605.02301) · 2026-05-04 · 引用 7
- [Above and Below: Heterogeneous Multi-robot SLAM Across Surface and Underwater Domains](https://arxiv.org/abs/2605.09811) · 2026-05-10 · 引用 7
- [Learning Cross-Coupled and Regime Dependent Dynamics for Aerial Manipulation](https://arxiv.org/abs/2605.14805) · 2026-05-14 · 引用 7
- [USS-Nav: Unified Spatio-Semantic Scene Graph for Lightweight UAV Zero-Shot Object Navigation](https://arxiv.org/abs/2602.00708) · 2026-01-31 · 引用 6
- [Muscle Coactivation in the Sky: Geometry and Pareto Optimality of Energy vs. Aerodynamic Promptness and Multirotors as Variable Stiffness Actuators](https://arxiv.org/abs/2602.14222) · 2026-02-15 · 引用 6
- [Swooper: Learning High-Speed Aerial Grasping With a Simple Gripper](https://arxiv.org/abs/2603.05935) · 2026-03-06 · 引用 6

<a id="21"></a>
### 21 · SLAM、定位与建图（802 篇）

- [LocateAnything: Fast and High-Quality Vision-Language Grounding with Parallel Box Decoding](https://arxiv.org/abs/2605.27365) · 2026-05-26 · 引用 37 · 👍 142
- [Edge-Assisted Multi-Robot Visual-Inertial SLAM with Efficient Communication](https://arxiv.org/abs/2603.11085) · 2026-03-11 · 引用 69
- [VGGT-SLAM 2.0: Real-time Dense Feed-forward Scene Reconstruction](https://arxiv.org/abs/2601.19887) · 2026-01-27 · 引用 50
- [SUPER ODOMETRY 2.0: Resilient Odometry via Hierarchical Adaptation](https://arxiv.org/abs/2608.25427) · 2026-08-26 · 引用 18 · `Science Robotics 2025`
- [DROID-SLAM in the Wild](https://arxiv.org/abs/2603.19076) · 2026-03-19 · 引用 14 · 👍 4
- [When the Inference Meets the Explicitness or Why Multimodality Can Make Us Forget About the Perfect Predictor](https://arxiv.org/abs/2602.18850) · 2026-02-21 · 引用 8
- [WildCross: A Cross-Modal Large Scale Benchmark for Place Recognition and Metric Depth Estimation in Natural Environments](https://arxiv.org/abs/2603.01475) · 2026-03-02 · 引用 7
- [Evolving Skill Modules under a Fixed Planner: Versioning, Rollback, and Runtime Governance for Long-Lived Robot Systems](https://arxiv.org/abs/2604.07799) · 2026-04-09 · 引用 7
- [SuperMap: A Spatio-Temporal SLAM System for Visual-Language Navigation](https://arxiv.org/abs/2608.22896) · 2026-08-24 · 引用 7 · `RSS 2026`
- [Distributed Relative Localization Based on Ultra-WideBand and LiDAR for Multi-robot with Limited Communication](https://arxiv.org/abs/2610.11141) · 2026-10-08 · 引用 7
- [Chamelion: Reliable Change Detection for Long-Term LiDAR Mapping in Transient Environments](https://arxiv.org/abs/2602.08189) · 2026-02-09 · 引用 6
- [AdaptManip: Learning Adaptive Whole-Body Object Lifting and Delivery with Online Recurrent State Estimation](https://arxiv.org/abs/2602.14363) · 2026-02-16 · 引用 6
- [Dream-SLAM: Dreaming the Unseen for Active SLAM in Dynamic Environments](https://arxiv.org/abs/2602.21967) · 2026-02-25 · 引用 6
- [Full Stack Navigation, Mapping, and Planning for the Lunar Autonomy Challenge](https://arxiv.org/abs/2603.17232) · 2026-03-18 · 引用 6
- [3-D Relative Localization for Multi-Robot Systems with Angle and Self-Displacement Measurements](https://arxiv.org/abs/2604.01703) · 2026-04-02 · 引用 6
- [Free-Init: Scan-Free, Motion-Free, and Correspondence-Free Initialization for Doppler LiDAR-Inertial Systems](https://arxiv.org/abs/2609.29375) · 2026-09-24 · 引用 6 · `RA-L`
- [R-VoxelMap: Accurate Voxel Mapping with Recursive Plane Fitting for Online LiDAR Odometry](https://arxiv.org/abs/2601.12377) · 2026-01-18 · 引用 5
- [MAGICIAN: Efficient Long-Term Planning with Imagined Gaussians for Active Mapping](https://arxiv.org/abs/2603.22650) · 2026-03-23 · 引用 5 · `CVPR 2026`
- [VBGS-SLAM: Variational Bayesian Gaussian Splatting Simultaneous Localization and Mapping](https://arxiv.org/abs/2604.02696) · 2026-04-03 · 引用 5
- [Flash-Mono: Feed-Forward Accelerated Gaussian Splatting Monocular SLAM](https://arxiv.org/abs/2604.03092) · 2026-04-03 · 引用 5

<a id="22"></a>
### 22 · 运动规划与控制（874 篇）

- [Safety Beyond the Training Data: Robust Out-of-Distribution MPC via Conformalized System Level Synthesis](https://arxiv.org/abs/2602.12047) · 2026-02-12 · 引用 14
- [Safe Large-Scale Robust Nonlinear MPC in Milliseconds via Reachability-Constrained System Level Synthesis on the GPU](https://arxiv.org/abs/2604.07644) · 2026-04-08 · 引用 12
- [First-order friction models with bristle dynamics: lumped and distributed formulations](https://arxiv.org/abs/2602.09429) · 2026-02-10 · 引用 10
- [Bellman Value Decomposition for Task Logic in Safe Optimal Control](https://arxiv.org/abs/2602.19532) · 2026-02-23 · 引用 8
- [Mind the Gap: Promises and Pitfalls of Hierarchical Planning in LeWorldModel](https://arxiv.org/abs/2607.12547) · 2026-07-14 · 引用 8
- [Just in time Informed Trees: Manipulability-Aware Asymptotically Optimized Motion Planning](https://arxiv.org/abs/2601.19972) · 2026-01-27 · 引用 7
- [Priority-Aware Multi-Robot Coverage Path Planning](https://arxiv.org/abs/2601.00580) · 2026-01-02 · 引用 6
- [Self-Organizing Dual-Buffer Adaptive Clustering Experience Replay (SODACER) for Safe Reinforcement Learning in Optimal Control](https://arxiv.org/abs/2601.06540) · 2026-01-10 · 引用 6
- [Geometry-Aware Sampling-Based Motion Planning on Riemannian Manifolds](https://arxiv.org/abs/2602.00992) · 2026-02-01 · 引用 6 · `WAFR`
- [Smooth trajectory generation and hybrid B-splines-Quaternions based tool path interpolation for a 3T1R parallel kinematic milling robot](https://arxiv.org/abs/2602.16758) · 2026-02-18 · 引用 6
- [Layered Safety: Enhancing Autonomous Collision Avoidance via Multistage CBF Safety Filters](https://arxiv.org/abs/2603.00338) · 2026-02-27 · 引用 6
- [Toward Interaction Dynamics: A Predictive Framework for Safe Physical Human Robot Interaction](https://arxiv.org/abs/2606.08281) · 2026-06-06 · 引用 6
- [TurboMPC: Fast, Scalable, and Differentiable Model Predictive Control on the GPU](https://arxiv.org/abs/2606.24039) · 2026-06-23 · 引用 6
- [Warm-Starting Collision-Free Model Predictive Control With Object-Centric Diffusion](https://arxiv.org/abs/2601.02873) · 2026-01-06 · 引用 5
- [Consensus-based optimization (CBO): Towards Global Optimality in Robotics](https://arxiv.org/abs/2602.06868) · 2026-02-06 · 引用 5
- [LILAC: Language-Conditioned Object-Centric Optical Flow for Open-Loop Trajectory Generation](https://arxiv.org/abs/2603.25481) · 2026-03-26 · 引用 5 · `RA-L`
- [Vectorizing Projection in Manifold-Constrained Motion Planning for Real-Time Whole-Body Control](https://arxiv.org/abs/2604.13323) · 2026-04-14 · 引用 5
- [Admissibility-Preserving Control for Strict-Feedback Nonlinear Systems with Asymmetric Actuator Constraints](https://arxiv.org/abs/2608.15375) · 2026-08-15 · 引用 5
- [Strict Modes Everywhere - Bringing Order Into Dynamics of Mechanical Systems by a Potential Compatible With the Geodesic Flow](https://arxiv.org/abs/2609.04817) · 2026-09-04 · 引用 5
- [A Fast Semidefinite Convex Relaxation for Optimal Control Problems With Spatio-Temporal Constraints](https://arxiv.org/abs/2601.03055) · 2026-01-06 · 引用 4

<a id="23"></a>
### 23 · 多机器人与人机交互（560 篇）

- [Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players](https://arxiv.org/abs/2605.28816) · 2026-05-27 · 引用 19 · 👍 95
- [Heterogeneous Policy Networks for Composite Robot Team Communication and Coordination](https://arxiv.org/abs/2606.20962) · 2026-06-18 · 引用 13
- [Estimating Trust in Human-Robot Collaboration through Behavioral Indicators and Explainability](https://arxiv.org/abs/2601.19856) · 2026-01-27 · 引用 9
- [Engagement Is Not Transfer: A Withdrawal Study of a Consumer Social Robot with Autistic Children at Home](https://arxiv.org/abs/2604.02642) · 2026-04-03 · 引用 9
- [A sequential explanatory mixed-methods study on the acceptance of a social robot for EFL speaking practice among Chinese primary school students: Insights from the Computers Are Social Actors (CASA) paradigm](https://arxiv.org/abs/2604.12789) · 2026-04-14 · 引用 7
- [Knowledge-Based Design Requirements for Generative Social Robots in Higher Education](https://arxiv.org/abs/2602.12873) · 2026-02-13 · 引用 6
- [Designing Robots for Families: In-Situ Prototyping for Contextual Reminders on Family Routines](https://arxiv.org/abs/2602.22628) · 2026-02-26 · 引用 6 · `HRI 2026`
- [Walking with Robots: Video Analysis of Human-Robot Interactions in Transit Spaces](https://arxiv.org/abs/2602.23475) · 2026-02-26 · 引用 6
- [PhysAgent: Automating Physics-Based 4D Synthesis via Trajectory-Grounded Multi-Agent Feedback](https://arxiv.org/abs/2606.08688) · 2026-06-07 · 引用 6
- [Optimal Transport-Based Decentralized Multi-Agent Distribution Matching](https://arxiv.org/abs/2601.00548) · 2026-01-02 · 引用 5
- [KGLAMP: Knowledge Graph-guided Language model for Adaptive Multi-robot Planning and Replanning](https://arxiv.org/abs/2602.04129) · 2026-02-04 · 引用 5
- ["Hello, I'm Delivering. Let Me Pass By": Navigating Public Pathways with Walk-along with Robots in Crowded City Streets](https://arxiv.org/abs/2602.16861) · 2026-02-18 · 引用 5
- [Age-Related Differences in the Perception of Eye-Gaze from a Social Robot](https://arxiv.org/abs/2603.08810) · 2026-03-09 · 引用 5
- [DiSCo: Diffusion Sequence Copilots for Shared Autonomy](https://arxiv.org/abs/2603.22787) · 2026-03-24 · 引用 5 · `HRI 2026`
- [Reimagining Social Robots as Recommender Systems: Foundations, Framework, and Applications](https://arxiv.org/abs/2601.19761) · 2026-01-27 · 引用 4
- [A Distributed Multi-Modal Sensing Approach for Human Activity Recognition in Real-Time Human-Robot Collaboration](https://arxiv.org/abs/2602.07024) · 2026-02-02 · 引用 4
- [Designing Social Robots with Ethical, User-Adaptive Explainability in the Era of Foundation Models](https://arxiv.org/abs/2603.00102) · 2026-02-17 · 引用 4
- [ParkDiffusion++: Ego Intention Conditioned Joint Multi-Agent Trajectory Prediction for Automated Parking using Diffusion Models](https://arxiv.org/abs/2602.20923) · 2026-02-24 · 引用 4 · `ICRA 2026`
- [Occlusion-Based Object Transportation Around Obstacles With a Swarm of Miniature Robots](https://arxiv.org/abs/2605.13006) · 2026-05-13 · 引用 4
- [PACT: Proactive Asking for Continual Task Assistance in Human-Robot Collaboration](https://arxiv.org/abs/2605.24350) · 2026-05-23 · 引用 4

<a id="24"></a>
### 24 · 医疗、软体与特种机器人（441 篇）

- [Exo-Plore: Exploring Exoskeleton Control Space through Human-aligned Simulation](https://arxiv.org/abs/2601.22550) · 2026-01-30 · 引用 13 · `ICLR 2026`
- [Learning Hip Exoskeleton Control Policy via Predictive Neuromusculoskeletal Simulation](https://arxiv.org/abs/2603.04166) · 2026-03-04 · 引用 13
- [DexEXO: A Wearability-First Dexterous Exoskeleton for Operator-Agnostic Demonstration and Learning](https://arxiv.org/abs/2603.17323) · 2026-03-18 · 引用 12
- [SRL Proxemics: Spatial Guidelines for Supernumerary Robotic Limbs in Near-Body Interactions](https://arxiv.org/abs/2602.00494) · 2026-01-31 · 引用 6
- [WHED: A Wearable Hand Exoskeleton for Natural, High-Quality Demonstration Collection](https://arxiv.org/abs/2602.17908) · 2026-02-20 · 引用 6
- [SMAT: Staged Multi-Agent Training for Co-Adaptive Exoskeleton Control](https://arxiv.org/abs/2603.07618) · 2026-03-08 · 引用 6 · `IROS 2026`
- [Universal Manipulation Exoskeleton: Learning Compliant Whole-body Policies with Real-time Torque Feedback](https://arxiv.org/abs/2606.14218) · 2026-06-12 · 引用 6
- [Continuum Robot State Estimation with Actuation Uncertainty](https://arxiv.org/abs/2601.04493) · 2026-01-08 · 引用 5 · `RA-L`
- [Systematic Evaluation of Hip Exoskeleton Assistance Parameters for Enhancing Gait Stability During Ground Slip Perturbations](https://arxiv.org/abs/2601.15056) · 2026-01-21 · 引用 5
- [Supervised Mixture-of-Experts for Surgical Grasping and Retraction](https://arxiv.org/abs/2601.21971) · 2026-01-29 · 引用 5
- [Reinforcement-Learning-Based Assistance Reduces Squat Effort with a Modular Hip--Knee Exoskeleton](https://arxiv.org/abs/2602.17794) · 2026-02-19 · 引用 5
- [Reinforcement learning in linear embedding space unlocks generalizable control across soft robot configurations](https://arxiv.org/abs/2606.08104) · 2026-06-06 · 引用 5
- [Forbidden Region Dynamic Active Constraints in Robot-Assisted Minimally Invasive Surgery](https://arxiv.org/abs/2608.03010) · 2026-08-04 · 引用 5
- [Towards Considerate Embodied AI: Co-Designing Situated Multi-Site Healthcare Robots from Abstract Concepts to High-Fidelity Prototypes](https://arxiv.org/abs/2602.03054) · 2026-02-03 · 引用 4
- [Continuum Robot Localization using Distributed Time-of-Flight Sensors](https://arxiv.org/abs/2602.07209) · 2026-02-06 · 引用 4 · `RSS`
- [RGA-Net: A Vision Enhancement Framework for Robotic Surgical Systems Using Reciprocal Attention Mechanisms](https://arxiv.org/abs/2602.13726) · 2026-02-14 · 引用 4
- [Musculoskeletal Motion Imitation for Learning Personalized Exoskeleton Control Policy in Impaired Gait](https://arxiv.org/abs/2604.09431) · 2026-04-10 · 引用 4
- [Do Rigid-Body Simulators Dream of Soft Robots? Learning Contact-Rich Manipulation for Tendon-Driven Continuum Robots](https://arxiv.org/abs/2606.22397) · 2026-06-21 · 引用 4
- [On-the-fly hand-eye calibration for the da Vinci surgical robot](https://arxiv.org/abs/2601.14871) · 2026-01-21 · 引用 3
- [Adding internal audio sensing to internal vision enables human-like in-hand fabric recognition with soft robotic fingertips](https://arxiv.org/abs/2602.12918) · 2026-02-13 · 引用 3 · `Humanoids`

<a id="99"></a>
### 99 · 其他（418 篇）

- [XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment](https://arxiv.org/abs/2608.09892) · 2026-08-10 · 引用 15
- [Quantization-Aware Collaborative Inference for Large Embodied AI Models](https://arxiv.org/abs/2602.13052) · 2026-02-13 · 引用 13
- [Learning to Act Robustly with View-Invariant Latent Actions](https://arxiv.org/abs/2601.02994) · 2026-01-06 · 引用 7
- [The human intention. A taxonomy attempt and its applications to robotics](https://arxiv.org/abs/2602.15963) · 2026-02-17 · 引用 7
- [Singularity-Free Lie Group Integration and Geometrically Consistent Evaluation of Multibody System Models Described in Terms of Standard Absolute Coordinates](https://arxiv.org/abs/2601.21413) · 2026-01-29 · 引用 5
- [Forward Dynamics of Variable Topology Mechanisms - The Case of Constraint Activation](https://arxiv.org/abs/2604.19419) · 2026-04-21 · 引用 5
- [Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066](https://arxiv.org/abs/2602.17822) · 2026-02-19 · 引用 4
- [Distributed Nonlinear Control of Networked Two-Wheeled Robots under Adversarial Interactions](https://arxiv.org/abs/2604.03917) · 2026-04-05 · 引用 4
- [Safe Control using Learned Safety Filters and Adaptive Conformal Inference](https://arxiv.org/abs/2604.18482) · 2026-04-20 · 引用 4 · `L4DC 2026`
- [How the Fusion of Onboard Sensors and V2X Data can Improve (or not) the Cooperative Perception of Connected Automated Vehicles](https://arxiv.org/abs/2607.07114) · 2026-07-08 · 引用 4
- [Networked Admissibility-Preserving Control for Directed Safe Coordination](https://arxiv.org/abs/2609.09384) · 2026-09-08 · 引用 4
- [The Semantic Lifecycle in Embodied AI: Acquisition, Representation and Storage via Foundation Models](https://arxiv.org/abs/2601.08876) · 2026-01-12 · 引用 3
- [Dynamic Hand Gesture Recognition for Robot Manipulator Tasks](https://arxiv.org/abs/2601.12918) · 2026-01-19 · 引用 3
- [Robust Out-of-Order Retrieval for Grid-Based Storage at Maximum Capacity](https://arxiv.org/abs/2601.19144) · 2026-01-27 · 引用 3
- [Simulating Human Audiovisual Search Behavior](https://arxiv.org/abs/2602.02790) · 2026-02-02 · 引用 3
- [Comparative Analysis of Autonomous Robotic and Manual Techniques for Ultrasonic Sacral Osteotomy: A Preliminary Study](https://arxiv.org/abs/2602.04076) · 2026-02-03 · 引用 3
- [Towards Adaptive Environment Generation for Training Embodied Agents](https://arxiv.org/abs/2602.06366) · 2026-02-06 · 引用 3 · `AAAI`
- [Data-Driven Trajectory Imputation for Vessel Mobility Analysis](https://arxiv.org/abs/2602.11890) · 2026-02-12 · 引用 3
- [Robot-Assisted Social Dining as a White Glove Service](https://arxiv.org/abs/2602.15767) · 2026-02-17 · 引用 3
- [Value Functions for Temporal Logic: Optimal Policies and Safety Filters](https://arxiv.org/abs/2605.01051) · 2026-05-01 · 引用 3

