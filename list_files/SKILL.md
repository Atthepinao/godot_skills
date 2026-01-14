---
name: list_project_structure
description: 列出项目中的所有文件和文件夹结构。全平台通用（Win/Mac/Linux）。
---
# Project Structure Lister

这个 Skill 使用 Python 脚本生成当前项目的树状目录结构图，并会自动过滤掉 Godot 的 .import 缓存文件。

## 使用场景

- 当你想知道某个文件在哪里时。
- 当你想让 AI 理解整个项目的组织方式时。

## 命令 (Command)

```bash
python .agent/skills/list_files/file_lister.py {{ directory_path }}
```
