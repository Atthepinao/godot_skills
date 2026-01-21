import sys
import subprocess
import os

# --- 配置区域 ---
# 如果你的 godot 命令没加入环境变量，请将其改为绝对路径
# Windows 例子: r"D:\Godot\Godot_v4.4.exe"
# Mac/Linux 例子: "/Applications/Godot.app/Contents/MacOS/Godot"
GODOT_EXEC = "godot" 
# ----------------

def run_headless_tests(script_path):
    if not os.path.exists(script_path) and not script_path.startswith("res://"):
        print(f"Error: Test script not found: {script_path}")
        return

    print(f"🚀 Running tests headless: {script_path}...")
    
    # 构建命令: godot --headless --script <script_path>
    cmd = [GODOT_EXEC, "--headless", "--script", script_path]
    
    try:
        # 实时输出测试结果
        process = subprocess.Popen(
            cmd, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            text=True, 
            encoding='utf-8',
            errors='replace'
        )
        
        for line in process.stdout:
            print(line, end='')
            
        process.wait()
        
        if process.returncode != 0:
            print(f"\n❌ Tests failed with exit code: {process.returncode}")
        else:
            print("\n✅ Tests finished successfully.")
            
    except FileNotFoundError:
        print("❌ Error: Godot executable not found. Please check 'GODOT_EXEC' path in test_runner.py")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # 默认测试入口，你可以改成你项目中常用的默认测试文件
        target_script = "res://Tool/Utils/run_tests.gd"
    else:
        target_script = sys.argv[1]
        
    run_headless_tests(target_script)