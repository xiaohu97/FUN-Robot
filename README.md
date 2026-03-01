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
| 项目合集 | 20条开源项目可读版（解读+应用标签） | [projects.md](./humanoid-awesome/projects/projects.md) |
| 数据集 | 数据集收录模板（待扩展） | [datasets/README.md](./humanoid-awesome/datasets/README.md) |
| Benchmark | 基准收录模板（待扩展） | [benchmarks/README.md](./humanoid-awesome/benchmarks/README.md) |
| 条目模板 | 论文/项目统一模板 | [entry-template.md](./humanoid-awesome/templates/entry-template.md) |

---

## 当前收录

- ✅ 论文：30 条（可读版）
- ✅ 开源项目：20 条（可读版）
- ✅ 总计：50 条初版骨架已升级为可读版

重点覆盖方向：
- 运动控制与全身控制
- 灵巧操作与双臂协作
- VLA（视觉-语言-动作）
- 数据与仿真（Sim2Real）
- 人机交互（HRI）
- 产业应用（零售/仓储/物流等）

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
