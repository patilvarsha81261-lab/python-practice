#day12_password_generator.py (simple version)

"""import random
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
    chars += "!@#$%^&*"""





#password_generator.py

import random
import string

# 1. Ask the user
length = int(input("Password length: "))
symbols = input("Include symbols? (y/n): ")

# 2. Decide which characters to use
chars = string.ascii_letters + string.digits
if symbols == "y":
    chars = chars + "!@#$%"

# 3. Build the password
password = ""
for i in range(length):
    password = password + random.choice(chars)

print("Your password:", password)

# 4. Check strength (simple)
if length < 8:
    print("Strength: Weak")
elif length < 12:
    print("Strength: Medium")
else:
    print("Strength: Strong")