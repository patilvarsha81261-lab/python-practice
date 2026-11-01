"""import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! You took", attempts, "tries")
        break"""



    # Twist 1: limit attempts to 7
import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("I picked a number from 1 to 100. You have 7 tries.")

while attempts < max_attempts:
    guess = int(input("Guess: "))
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! You took", attempts, "tries")
        break
else:
    print("Out of attempts! The number was", secret)