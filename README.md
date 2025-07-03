# 🔐 Cyber Sentinel: Intelligence Training Missions

Cyber Sentinel is a story-driven terminal-based cybersecurity training game developed in Python. It features 3 missions designed to test players on critical cybersecurity concepts through interactive puzzles, cryptographic challenges, and a simulated hacking environment.

## 🎮 Game Overview

Step into the shoes of a rookie agent and take on the challenge of completing 3 progressively harder missions. Your success will prove your ability to join the elite Cyber Defense Task Force.

### 🧠 Missions Breakdown

| Mission | Challenge Type         | Description |
|--------:|------------------------|-------------|
| 1       | Hidden Key Challenge   | Find a recovery key hidden within a simulated backup file. |
| 2       | Cipher Decryption      | Crack a double-encrypted message using Vigenère cipher logic. |
| 3       | Puzzle & Source Hunt   | Solve a web-based puzzle, inspect hidden code, and unlock the final flag. |

---

## 🧩 Features

- 🖥️ Terminal interface with immersive storyline
- ⏱️ Countdown timer: 5 minutes per mission
- 🔐 Encryption-based puzzles (Caesar, Vigenère)
- 🌐 Web integration (auto-launches mission 3 in browser)
- 🔊 Sound Effects:
  - `alarm.mp3` – Mission start alert
  - `game_start.mp3` – Introduction sound
  - `success.mp3` – Mission success sound
  - `fail.mp3` – Failure tone

---

## 🛠️ Technologies Used

- **Python 3**
- **Webbrowser** for opening HTML files
- **HTML/CSS** for mission 3 puzzle interface
- **playsound** for audio feedback
- **Custom JS Puzzle Logic** in `puzzle.html`

---

## Install dependencies
> pip install playsound==1.2.2

## Run the game
> python3 main.py
