import importlib
import subprocess
import sys
import os

# Danh sách các module cần kiểm tra
modules = [
    "customtkinter",
    "platform",
    "psutil",
    "requests",
    "threading",
    "time",
    "queue",
    "re",
    "logging",
    "sys",
    "os",
    "subprocess",
    "importlib.metadata",
    "selenium",
    "datetime",
    "traceback",
    "signal",
    "webdriver_manager"
]

def install_module(module_name):
    """Cài đặt module pip"""
    print(f"[+] Đang cài đặt: {module_name} ...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

def check_and_install_modules():
    """Kiểm tra & cài đặt nếu thiếu"""
    for module in modules:
        try:
            importlib.import_module(module.split(".")[0])
            print(f"[OK] Module đã có: {module}")
        except ImportError:
            try:
                install_module(module.split(".")[0])
            except Exception as e:
                print(f"[ERR] Lỗi khi cài {module}: {e}")

if __name__ == "__main__":
    # 1. Kiểm tra & cài đặt module
    check_and_install_modules()
    print("\n✅ Hoàn tất kiểm tra & cài đặt module.\n")

    # 2. Chạy file ./tun/bot.py
    bot_path = os.path.join(".", "run", "sryzendis-3.py")
    if os.path.exists(bot_path):
        print(f"[RUN] Đang chạy {bot_path}...")
        subprocess.run([sys.executable, bot_path])
    else:
        print(f"[ERR] Không tìm thấy file: {bot_path}")
