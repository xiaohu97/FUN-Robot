# 01 · VLA 与机器人基础模型

> Vision-Language-Action（VLA）：把视觉、语言和动作放进同一个大模型，目标是做出“一个模型、多种任务、多种机器人”的通用策略。
> 主线：**Gato / RT-1（多任务 Transformer）→ RT-2（VLM 直接输出动作）→ Open X-Embodiment（跨本体数据）→ OpenVLA / π0（开源 + 连续动作）→ π0.5 / GR00T / Gemini Robotics（开放世界泛化）→ 2026：RL 后训练、可引导、世界动作模型**

⭐ = 必读　｜　条目格式见 [`templates/paper-entry.md`](../templates/paper-entry.md)

## 🏛 经典论文

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| ⭐ **Gato** · A Generalist Agent | 2022 · TMLR | 单个 Transformer 同时玩游戏、聊天、控制机械臂，“通才智能体”的早期样板 | [arXiv](https://arxiv.org/abs/2205.06175) |
| ⭐ **RT-1** · Robotics Transformer for Real-World Control at Scale | 2022 · RSS'23 | 13 万条真机示教、700+ 任务训练的机器人 Transformer，证明大规模多任务数据带来泛化 | [arXiv](https://arxiv.org/abs/2212.06817) · [代码](https://github.com/google-research/robotics_transformer) |
| **VIMA** · General Robot Manipulation with Multimodal Prompts | 2022 · ICML'23 | 用图文交错的多模态 prompt 统一描述各种操作任务，并给出对应基准 | [arXiv](https://arxiv.org/abs/2210.03094) · [代码](https://github.com/vimalabs/VIMA) |
| **PaLM-E** · An Embodied Multimodal Language Model | 2023 · ICML'23 | 把图像/状态编码注入 562B 大语言模型，构成能做具身规划的多模态 LLM | [arXiv](https://arxiv.org/abs/2303.03378) |
| **RoboCat** · A Self-Improving Generalist Agent for Robotic Manipulation | 2023 · TMLR | 新任务只需少量示教 → 自己生成数据 → 再训练，形成自我改进循环 | [arXiv](https://arxiv.org/abs/2306.11706) |
| ⭐ **RT-2** · Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023 · CoRL'23 | 把动作离散成文本 token 与 VLM 联合微调，正式提出 VLA 概念，网络知识可迁移到动作 | [arXiv](https://arxiv.org/abs/2307.15818) |
| ⭐ **Open X-Embodiment / RT-X** · Robotic Learning Datasets and RT-X Models | 2023 · ICRA'24 | 21 家机构、22 种机器人、百万级轨迹合并成统一数据集，跨本体训练出现正迁移 | [arXiv](https://arxiv.org/abs/2310.08864) · [代码](https://github.com/google-deepmind/open_x_embodiment) |

## 🚀 最新进展（2024 – 2026）

| 论文 | 年份 · 会议 | 核心贡献 | 资源 |
|---|---|---|---|
| **3D-VLA** · A 3D Vision-Language-Action Generative World Model | 2024 · ICML'24 | 在 VLA 中引入 3D 感知与目标图像/点云生成，“先想象目标再行动” | [arXiv](https://arxiv.org/abs/2403.09631) |
| **Octo** · An Open-Source Generalist Robot Policy | 2024 · RSS'24 | 在 OXE 80 万条轨迹上预训练的开源扩散头 Transformer 策略，观测/动作空间可灵活微调 | [arXiv](https://arxiv.org/abs/2405.12213) · [代码](https://github.com/octo-models/octo) |
| ⭐ **OpenVLA** · An Open-Source Vision-Language-Action Model | 2024 · CoRL'24 | 7B 开源 VLA（Llama 2 + DINOv2/SigLIP），以 1/7 参数超过 RT-2-X，支持 LoRA 微调 | [arXiv](https://arxiv.org/abs/2406.09246) · [代码](https://github.com/openvla/openvla) |
| **HPT** · Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers | 2024 · NeurIPS'24 | 本体专属 stem + 共享 trunk 的结构，把异构机器人数据对齐到同一表示空间 | [arXiv](https://arxiv.org/abs/2409.20537) |
| **RDT-1B** · A Diffusion Foundation Model for Bimanual Manipulation | 2024 · ICLR'25 | 1.2B 双臂扩散基础模型，提出统一物理动作空间以吸收多种双臂数据 | [arXiv](https://arxiv.org/abs/2410.07864) · [代码](https://github.com/thu-ml/RoboticsDiffusionTransformer) |
| **LAPA** · Latent Action Pretraining from Videos | 2024 · ICLR'25 | 从无动作标签的视频中学“潜在动作”做预训练，降低对机器人动作标注的依赖 | [arXiv](https://arxiv.org/abs/2410.11758) |
| ⭐ **π0** · A Vision-Language-Action Flow Model for General Robot Control | 2024 · RSS'25 | VLM + flow matching 动作专家，输出 50Hz 连续动作块，完成叠衣服等长程灵巧任务 | [arXiv](https://arxiv.org/abs/2410.24164) · [代码](https://github.com/Physical-Intelligence/openpi) |
| **CogACT** · A Foundational VLA Model for Synergizing Cognition and Action | 2024 · arXiv | VLM 负责“认知”，独立扩散动作模块负责“动作”，解耦结构显著优于 OpenVLA | [arXiv](https://arxiv.org/abs/2411.19650) |
| **FAST** · Efficient Action Tokenization for VLA Models | 2025 · RSS'25 | 基于 DCT 频域压缩的动作 tokenizer，让自回归 VLA 也能学高频灵巧动作 | [arXiv](https://arxiv.org/abs/2501.09747) |
| **SpatialVLA** · Exploring Spatial Representations for VLA Models | 2025 · RSS'25 | 引入 3D 自我中心位置编码与自适应动作网格，增强 VLA 的空间理解 | [arXiv](https://arxiv.org/abs/2501.15830) |
| **Hi Robot** · Open-Ended Instruction Following with Hierarchical VLA Models | 2025 · ICML'25 | 高层 VLM 理解复杂指令与实时口头纠正，低层 π0 执行，分层“System 2 + System 1” | [arXiv](https://arxiv.org/abs/2502.19417) |
| **OpenVLA-OFT** · Fine-Tuning VLA Models: Optimizing Speed and Success | 2025 · RSS'25 | 并行解码 + 动作分块 + 连续动作 + L1 回归的微调配方，推理快 25~50 倍，LIBERO 97%+ | [arXiv](https://arxiv.org/abs/2502.19645) · [代码](https://github.com/moojink/openvla-oft) |
| ⭐ **GR00T N1** · An Open Foundation Model for Generalist Humanoid Robots | 2025 · arXiv | NVIDIA 人形基础模型：VLM（System 2）+ 扩散动作头（System 1），混合真机/仿真/人类视频训练 | [arXiv](https://arxiv.org/abs/2503.14734) · [代码](https://github.com/NVIDIA/Isaac-GR00T) |
| **Gemini Robotics** · Bringing AI into the Physical World | 2025 · arXiv | 基于 Gemini 2.0 的 VLA 与具身推理模型（ER），强调泛化、交互性与灵巧性 | [arXiv](https://arxiv.org/abs/2503.20020) |
| ⭐ **π0.5** · A VLA with Open-World Generalization | 2025 · CoRL'25 | 多源异构数据协同训练（多机器人、网页数据、高层语义标注），在全新家庭中完成清洁类长程任务 | [arXiv](https://arxiv.org/abs/2504.16054) · [代码](https://github.com/Physical-Intelligence/openpi) |
| **UniVLA** · Learning to Act Anywhere with Task-centric Latent Actions | 2025 · RSS'25 | 在 DINO 特征空间学习任务相关的潜在动作，可从人类视频和跨本体数据预训练 | [arXiv](https://arxiv.org/abs/2505.06111) · [代码](https://github.com/OpenDriveLab/UniVLA) |
| **Knowledge Insulating VLA** · Train Fast, Run Fast, Generalize Better | 2025 · arXiv | 训练连续动作专家时阻断梯度回传 VLM，既保留语言知识又加速训练 | [arXiv](https://arxiv.org/abs/2505.23705) |
| **SmolVLA** · A VLA Model for Affordable and Efficient Robotics | 2025 · arXiv | 约 450M 参数的小型开源 VLA，用社区 LeRobot 数据训练，消费级 GPU 可跑 | [arXiv](https://arxiv.org/abs/2506.01844) · [代码](https://github.com/huggingface/lerobot) |
| **Gemini Robotics 1.5** · Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer | 2025 · arXiv | Motion Transfer 机制吸收多本体数据；动作与多级语言推理交错（先思考再行动）；ER 1.5 刷新具身推理 SOTA | [arXiv](https://arxiv.org/abs/2510.03342) |
| ⭐ **π\*0.6** · a VLA That Learns From Experience | 2025 · arXiv | RECAP：融合示教、自主经验与人工纠正的优势条件 RL，难任务吞吐翻倍、失败率约减半 | [arXiv](https://arxiv.org/abs/2511.14759) · [博客](https://pi.website/blog/pistar06) |
| **Being-H0.5** · Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization | 2026 · arXiv | 把人类交互轨迹当作物理交互的“通用母语”，用 3.5 万小时多模态数据（UniHand-2.0）预训练跨本体 VLA | [arXiv](https://arxiv.org/abs/2601.12993) |
| **LingBot-VLA** · A Pragmatic VLA Foundation Model | 2026 · arXiv | 面向实际部署的 VLA 基础模型，强调工程可用性 | [arXiv](https://arxiv.org/abs/2601.18692) |
| **DynamicVLA** · A Vision-Language-Action Model for Dynamic Object Manipulation | 2026 · NeurIPS'26 | 面向运动物体操作的低延迟 VLA，并构建 20 万条合成 + 免遥操作真机采集的动态操作基准 DOM | [arXiv](https://arxiv.org/abs/2601.22153) |
| **Green-VLA** · Staged Vision-Language-Action Model for Generalist Robots | 2026 · arXiv | 五阶段课程（VLM → 多模态对齐 → 多本体预训练 → 本体适配 → RL 对齐）+ 3000 小时数据，单一策略控制人形、移动操作臂与固定臂 | [arXiv](https://arxiv.org/abs/2602.00919) |
| **ABot-M0** · VLA Foundation Model for Robotic Manipulation with Action Manifold Learning | 2026 · arXiv | 把 6 个公开数据集清洗统一为 600 万条轨迹 / 9500 小时的 UniACT 数据集，结合动作流形学习预训练跨形态操作基础模型 | [arXiv](https://arxiv.org/abs/2602.11236) |
| **MEM** · Multi-Scale Embodied Memory for Vision Language Action Models | 2026 · arXiv | Physical Intelligence 的多尺度记忆：视频短时记忆 + 文本长时记忆，支撑长达 15 分钟的任务（收拾厨房、做烤三明治） | [arXiv](https://arxiv.org/abs/2603.03596) |
| **StarVLA** · A Lego-like Codebase for Vision-Language-Action Model Developing | 2026 · arXiv | 积木式开源 VLA 代码框架，统一复现主流 VLA 方法并快速搭建新模型 | [arXiv](https://arxiv.org/abs/2604.05014) |
| ⭐ **π0.7** · a Steerable Generalist Robotic Foundation Model with Emergent Capabilities | 2026 · arXiv | 以子任务、元数据、子目标图像、控制模式等丰富上下文为条件训练，可吸收混合质量数据并被“引导”，出现组合泛化与零样本跨本体迁移 | [arXiv](https://arxiv.org/abs/2604.15483) |
| **RLDX-1 Technical Report** | 2026 · arXiv | 多流动作 Transformer（MSAT）融合异构模态的灵巧操作通用策略，仿真与真机均超过 π0.5、GR00T N1.6 | [arXiv](https://arxiv.org/abs/2605.03269) |
| **Qwen-VLA** · Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments | 2026 · arXiv | 在 Qwen 视觉语言模型上接 DiT 动作解码器，用一个模型统一操作、导航等多任务、多环境、多本体决策 | [arXiv](https://arxiv.org/abs/2605.30280) |
| **Qwen-RobotManip Technical Report** · Alignment Unlocks Scale for Robotic Manipulation Foundation Models | 2026 · arXiv | 基于 Qwen-VL 的操作 VLA 基础模型，强调异构数据对齐带来的规模化，分布外设置全面超过 π0.5，RoboChallenge 第一 | [arXiv](https://arxiv.org/abs/2606.17846) |
| **Harness VLA** · Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents | 2026 · arXiv | 把冻结的 VLA 当作可重试的接触操作原语，由记忆增强智能体与解析原语组合调度，LIBERO-Pro 上提升 38.6 个点 | [arXiv](https://arxiv.org/abs/2607.08448) |
| **Xiaomi-Robotics-1** · Scaling VLA Models with over 100K Hours of Real-World Trajectories | 2026 · arXiv | 用 10 万小时以上真机轨迹扩展 VLA 规模，探索真机数据的 scaling | [arXiv](https://arxiv.org/abs/2607.15330) |
| **τ0-VLA** · a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation | 2026 · arXiv | 分层基础模型，用世界模型在推理时评估并选择高层子任务（test-time compute 进入机器人） | [arXiv](https://arxiv.org/abs/2608.16885) |
| **GroundingPI** · A Grounding Foundation Model towards Physical Intelligence with Visual Primitives | 2026 · arXiv | 4B 视觉定位基础模型以量化坐标输出点和框，作为 VLA 视觉骨干在 RoboTwin 2.0 分布外设置中全面领先 | [arXiv](https://arxiv.org/abs/2609.39601) |
| **PDRVLA** · A Vision-Language-Action Model with Physical Dynamics Representations | 2026 · arXiv | 轻量物理动力学模块从视觉语言特征中提取“物理 token”来条件化动作，无需在线生成视频；LIBERO 99.3% | [arXiv](https://arxiv.org/abs/2610.37381) |
| **GR00T N1.6** · 开源人形 VLA（无论文） | 2026 · 模型发布 | 3B 参数，VLM + 扩散 Transformer 动作头，CES 2026 发布并开放权重与微调脚本 | [模型](https://huggingface.co/nvidia/GR00T-N1.6-3B) · [代码](https://github.com/NVIDIA/Isaac-GR00T) |

## 🔗 相关
- 上手项目：[openpi](https://github.com/Physical-Intelligence/openpi) · [LeRobot](https://github.com/huggingface/lerobot) · [Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T)
- 评测：LIBERO / SIMPLER / CALVIN → 见 [`11-simulation-benchmarks.md`](./11-simulation-benchmarks.md)
- 世界动作模型（WAM）→ 见 [`07-world-models.md`](./07-world-models.md)

> 📅 **2026 年本方向全部 1404 篇 arXiv 论文**（自动分类、按热度排序）见 [2026 年度总览](../digests/2026-annual-arxiv.md#01)，按月份见 [全量月报](../digests/README.md)。上表只收录其中经人工筛选的代表作。
