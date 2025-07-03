import threading
import time

timeout = 300
user_input = None

# Reverse Caesar first
def reverse_caesar(text, shift=7):
    result = ''
    for c in text:
        if c.isalpha():
            shifted = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            result += shifted
        else:
            result += c
    return result

# Then Substitution
sub_map = {
    'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q',
    'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U',
    'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y',
    'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',
    'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G',
    'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K',
    'Y': 'L', 'Z': 'M'
}
def subst_decrypt(text):
    return ''.join([k for c in text for k,v in sub_map.items() if v == c]) if text else ""

def decrypt_double(ciphertext):
    step1 = reverse_caesar(ciphertext, shift=7)
    return subst_decrypt(step1)

def ask_input():
    global user_input
    user_input = input("🔐 Enter the decrypted message: ").strip().upper()

def run():
    print("💣 MISSION 2: DOUBLE ENCRYPTED PAYLOAD")
    print("🔒 Message is encrypted using substitution + reverse Caesar.")
    print(f"⏲️ You have {timeout//60} minutes.\n")
    
    with open("assets/decrypt_this.txt", "r") as f:
        encrypted = f.read().strip()
        print("📄 Encrypted message:\n", encrypted)

    t = threading.Thread(target=ask_input)
    t.start()
    t.join(timeout)

    if user_input is None:
        print("❌ Time expired.")
        return False

    expected = "AGENT_ELIMINATED_INTRUDER_SUCCESSFULLY"
    if user_input == expected:
        print("✅ Bravo! Intrusion neutralized.")
        return True
    else:
        print("❌ Incorrect decryption.")
        return False
