<div align="center">
  <h1>🤖 FUN-Robot</h1>
  <p><b>机器人与具身智能：经典论文 · 最新进展 · 开源项目</b></p>
  <p>Robotics & Embodied AI Paper Collection（中文友好、分类清晰、持续更新）</p>
  <p>
    <a href="./papers/README.md">📚 论文库</a> ·
    <a href="./papers/must-read.md">🧭 阅读路线</a> ·
    <a href="./digests/README.md">🗞 进展速递</a> ·
    <a href="./projects/README.md">🛠 开源项目</a> ·
    <a href="./datasets/README.md">📦 数据集</a> ·
    <a href="./benchmarks/README.md">📏 基准</a> ·
    <a href="./templates/">🧩 模板</a>
  </p>
</div>

---

## 这是什么

参考 [funNLP](https://github.com/fighting41love/funNLP) 的组织方式，把机器人 / 具身智能领域的论文整理成**按方向分类、经典与前沿分开、每篇一句话中文解读**的资料库，并配套**模板 + 脚本**，方便自己持续添加新论文。

适合：
- 想系统入门具身智能的同学 → 从 [🧭 阅读路线](./papers/must-read.md) 开始
- 想跟踪前沿的研究者 → 看各方向的「🚀 最新进展」和 [🗞 进展速递](./digests/README.md)
- 想动手复现的开发者 → 看 [🛠 开源项目](./projects/README.md)

## 📚 论文库（12 个方向）

| # | 方向 | 代表工作 |
|---|---|---|
| 01 | [VLA 与机器人基础模型](./papers/01-vla-foundation-models.md) | RT-2 · OpenVLA · π0 / π0.5 / π0.7 · GR00T · Gemini Robotics |
| 02 | [具身推理与任务规划](./papers/02-embodied-reasoning-planning.md) | SayCan · Code as Policies · VoxPoser · ReKep · Eureka |
| 03 | [模仿学习与策略学习](./papers/03-imitation-learning.md) | DAgger · Diffusion Policy · ACT · DP3 |
| 04 | [强化学习与足式运动控制](./papers/04-rl-locomotion.md) | RMA · legged_gym · Extreme Parkour · HIL-SERL |
| 05 | [人形机器人](./papers/05-humanoid.md) | DeepMimic · PHC · HumanPlus · HOVER · ASAP · BeyondMimic |
| 06 | [操作、抓取与灵巧手](./papers/06-manipulation-dexterous.md) | Dex-Net · Rubik's Cube · PerAct · DexterityGen |
| 07 | [世界模型与视频生成](./papers/07-world-models.md) | Dreamer · UniSim · Cosmos · V-JEPA 2 · DreamZero |
| 08 | [视觉表征与 3D 场景理解](./papers/08-perception-representation.md) | R3M · VC-1 · F3RM · FoundationPose |
| 09 | [具身导航与移动操作](./papers/09-navigation.md) | R2R · ViNT · NoMaD · NaVILA · Uni-NaVid |
| 10 | [数据采集、遥操作与数据集](./papers/10-data-teleoperation.md) | ALOHA · UMI · DROID · MimicGen · AgiBot World |
| 11 | [仿真平台、Sim2Real 与评测基准](./papers/11-simulation-benchmarks.md) | MuJoCo · Isaac Gym / Lab · LIBERO · SIMPLER |
| 12 | [综述与教程](./papers/12-surveys.md) | VLA 综述 · 行为基础模型综述 · WAM 教程 |

### 收录统计

<!-- STATS:START -->
| 方向 | 经典 | 最新进展 | ⭐ 必读 | 合计 |
|---|---:|---:|---:|---:|
| [VLA 与机器人基础模型](papers/01-vla-foundation-models.md) | 7 | 25 | 10 | 32 |
| [具身推理与任务规划（LLM / VLM for Robotics）](papers/02-embodied-reasoning-planning.md) | 10 | 7 | 5 | 17 |
| [模仿学习与策略学习](papers/03-imitation-learning.md) | 10 | 5 | 6 | 15 |
| [强化学习与足式运动控制](papers/04-rl-locomotion.md) | 7 | 4 | 6 | 11 |
| [人形机器人（运动、全身控制与遥操作）](papers/05-humanoid.md) | 5 | 23 | 8 | 28 |
| [操作、抓取与灵巧手](papers/06-manipulation-dexterous.md) | 13 | 10 | 6 | 23 |
| [世界模型与视频生成](papers/07-world-models.md) | 6 | 14 | 7 | 20 |
| [视觉表征与 3D 场景理解](papers/08-perception-representation.md) | 4 | 5 | 3 | 9 |
| [具身导航与移动操作](papers/09-navigation.md) | 7 | 11 | 3 | 18 |
| [数据采集、遥操作与大规模数据集](papers/10-data-teleoperation.md) | 2 | 12 | 5 | 14 |
| [仿真平台、Sim2Real 与评测基准](papers/11-simulation-benchmarks.md) | 7 | 9 | 6 | 16 |
| [综述与教程](papers/12-surveys.md) | 0 | 14 | 3 | 14 |
| **总计** | **78** | **139** | **68** | **217** |
<!-- STATS:END -->

## 🔥 当前前沿速览（截至 2026 年）

1. **VLA 从“模仿”走向“经验”**：π\*0.6 用 RL 后训练、π0.7 用丰富上下文实现可引导与组合泛化，Gemini Robotics 1.5 让动作与推理交错。
2. **世界动作模型（World-Action Model）兴起**：DreamZero、DreamDojo 等用视频生成骨干同时预测画面与动作，被视为 VLA 之后的新范式。
3. **人形全身控制走向基础模型**：从 BeyondMimic / GMT 的通用动作跟踪，到 X-WBC 等跨本体行为基础模型。
4. **数据规模化**：AgiBot World、Xiaomi-Robotics-1 等百万轨迹 / 十万小时级真机数据，以及 UMI 式无机器人采集和人类视频学习。
5. **基础设施成熟**：Isaac Lab、MuJoCo Playground 让大规模并行训练成为标配；LIBERO / SIMPLER 成为 VLA 评测基线。

## ➕ 如何添加新论文

```bash
# 自动获取 arXiv 标题，插入指定方向的「最新进展」表格，并生成精读笔记
python scripts/new_paper.py 2410.24164 --short "π0" --topic 01 --summary "一句话贡献" --note

# 查重 + 检查链接 + 刷新上面的统计表
python scripts/check.py --update
```

| 模板 | 用途 |
|---|---|
| [`templates/paper-entry.md`](./templates/paper-entry.md) | 论文表格行（加入分类清单） |
| [`templates/paper-note.md`](./templates/paper-note.md) | 精读笔记（[示例：Diffusion Policy](./papers/notes/2303.04137-diffusion-policy.md)） |
| [`templates/digest.md`](./templates/digest.md) | 月度进展速递 |
| [`templates/project-entry.md`](./templates/project-entry.md) | 开源项目条目 |

完整流程与规范见 [CONTRIBUTING.md](./CONTRIBUTING.md)；分类与标签规则见 [taxonomy.md](./taxonomy.md)。

## 📁 仓库结构

```
├── papers/        # 论文库：12 个方向文件 + 必读路线 + notes/ 精读笔记
├── digests/       # 按时间的进展速递（如 2026 年 1-2 月 arXiv humanoid 109 篇）
├── projects/      # 开源项目（框架、仿真器、人形控制、系统库）
├── datasets/      # 数据集
├── benchmarks/    # 评测基准与指标
├── templates/     # 所有模板
├── scripts/       # new_paper.py（新增论文）、check.py（查重 + 统计）
├── taxonomy.md    # 分类体系与标签词表
└── CONTRIBUTING.md
```

## 维护节奏建议

- **每周**：浏览 arXiv `cs.RO`，把候选论文记进当月速递
- **每月**：整理一期 [速递](./digests/README.md)，把值得保留的升级进分类清单
- **每年初**：把超过 2 年的「最新进展」挪进「经典」或删除，更新阅读路线

欢迎通过 Issue（「📄 推荐论文」模板）或 PR 贡献。

## License

建议补充 MIT License（如需可直接添加 `LICENSE` 文件）。
