# simple code to implement caesar cipher


text = input("Enter a message: ")
shift = int(input("Shift (1-25): "))

result = ""
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            base = ord("A")
        else:
            base = ord("a")
        result = result + chr((ord(ch) - base + shift) % 26 + base)
    else:
        result = result + ch

print("Encrypted:", result)







#Full version (decrypt, try all shifts, auto-crack)


# day20_caesar_cipher.py
import string
from collections import Counter


def shift_text(text, shift):
    result = ""
    for ch in text:
        if ch in string.ascii_letters:
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch          # spaces, digits, symbols stay the same
    return result


def get_shift():
    while True:
        try:
            shift = int(input("Shift (1-25): "))
        except ValueError:
            print("Please type a number")
            continue
        if 1 <= shift <= 25:
            return shift
        print("Shift must be between 1 and 25")


def guess_shift(text):
    # In English, the most common letter is usually "e"
    letters = [ch.lower() for ch in text if ch in string.ascii_letters]
    if len(letters) == 0:
        return None
    most_common = Counter(letters).most_common(1)[0][0]
    return (ord(most_common) - ord("e")) % 26


def save_message(label, text):
    with open("secret_messages.txt", "a") as f:
        f.write(f"{label}: {text}\n")


while True:
    print("\n--- Caesar Cipher ---")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Try all 25 shifts (when you don't know the key)")
    print("4. Auto-crack a long message")
    print("5. Quit")
    choice = input("Choose (1-5): ")

    if choice == "1":
        text = input("Message: ")
        shift = get_shift()
        result = shift_text(text, shift)
        print("Encrypted:", result)
        save_message(f"Encrypted (shift {shift})", result)

    elif choice == "2":
        text = input("Encrypted message: ")
        shift = get_shift()
        print("Decrypted:", shift_text(text, -shift))

    elif choice == "3":
        text = input("Encrypted message: ")
        for shift in range(1, 26):
            print(f"Shift {shift:>2}: {shift_text(text, -shift)}")

    elif choice == "4":
        text = input("Paste a long encrypted message: ")
        shift = guess_shift(text)
        if shift is None:
            print("No letters found")
        elif shift == 0:
            print("It looks like the message is not encrypted")
        else:
            print(f"Best guess: shift {shift}")
            print("Decrypted:", shift_text(text, -shift))

    elif choice == "5":
        print("Bye! Day 20 done.")
        break

    else:
        print("Please choose 1 to 5")