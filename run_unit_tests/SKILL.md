---
name: run_unit_tests
description: 在 Godot Headless 模式下运行单元测试脚本。用于在不打开游戏窗口的情况下快速验证逻辑。
---
# Headless Unit Test Runner

这个 Skill 调用 Godot 的命令行模式来运行指定的测试脚本。

## 使用场景

- "运行一下所有单元测试。"
- "测试一下刚刚修改的战斗逻辑 (combat_test.gd)。"
- 持续集成/验证代码逻辑。

## 命令 (Command)

```bash
python .agent/skills/run_tests/test_runner.py {{ script_path }}
```
