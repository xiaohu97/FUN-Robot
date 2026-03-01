# 论文可读版（30条）

> 字段：方向标签｜中文解读（2-3行）｜链接

## 1) 运动控制与全身控制

### 1. DeepMimic (2018)
- 标签：`imitation-learning` `locomotion` `sim`
- 解读：把“模仿动作”与强化学习结合，显著提升了角色动作自然度与稳定性。对人形机器人而言，它奠定了“从动作数据学习控制策略”的主流范式。
- 链接：https://arxiv.org/abs/1804.02717

### 2. AMP: Adversarial Motion Priors (2021)
- 标签：`humanoid-rl` `motion-prior` `sim`
- 解读：通过对抗式运动先验，让策略在没有精细奖励设计时也能学到更自然的动作。对复杂步态与转身动作很有价值。
- 链接：https://arxiv.org/abs/2104.02180

### 3. ASE: Large-Scale Reusable Skills (2022)
- 标签：`skill-learning` `latent-policy` `reusable-skills`
- 解读：核心是构建可复用技能库，把“单任务训练”升级为“技能组合”。适合多场景切换的人形应用。
- 链接：https://arxiv.org/abs/2205.01906

### 4. PHC: Periodic Humanoid Control (2024)
- 标签：`periodic-control` `locomotion` `humanoid`
- 解读：聚焦周期性动作建模，提升步态稳定性和能效表现。对长时间行走、重复工况任务很关键。
- 链接：https://arxiv.org/abs/2401.08570

### 5. HOVER (2024)
- 标签：`whole-body-control` `humanoid` `policy`
- 解读：强调全身协调控制，在复杂动作下兼顾平衡和任务执行。适合“边走边干活”的复合任务。
- 链接：https://arxiv.org/abs/2404.19235

### 6. Iterative Closed-Loop Motion Synthesis (2026)
- 标签：`data-scaling` `closed-loop` `humanoid-control`
- 解读：用“训练-评估-再合成”闭环持续提升动作数据质量。更像一条工程化训练流水线，而非一次性训练。
- 链接：https://arxiv.org/abs/2602.21599

## 2) 操作与灵巧手

### 7. Mobile ALOHA (2024)
- 标签：`bimanual` `mobile-manipulation` `teleop`
- 解读：低成本双臂移动操作平台，强调“可复现、可扩展”。特别适合快速验证仓储/零售拣选任务。
- 链接：https://arxiv.org/abs/2401.02117

### 8. ALOHA Unleashed (2024)
- 标签：`low-cost-robotics` `bimanual` `imitation`
- 解读：延续 ALOHA 路线，把低成本硬件与数据驱动控制结合。对预算有限的研发团队很友好。
- 链接：https://arxiv.org/abs/2401.02117

### 9. Grasp, Slide, Roll (2026)
- 标签：`tactile` `contact-rich` `manipulation`
- 解读：系统比较不同触觉接触模式对重建和操作效果的影响。对人形手“弱视觉/盲操”能力提升明显。
- 链接：https://arxiv.org/abs/2602.23206

### 10. SPARR (2026)
- 标签：`sim2real` `assembly` `residual-policy`
- 解读：把“仿真基策略 + 真实残差策略”结合，提升装配任务落地效果。非常贴近工厂场景需求。
- 链接：https://arxiv.org/abs/2602.23253

## 3) 视觉-语言-动作（VLA）与通用策略

### 11. RT-1 (2022)
- 标签：`VLA` `multi-task` `robot-transformer`
- 解读：将 Transformer 用于机器人多任务策略学习，开启了“统一模型跑多任务”的路线。
- 链接：https://arxiv.org/abs/2212.06817

### 12. RT-2 (2023)
- 标签：`VLA` `vision-language` `generalization`
- 解读：把视觉语言能力更深度接入机器人控制，提升了未见任务上的泛化。对开放场景更实用。
- 链接：https://arxiv.org/abs/2307.15818

### 13. PaLM-E (2023)
- 标签：`multimodal-LLM` `embodied` `foundation-model`
- 解读：将具身感知输入融合到大模型，推动“语言智能 + 机器人执行”一体化。
- 链接：https://arxiv.org/abs/2303.03378

### 14. SayCan (2022)
- 标签：`language-planning` `affordance` `LLM`
- 解读：让语言模型负责“说什么该做”，价值模型负责“做不做得成”。是任务规划落地的重要桥梁。
- 链接：https://arxiv.org/abs/2204.01691

### 15. Code as Policies (2022)
- 标签：`program-synthesis` `robot-control` `LLM`
- 解读：将自然语言映射为可执行程序策略，便于快速表达复杂任务逻辑。工程可解释性更强。
- 链接：https://arxiv.org/abs/2209.07753

### 16. VoxPoser (2023)
- 标签：`language-to-action` `affordance` `3D`
- 解读：面向语义指令生成可执行动作，强调“看懂场景再动手”。对服务机器人很实用。
- 链接：https://arxiv.org/abs/2307.05973

### 17. Octo (2024)
- 标签：`open-policy` `multi-robot` `foundation-policy`
- 解读：开源通用策略模型路线，目标是跨平台与跨任务迁移。适合做基线与二次微调。
- 链接：https://arxiv.org/abs/2405.12213

### 18. OpenVLA (2024)
- 标签：`open-vla` `foundation-model` `manipulation`
- 解读：开放版 VLA 路线，降低研究门槛。适合与自有数据结合做行业定制。
- 链接：https://arxiv.org/abs/2406.09246

### 19. GR00T N1 (2025)
- 标签：`foundation-model` `humanoid` `industry`
- 解读：NVIDIA 面向通用人形能力布局的基础模型方向，偏产业生态联动。
- 链接：https://developer.nvidia.com/isaac/gr00t

### 20. RoboCat (2023)
- 标签：`self-improving-agent` `generalist`
- 解读：强调自我提升与跨任务迁移，体现“少样本快速适配”思路。
- 链接：https://www.deepmind.com/blog/robocat-a-self-improving-robotic-agent

### 21. Gato (2022)
- 标签：`generalist-transformer` `multi-domain`
- 解读：通用序列模型跨多模态、多任务的早期代表，对后续通用机器人模型影响大。
- 链接：https://arxiv.org/abs/2205.06175

### 22. Eureka (2023)
- 标签：`reward-design` `LLM-for-RL` `automation`
- 解读：让大模型自动生成奖励函数，减少手工调参成本。对迭代效率提升明显。
- 链接：https://arxiv.org/abs/2310.12931

## 4) 数据、仿真与迁移

### 23. EmbodMocap (2026)
- 标签：`4D-reconstruction` `data-pipeline` `sim2real`
- 解读：提出低成本真实场景人-景4D采集方案，补齐具身数据短板。对训练管线价值非常高。
- 链接：https://arxiv.org/abs/2602.23205

### 24. LessMimic (2026)
- 标签：`long-horizon` `humanoid-interaction` `representation`
- 解读：关注长时任务与多接触交互，用统一表示提升策略泛化。贴近真实复杂作业流程。
- 链接：https://arxiv.org/abs/2602.21723

### 25. Diffusion Policy (2023)
- 标签：`diffusion` `manipulation` `policy-learning`
- 解读：把扩散模型用于动作生成，提升复杂操作轨迹质量与鲁棒性。
- 链接：https://arxiv.org/abs/2303.04137

### 26. ACT: Action Chunking with Transformers (2023)
- 标签：`imitation` `chunking` `transformer`
- 解读：将长动作序列分块学习，降低长时依赖难度。对装配/抓取多步骤任务有效。
- 链接：https://arxiv.org/abs/2304.13705

### 27. UniSim / Unifying Simulation Transfer (2024)
- 标签：`sim2real` `transfer` `generalization`
- 解读：围绕仿真到真实迁移提出统一方法，目标是减少真实数据需求与部署落差。
- 链接：https://arxiv.org/abs/2402.10329

## 5) 人机交互与社交行为

### 28. Humanizing Robot Gaze Shifts (2026)
- 标签：`HRI` `gaze` `social-robotics`
- 解读：提升人形机器人注视转移的自然性，对导览、陪护、前台场景直接有用。
- 链接：https://arxiv.org/abs/2602.21983

### 29. HumanPlus (2024)
- 标签：`teleop` `imitation` `whole-body`
- 解读：强调人类动作映射到机器人本体的效率与质量，适合快速收集示教数据。
- 链接：https://arxiv.org/abs/2405.03985

### 30. Open-TeleVision (2024)
- 标签：`telepresence` `remote-operation` `embodied`
- 解读：关注远程操作与沉浸式感知，适合服务、巡检、危险环境作业。
- 链接：https://arxiv.org/abs/2407.01512
