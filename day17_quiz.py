# day17_quiz.py
import random
from datetime import datetime

QUESTIONS = [
    {"q": "Which keyword defines a function in Python?",
     "options": ["def", "func", "function", "define"], "answer": "def"},
    {"q": "What does len('python') return?",
     "options": ["5", "6", "7", "Error"], "answer": "6"},
    {"q": "Which one is a list?",
     "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "<1, 2, 3>"], "answer": "[1, 2, 3]"},
    {"q": "What is 10 % 3?",
     "options": ["3", "0", "1", "10"], "answer": "1"},
    {"q": "Which keyword stops a loop early?",
     "options": ["stop", "exit", "break", "end"], "answer": "break"},
    {"q": "What type is 3.14?",
     "options": ["int", "float", "str", "bool"], "answer": "float"},
    {"q": "Which symbol starts a comment?",
     "options": ["//", "#", "/*", "--"], "answer": "#"},
    {"q": "What does print(2 ** 3) show?",
     "options": ["6", "8", "9", "5"], "answer": "8"},
]

SCORE_FILE = "quiz_scores.txt"
LETTERS = "abcd"


def ask_question(number, item):
    options = item["options"][:]      # copy, so the original stays the same
    random.shuffle(options)

    print(f"\nQuestion {number}: {item['q']}")
    for letter, option in zip(LETTERS, options):
        print(f"  {letter}) {option}")

    while True:
        choice = input("Your answer (a-d): ").strip().lower()
        if choice in LETTERS and len(choice) == 1:
            break
        print("Please type a, b, c or d")

    chosen = options[LETTERS.index(choice)]
    if chosen == item["answer"]:
        print("Correct!")
        return True

    print("Wrong. The answer is", item["answer"])
    return False


def save_score(score, total):
    when = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(SCORE_FILE, "a") as f:
        f.write(f"{when} - {score}/{total}\n")


def show_scores():
    try:
        with open(SCORE_FILE) as f:
            print("\nPast scores:")
            print(f.read())
    except FileNotFoundError:
        print("No scores yet")


print("=== PYTHON QUIZ ===")

while True:
    questions = random.sample(QUESTIONS, 5)
    score = 0

    for number, item in enumerate(questions, 1):
        if ask_question(number, item):
            score += 1

    print(f"\nYou scored {score} out of {len(questions)}")

    if score == len(questions):
        print("Perfect!")
    elif score >= 3:
        print("Good job!")
    else:
        print("Keep practicing!")

    save_score(score, len(questions))

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        break

show_scores()
print("Thanks for playing!")