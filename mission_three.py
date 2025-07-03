import webbrowser
import os
import threading
import time

timeout = 300  # 5 minutes
user_input = None

def ask_input():
    global user_input
    user_input = input("🔑 Enter the hidden Recovery Key (format: FLAG{...}): ").strip()

def run():
    print("🛠️ MISSION: BACKUP RECOVERY")
    print("You must find a recovery key hidden deep inside a corrupted backup HTML file.")
    print("🕵️ Clue: Right-click → View Page Source or press CTRL+U.")

    file_path = os.path.abspath("assets/backup_code.html")
    webbrowser.open("file://" + file_path)

    print(f"\n⏲️ You have {timeout // 60} minutes to inspect and input the key!\n")
    t = threading.Thread(target=ask_input)
    t.start()
    t.join(timeout)

    if user_input is None:
        print("❌ Time's up! You failed to recover the system.")
        return False

    if user_input == "FLAG{R3C0V3RY_KEY_UNL0CK3D}":
        print("✅ Flag accepted! Backup successfully restored.")
        return True
    else:
        print("❌ Incorrect flag. Recovery failed.")
        return False
