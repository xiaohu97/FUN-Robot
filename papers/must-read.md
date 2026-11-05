# 🧭 必读清单与阅读路线

> 不知道从哪读起？按下面的路线走。每条路线 8~12 篇，按“先经典、后前沿”排序，每篇都给出“读完应该能回答的问题”。
> 所有论文的完整信息（会议、代码、一句话贡献）在对应分类文件里。

## 路线 0 · 先建地图（1~2 篇综述）

| # | 论文 | 读完能回答 |
|---|---|---|
| 1 | [A Survey on Vision-Language-Action Models for Embodied AI](https://arxiv.org/abs/2405.14093) | VLA 有哪些结构流派？数据和评测怎么做？ |
| 2 | [Aligning Cyber Space with Physical World: A Survey on Embodied AI](https://arxiv.org/abs/2407.06886) | 具身智能包含哪些子问题？各自的代表工作是什么？ |

## 路线 A · 机器人学习基础（所有人必读，10 篇）

| # | 论文 | 方向 | 读完能回答 |
|---|---|---|---|
| 1 | [End-to-End Training of Deep Visuomotor Policies](https://arxiv.org/abs/1504.00702) | [06](./06-imitation-learning.md) | 为什么“从像素直接到动作”是可行的？ |
| 2 | [DAgger](https://arxiv.org/abs/1011.0686) | [06](./06-imitation-learning.md) | 行为克隆的复合误差从哪来？怎么缓解？ |
| 3 | [Domain Randomization](https://arxiv.org/abs/1703.06907) | [17](./17-simulation-benchmarks.md) | 只在仿真里训练，凭什么能用到真机？ |
| 4 | [Learning to Walk in Minutes (legged_gym)](https://arxiv.org/abs/2109.11978) | [10](./10-legged-locomotion.md) | 大规模并行仿真 RL 的标准流程是什么？ |
| 5 | [Diffusion Policy](https://arxiv.org/abs/2303.04137) | [06](./06-imitation-learning.md) | 为什么生成式动作头能处理多模态示教？（[示例笔记](./notes/2303.04137-diffusion-policy.md)） |
| 6 | [ACT / ALOHA](https://arxiv.org/abs/2304.13705) | [06](./06-imitation-learning.md) | 动作分块为什么能提升精细操作？ |
| 7 | [SayCan](https://arxiv.org/abs/2204.01691) | [04](./04-embodied-reasoning-planning.md) | LLM 如何与机器人技能对接？ |
| 8 | [Code as Policies](https://arxiv.org/abs/2209.07753) | [05](./05-robot-agents.md) | “代码即策略”的优缺点是什么？ |
| 9 | [RT-1](https://arxiv.org/abs/2212.06817) → [RT-2](https://arxiv.org/abs/2307.15818) | [01](./01-vla-foundation-models.md) | VLA 的概念是怎么来的？动作如何 token 化？ |
| 10 | [Open X-Embodiment](https://arxiv.org/abs/2310.08864) | [01](./01-vla-foundation-models.md) | 跨本体数据为什么有用？ |

## 路线 B · VLA 与通用策略（前沿主线）

| # | 论文 | 读完能回答 |
|---|---|---|
| 1 | [OpenVLA](https://arxiv.org/abs/2406.09246) | 开源 VLA 的标准结构与微调方式 |
| 2 | [π0](https://arxiv.org/abs/2410.24164) | flow matching 动作专家如何输出高频连续动作？ |
| 3 | [FAST](https://arxiv.org/abs/2501.09747) | 自回归 VLA 如何高效 token 化动作？ |
| 4 | [OpenVLA-OFT](https://arxiv.org/abs/2502.19645) | 微调 VLA 时哪些设计最影响速度和成功率？ |
| 5 | [GR00T N1](https://arxiv.org/abs/2503.14734) | System 1 / System 2 双系统架构；人形数据金字塔 |
| 6 | [π0.5](https://arxiv.org/abs/2504.16054) | 开放世界泛化需要什么样的数据配比？ |
| 7 | [Gemini Robotics 1.5](https://arxiv.org/abs/2510.03342) | “先思考再行动”和跨本体 Motion Transfer |
| 8 | [π\*0.6 (RECAP)](https://arxiv.org/abs/2511.14759) | VLA 如何用真机经验做 RL 后训练？ |
| 9 | [π0.7](https://arxiv.org/abs/2604.15483) | 丰富上下文条件如何让模型“可引导”并吸收混合质量数据？ |
| 10 | [DreamZero](https://arxiv.org/abs/2602.15922) | 世界动作模型（WAM）与 VLA 的区别 |
| 11 | [MolmoAct2](https://arxiv.org/abs/2605.02881) · [CaP-X](https://arxiv.org/abs/2603.22435) | 2026 下半年的两条新路线：完全开源的动作推理模型 vs. 大模型智能体直接写代码控制机器人 |

## 路线 C · 人形机器人与运动控制

| # | 论文 | 读完能回答 |
|---|---|---|
| 1 | [Learning Quadrupedal Locomotion over Challenging Terrain](https://arxiv.org/abs/2010.11251) | 教师-学生特权蒸馏 |
| 2 | [RMA](https://arxiv.org/abs/2107.04034) | 在线自适应如何应对未知环境？ |
| 3 | [DeepMimic](https://arxiv.org/abs/1804.02717) → [AMP](https://arxiv.org/abs/2104.02180) | 动作模仿奖励 vs 对抗式运动先验 |
| 4 | [PHC](https://arxiv.org/abs/2305.06456) | 如何用一个策略跟踪大规模动捕数据？ |
| 5 | [Real-World Humanoid Locomotion with RL](https://arxiv.org/abs/2303.03381) | 人形 sim2real 行走的完整流程 |
| 6 | [HumanPlus](https://arxiv.org/abs/2406.10454) | 人形全身遥操作 + 模仿学习 |
| 7 | [HOVER](https://arxiv.org/abs/2410.21229) | 多模式指令的统一全身控制器 |
| 8 | [ASAP](https://arxiv.org/abs/2502.01143) | 如何用真机数据对齐仿真动力学？ |
| 9 | [BeyondMimic](https://arxiv.org/abs/2508.08241) | 高动态动作跟踪 + 测试时引导的扩散控制 |
| 10 | [X-WBC](https://arxiv.org/abs/2609.15213) | 跨本体全身控制基础模型 |

## 路线 D · 数据与基础设施

| # | 论文 | 读完能回答 |
|---|---|---|
| 1 | [UMI](https://arxiv.org/abs/2402.10329) | 不用机器人也能采集可迁移的示教吗？ |
| 2 | [Mobile ALOHA](https://arxiv.org/abs/2401.02117) | 低成本全身遥操作 + 协同训练 |
| 3 | [MimicGen](https://arxiv.org/abs/2310.17596) | 如何从少量示教自动扩增数据？ |
| 4 | [DROID](https://arxiv.org/abs/2403.12945) · [AgiBot World](https://arxiv.org/abs/2503.06669) | 大规模真机数据集如何组织与质控？ |
| 5 | [Data Scaling Laws in Imitation Learning](https://arxiv.org/abs/2410.18647) | 数据“多样性”和“数量”哪个更重要？ |
| 6 | [Isaac Lab](https://arxiv.org/abs/2511.04831) | 现代 GPU 仿真框架能做什么？ |
| 7 | [LIBERO](https://arxiv.org/abs/2306.03310) · [SIMPLER](https://arxiv.org/abs/2405.05941) | VLA 论文里的仿真评测是怎么做的？ |

## 路线 E · 世界模型

| # | 论文 | 读完能回答 |
|---|---|---|
| 1 | [World Models](https://arxiv.org/abs/1803.10122) → [DreamerV3](https://arxiv.org/abs/2301.04104) | 在潜空间“想象”中学习策略 |
| 2 | [UniSim](https://arxiv.org/abs/2310.06114) | 视频生成模型能当模拟器用吗？ |
| 3 | [Cosmos](https://arxiv.org/abs/2501.03575) | 世界基础模型平台由哪些部件组成？ |
| 4 | [V-JEPA 2](https://arxiv.org/abs/2506.09985) | 不生成像素的预测式世界模型如何规划？ |
| 5 | [DreamGen](https://arxiv.org/abs/2505.12705) | 用世界模型合成训练数据 |
| 6 | [DreamZero](https://arxiv.org/abs/2602.15922) → [Fast-WAM](https://arxiv.org/abs/2603.16666) | WAM 作为零样本策略；测试时“想象未来”到底有没有必要？ |
| 7 | [Cosmos Policy](https://arxiv.org/abs/2601.16163) · [LingBot-VA](https://arxiv.org/abs/2601.21998) | 如何把预训练视频模型直接变成机器人策略？ |
| 8 | [From World Models to World Action Models](https://arxiv.org/abs/2607.00836) | WAM 的四种范式 |

## 路线 F · 2026 新方向速览（每个新方向 2~3 篇）

> 对应 v2 分类中新增 / 拆分的 6 个方向，适合已有基础、想快速跟上 2026 年变化的读者。

| 方向 | 论文 | 读完能回答 |
|---|---|---|
| [02 世界动作模型](./02-world-action-models.md) | [DreamZero](https://arxiv.org/abs/2602.15922) → [Fast-WAM](https://arxiv.org/abs/2603.16666) → [OpenWAM](https://arxiv.org/abs/2609.07398) | WAM 为什么能零样本泛化？视频预测的作用在训练还是推理？ |
| [05 机器人智能体](./05-robot-agents.md) | [CaP-X](https://arxiv.org/abs/2603.22435) → [LLM as Policy](https://arxiv.org/abs/2609.24170) → [Zetta](https://arxiv.org/abs/2608.16590) | 通用大模型直接控制机器人能做到什么程度？短板在哪？ |
| [07 RL 后训练](./07-rl-post-training.md) | [π\*0.6 / RECAP](https://arxiv.org/abs/2511.14759) → [QAM](https://arxiv.org/abs/2601.14234) | 如何用真机经验和 RL 继续提升预训练策略？ |
| [08 奖励与失败恢复](./08-reward-failure-recovery.md) | [GVL](https://arxiv.org/abs/2411.04549) → [Robometer](https://arxiv.org/abs/2603.02115) → [LIBERO-RECOVER](https://arxiv.org/abs/2609.05178) | 通用奖励模型如何训练？“接近 100% 成功率”的策略为什么仍然脆弱？ |
| [09 记忆](./09-memory-long-horizon.md) | [MEM](https://arxiv.org/abs/2603.03596) → [RoboMME](https://arxiv.org/abs/2603.04639) | 机器人策略需要哪几类记忆？怎么评测？ |
| [13 触觉](./13-tactile.md) | [3D-ViTac](https://arxiv.org/abs/2410.24091) → [FTP-1](https://arxiv.org/abs/2606.13102) → [N0-TWAM](https://arxiv.org/abs/2607.23783) | 触觉如何进入 VLA 与世界动作模型？ |
