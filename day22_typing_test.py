#typing_test.py (easy version)

import time

sentence = "Python is fun to learn."

print("Type this sentence:")
print(sentence)

start = time.time()
typed = input("> ")
end = time.time()

seconds = end - start
words = len(typed.split())
wpm = words / (seconds / 60)

print("Time:", round(seconds, 1), "seconds")
print("Speed:", round(wpm), "words per minute")

if typed == sentence:
    print("Perfect, no mistakes!")
else:
    print("You made some mistakes")




#Full version (levels, accuracy, saved scores)

# day22_typing_test.py
import csv
import random
import time
from datetime import datetime

SCORE_FILE = "typing_scores.csv"

SENTENCES = {
    "easy": [
        "The sun is hot today.",
        "I like to code in Python.",
        "A cat sat on the mat.",
        "We play games after school.",
    ],
    "medium": [
        "Practice makes a programmer better every single day.",
        "Python is a simple language with a very powerful community.",
        "A good programmer writes code that other people can read.",
    ],
    "hard": [
        "Debugging is twice as hard as writing the code in the first place.",
        "The quick brown fox jumps over the lazy dog, again and again!",
        "Every great developer you know got there by solving problems they were unqualified to solve.",
    ],
}


def calculate_results(target, typed, seconds):
    # accuracy: compare letter by letter
    correct = sum(1 for a, b in zip(target, typed) if a == b)
    accuracy = correct / len(target) * 100

    # standard rule: 5 characters = 1 word
    minutes = max(seconds, 0.1) / 60
    wpm = (len(typed) / 5) / minutes
    return wpm, accuracy


def save_score(level, wpm, accuracy):
    is_new_file = False
    try:
        open(SCORE_FILE).close()
    except FileNotFoundError:
        is_new_file = True

    with open(SCORE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if is_new_file:
            writer.writerow(["date", "level", "wpm", "accuracy"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"),
                         level, round(wpm, 1), round(accuracy, 1)])


def load_scores():
    try:
        with open(SCORE_FILE, newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


def best_wpm(scores, level):
    values = [float(row["wpm"]) for row in scores if row["level"] == level]
    return max(values) if values else None


def play_round():
    level = input("Choose level (easy / medium / hard): ").strip().lower()
    if level not in SENTENCES:
        print("Please type easy, medium or hard")
        return

    scores = load_scores()
    best = best_wpm(scores, level)
    if best is not None:
        print(f"Your best {level} speed: {best} WPM")

    target = random.choice(SENTENCES[level])

    print("\nGet ready...")
    for number in (3, 2, 1):
        print(number)
        time.sleep(1)

    print("\nType this sentence and press Enter:\n")
    print(target)
    print()

    start = time.perf_counter()
    typed = input("> ")
    seconds = time.perf_counter() - start

    if typed.strip() == "":
        print("You didn't type anything")
        return

    wpm, accuracy = calculate_results(target, typed, seconds)

    print(f"\nTime:     {seconds:.1f} seconds")
    print(f"Speed:    {wpm:.1f} WPM")
    print(f"Accuracy: {accuracy:.1f}%")

    if accuracy < 80:
        print("Slow down a little, accuracy matters more than speed")
    elif best is None or wpm > best:
        print("New personal best!")

    save_score(level, wpm, accuracy)


def show_history():
    scores = load_scores()
    if len(scores) == 0:
        print("No scores yet")
        return

    print(f"\n{'Date':<18}{'Level':<9}{'WPM':>7}{'Accuracy':>10}")
    for row in scores[-10:]:
        print(f"{row['date']:<18}{row['level']:<9}{row['wpm']:>7}{row['accuracy']:>9}%")


while True:
    print("\n--- Typing Speed Test ---")
    print("1. Start a test")
    print("2. Show my last 10 scores")
    print("3. Quit")
    choice = input("Choose (1-3): ")

    if choice == "1":
        play_round()
    elif choice == "2":
        show_history()
    elif choice == "3":
        print("Bye! Day 22 done.")
        break
    else:
        print("Please choose 1, 2 or 3")