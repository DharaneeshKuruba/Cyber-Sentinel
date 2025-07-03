import threading
import time

timeout = 300
user_input = None

def ask_input():
    global user_input
    user_input = input("🔍 Enter the hidden flag (format: FLAG{...}): ").strip()

def run():
    print("📁 MISSION 1: ADVANCED THREAT LOG ANALYSIS")
    print("🧠 Analyze threat logs to extract a real hidden flag from noisy data.")
    print("⚠️ Beware: There are fake flags planted to confuse you.")

    with open("assets/threat_logs.txt", "r") as file:
        for line in file:
            print(line.strip())

    print(f"\n⏲️ You have {timeout // 60} minutes to find the actual flag.\n")

    t = threading.Thread(target=ask_input)
    t.start()
    t.join(timeout)

    if user_input is None:
        print("❌ Time's up!")
        return False

    if user_input == "FLAG{xFG72A}":
        print("✅ Correct! You've found the real threat signature.")
        return True
    else:
        print("❌ That's not the valid flag.")
        return False
