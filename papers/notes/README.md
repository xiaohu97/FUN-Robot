# 📝 精读笔记

每篇精读过的论文一份笔记，使用统一模板 [`templates/paper-note.md`](../../templates/paper-note.md)。

## 命名规则
`<arXiv编号>-<简称小写连字符>.md`，例如 `2303.04137-diffusion-policy.md`。没有 arXiv 的用 `YYYY-MM-DD-简称.md`。

## 快速创建
```bash
python scripts/new_paper.py 2303.04137 --short "Diffusion Policy" --topic 03 --note
```
脚本会：① 生成笔记文件并填好元信息；② 在分类表格中插入一行并挂上 `[笔记]` 链接。

## 笔记索引

| 论文 | 方向 | 推荐度 | 状态 |
|---|---|---|---|
| [Diffusion Policy](./2303.04137-diffusion-policy.md)（示例） | 03 模仿学习 | ⭐⭐⭐⭐⭐ | 精读 |
