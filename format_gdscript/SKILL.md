---
name: format_gdscript
description: 自动格式化 GDScript 代码文件。当你觉得代码缩进混乱、空行过多或不整洁时，使用此工具。它会直接修改文件。
---
# GDScript Formatter

这个 Skill 调用 `gdformat` 来自动美化代码。它会修复缩进、空格和换行问题。

## 使用场景

- 当你完成了一段复杂的代码编写后。
- 当你让 AI 重构代码后，为了保险起见，让它运行一次格式化。
- "把这个脚本整理一下"。

## 命令 (Command)

```bash
python -m gdtoolkit.formatter {{ file_path }}
```
