---
name: lint_gdscript
description: 用于检查 GDScript 代码的语法错误和风格问题。当你修改或编写了 .gd 文件后，必须运行此工具。
---
# GDScript Linter

这个 Skill 允许你运行 `gdlint` 来检查指定的 Godot 脚本文件。

## 使用场景

- 当用户要求检查代码错误时。
- 当你（AI）生成了新的代码，在提交给用户之前，应该先自我检查一遍。
- 如果代码运行报错，使用此工具排查静态语法问题。

## 命令 (Command)

```bash
python -m gdtoolkit.linter {{ file_path }}
```
