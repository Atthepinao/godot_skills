---
name: search_godot_docs
description: 在线查询 Godot 4.4 官方文档。当你需要确认 API 用法、类属性或方法签名时使用。
---
# Godot Documentation Searcher

这个 Skill 会访问 Godot 在线文档 (latest版) 并返回类的详细说明、属性和方法列表。

## 使用场景

- 当你不确定某个类（如 `RigidBody2D`）有哪些信号时。
- 当你需要查阅某个函数（如 `move_and_slide`）的具体参数时。
- **注意**：如果查询失败，请检查类名拼写是否正确（区分大小写，虽然工具会处理，但最好准确）。

## 命令 (Command)

```bash
python .agent/skills/search_docs/doc_fetcher.py {{ class_name }}
```
