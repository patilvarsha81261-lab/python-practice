#day12_password_generator.py (simple version)

import random
import string

length = 12
chars = string.ascii_letters + string.digits + "!@#$%"

password = ""
for i in range(length):
    password += random.choice(chars)

print("Your password:", password)