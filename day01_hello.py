# day01_hello.py
from datetime import datetime

name = input("Your name: ")
age = int(input("Your age: "))

# Greeting based on time of day
hour = datetime.now().hour
if hour < 12:
    greeting = "Good morning"
elif hour < 17:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# Year the person turns 100
current_year = datetime.now().year
year_100 = current_year + (100 - age)

print(f"{greeting}, {name}! Day 1 of my streak.")
print(f"You will turn 100 in the year {year_100}.")