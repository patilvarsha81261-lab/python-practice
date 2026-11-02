#day12_password_generator.py (simple version)

import random
import string

length = 12
chars = string.ascii_letters + string.digits + "!@#$%"

password = ""
for i in range(length):
    password += random.choice(chars)

print("Your password:", password)

#Choose length and symbols
try:
    length = int(input("Password length (8-32): "))
except ValueError:
    print("Please type a number")
    exit()

use_symbols = input("Include symbols? (y/n): ").lower() == "y"

chars = string.ascii_letters + string.digits
if use_symbols:
    chars += "!@#$%^&*"