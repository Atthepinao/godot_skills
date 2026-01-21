---
name: design_ui_loop
description: 这是一个迭代式的 UI 设计工具。不仅仅是生成代码，你需要负责“生成 -> 预览 -> 修正”的整个设计闭环。
---
# Godot UI Designer & Iterator

这个 Skill 允许你渲染 UI 场景并查看视觉结果。

## ⚠️ 核心工作流 (Critical Workflow)

作为一个智能 UI 设计师，你不能只写一次代码就结束。你必须遵循以下 **LOOP (循环)**：

1. **Draft (起草)**: 根据用户需求编写或修改 `.tscn` / `.gd` 代码。
2. **Render (渲染)**: 必须调用 `python ... preview_ui.py` 生成预览图 `preview_ui.png`。
3. **Verify (验证)**:
   - 这一步非常关键。既然你无法直接“看见”图片（除非用户上传），你必须**暂停并展示图片**。
   - 询问用户：“预览图已生成。布局、颜色或间距符合预期吗？如果不符合，请告诉我哪里需要调整。”
4. **Refine (修正)**:
   - 如果用户给出视觉反馈（例如“按钮太小了”、“文字没居中”），你**必须**回到第 1 步修改代码，然后**再次**运行第 2 步渲染。
   - **不要**只修改代码而不给新的截图。

## 目标

你的目标不是“写完代码”，而是“交付一张令用户满意的界面截图”。

## 命令 (Command)

```bash
python .agent/skills/design_ui/preview_ui.py {{ scene_path }}
```
