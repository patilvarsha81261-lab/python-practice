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