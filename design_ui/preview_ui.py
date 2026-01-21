import sys
import subprocess
import os

# 配置 Godot 路径 (Windows 示例，请按需修改)
GODOT_EXEC = r"D:\SteamLibrary\steamapps\common\Godot Engine\godot.windows.opt.tools.64.exe" 

def preview_scene(scene_path):
    output_file = "preview_ui.png"
    
    # 构造命令: godot --headless -s res://utils/screenshot.gd -- <scene_path> <output_path>
    # 注意：-s 表示运行脚本，-- 后面的是传给脚本的参数
    cmd = [
        GODOT_EXEC, 
        "--headless", 
        "--audio-driver", "Dummy",
        "res://Tool/Utils/ScreenshotMain.tscn", 
        "--", 
        scene_path, 
        output_file
    ]
    
    print(f"🎨 Rendering preview for {scene_path}...")
    try:
        subprocess.run(cmd, check=True)
        if os.path.exists(output_file):
            print(f"✅ Preview generated: {output_file}")
            print("You can now open this image to see the design.")
        else:
            print("❌ Failed to generate image.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python preview_ui.py <res://path/to/scene.tscn>")
    else:
        preview_scene(sys.argv[1])