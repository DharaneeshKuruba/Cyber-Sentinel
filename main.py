import mission_one
import mission_two
import mission_three
import time
import os
from playsound import playsound

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(r"""
  ____            _     _       _     _             
 |  _ \ ___  __ _(_)___| |__   (_)___| |_ ___  _ __ 
 | |_) / _ \/ _` | / __| '_ \  | / __| __/ _ \| '__|
 |  __/  __/ (_| | \__ \ | | |_| \__ \ || (_) | |   
 |_|   \___|\__, |_|___/_| |_(_)_|___/\__\___/|_|   
            |___/                                   
   Cyber Sentinel: Intelligence Training Missions
    """)

def main():
    clear_console()
    banner()
    playsound("sounds/alarm.mp3")
    print("🔒 Welcome Agent. Your mission is to complete all 3 cybersecurity challenges.")
    print("⏱ Each mission has a 5-minute time limit. Be sharp. Be precise.")
    print("💥 Good luck, the agency is counting on you.\n")
    
    input("▶️ Press ENTER to begin Mission 1...")
    clear_console()
    playsound("sounds/game_start.mp3")
    result1 = mission_one.run()
    if result1:
        playsound("sounds/success.mp3")
    else:
        playsound("sounds/fail.mp3")
        print("\n❌ Mission 1 failed. Training terminated.")
        return
    
    input("\n✅ Mission 1 Complete! Press ENTER to continue to Mission 2...")
    clear_console()
    playsound("sounds/game_start.mp3")
    result2 = mission_two.run()
    if result2:
        playsound("sounds/success.mp3")
    else:
        playsound("sounds/fail.mp3")
        print("\n❌ Mission 2 failed. Training terminated.")
        return

    input("\n✅ Mission 2 Complete! Press ENTER to continue to Final Mission...")
    clear_console()
    playsound("sounds/game_start.mp3")
    result3 = mission_three.run()
    if result3:
        playsound("sounds/success.mp3")
        print("\n🎉 All Missions Completed Successfully!")
        print("🏆 You’ve proven your skills. Promotion to Senior Agent approved.")
        print("📜 FLAG: CYBER-AGENT-CERTIFIED")
    else:
        playsound("sounds/fail.mp3")
        print("\n❌ Final Mission failed. Training terminated.")

if __name__ == "__main__":
    main()
