# day16_hangman.py
import random

WORDS = ["python", "github", "variable", "function", "loop",
         "string", "program", "keyboard", "developer", "terminal"]

STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0
    max_wrong = 6

    while wrong < max_wrong:
        display = " ".join(letter if letter in guessed else "_" for letter in word)

        print(STAGES[wrong])
        print("\nWord:   ", display)
        print("Guessed:", " ".join(sorted(guessed)) if guessed else "none")

        if "_" not in display:
            print("\nYou won! The word was", word)
            return True

        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please type one letter only")
            continue

        if guess in guessed:
            print("You already guessed that letter")
            continue

        guessed.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            wrong += 1
            print(f"Wrong! {max_wrong - wrong} tries left")

    print(STAGES[wrong])
    print("\nYou lost. The word was", word)
    return False


wins = 0
losses = 0

print("=== HANGMAN ===")

while True:
    if play():
        wins += 1
    else:
        losses += 1

    print(f"\nScore: {wins} won, {losses} lost")
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
    