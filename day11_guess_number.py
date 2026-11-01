import random

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
        break



    #Twist 1: Limit attempts to 7

    max_attempts = 7

while attempts < max_attempts:
    guess = int(input("Guess: "))
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")
        break
else:
    print("Out of attempts! The number was", secret)