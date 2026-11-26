# Python Practice

Daily Python practice programs, my GitHub streak challenge.

I write one small program every day, add my own twist to it, and push it to GitHub. The 15-day challenge is complete, and I'm continuing with bonus days: games, tools and algorithms.

## Progress

- [x] Day 1: Hello program (age and time-of-day greeting)
- [x] Day 2: Even or odd (try/except, range check)
- [x] Day 3: FizzBuzz (custom range and numbers)
- [x] Day 4: Palindrome checker
- [x] Day 5: Factorial (loop, recursion, timing)
- [x] Day 6: List stats (median and mode)
- [x] Day 7: Word count (top 3 words)
- [x] Day 8: Prime checker
- [x] Day 9: To-do list with file
- [x] Day 10: Fibonacci (generator and checker)
- [x] Day 11: Guess the number (levels and high score)
- [x] Day 12: Password generator (strength checker)
- [x] Day 13: Binary search
- [x] Day 14: Calculator
- [x] Day 15: Bank account (history and custom error)
- [x] Day 16: Hangman game
- [x] Day 17: Quiz game (random questions, saved scores)
- [x] Day 18: Expense tracker (categories, JSON file)
- [x] Day 19: Tic-Tac-Toe (computer opponent, score)
- [x] Day 20: Caesar cipher (encrypt, decrypt, auto-crack)
- [x] Day 21: Contact book (class, JSON file, validation)
- [x] Day 22: Typing speed test (WPM, accuracy, CSV scores)
- [x] Day 23: Text adventure (rooms, items, locked door)
- [x] Day 24: Sorting race (bubble, selection, insertion, merge sort)

## Project structure

```
python-practice/
├── day01_hello.py ... day24_sorting_race.py    # one program per day
├── basics/                                     # small practice files by topic
├── oop-practice/                               # object-oriented programming practice
├── sample.txt
├── todo.txt
└── README.md
```

## Requirements

- Python 3 installed (check with `python --version`)
- No extra libraries needed, only built-in modules

## Setup

```bash
git clone https://github.com/patilvarsha81261-lab/python-practice.git
cd python-practice
```

## How to run each program

Open a terminal in the `python-practice` folder and run the command for the day you want.

### Day 1: Hello program

```bash
python day01_hello.py
```

Asks for your name and age, greets you based on the time of day, and prints the year you turn 100.

### Day 2: Even or odd

```bash
python day02_even_odd.py
```

Type a number to see if it is even or odd. Type `q` to quit. After that, enter a start and end number to check a whole range.

### Day 3: FizzBuzz

```bash
python day03_fizzbuzz.py
```

Enter a start, an end, and two numbers (like 3 and 5). It prints Fizz, Buzz or FizzBuzz, counts each one, and saves the result to `fizzbuzz_output.txt`.

### Day 4: Palindrome checker

```bash
python day04_palindrome.py
```

Choose from a menu: check a word or sentence, find palindromes in a list of words, find the longest palindrome inside a text, find the next palindrome number, or show your saved history in `palindrome_history.txt`.

### Day 5: Factorial

```bash
python day05_factorial.py
```

Enter one whole number, for example `5`. It prints `120`.

### Day 6: List stats

```bash
python day06_list_stats.py
```

Enter numbers separated by commas, for example `4, 8, 15, 16, 23, 42`. It prints sum, max, min, average, median and mode.

### Day 7: Word count

```bash
python day07_word_count.py
```

Enter the file name `sample.txt` (keep it in the same folder). It prints total words, characters, lines, unique words and the top 3 words.

### Day 8: Prime checker

```bash
python day08_prime_checker.py
```

Enter a number to see if it is prime and what its prime factors are. Then enter a limit to list all primes up to it.

### Day 9: To-do list

```bash
python day09_todo.py
```

Use the menu to add, view, mark as done, or delete tasks. Tasks are saved in `todo.txt`, so they are still there next time.

### Day 10: Fibonacci

```bash
python day10_fibonacci.py
```

Enter how many Fibonacci numbers to show (for example `10` prints `0 1 1 2 3 5 8 13 21 34`). Then enter a number to check if it is a Fibonacci number.

### Day 11: Guess the number

```bash
python day11_guess_number.py
```

Choose a level (easy, medium or hard) and guess the secret number. The program says "Too low" or "Too high" after each guess. Your best score (fewest tries) is saved in `highscore.txt`.

### Day 12: Password generator

```bash
python day12_password_generator.py
```

Enter a password length and choose whether to include symbols. It prints a random password and shows how strong it is.

### Day 13: Binary search

```bash
python day13_binary_search.py
```

Enter a number to find in a sorted list. It prints the position and the number of steps taken.

### Day 14: Calculator

```bash
python day14_calculator.py
```

Enter two numbers and an operation (+ - * / ** %). It keeps running until you type `quit`.

### Day 15: Bank account

```bash
python day15_bank_account.py
```

Deposit and withdraw money, view your balance and transaction history. Withdrawing more than you have shows an insufficient funds error. The balance is saved in `balance.txt`.

### Day 16: Hangman

```bash
python day16_hangman.py
```

Guess the secret word one letter at a time. You have 6 wrong guesses before you lose. The game keeps your score and lets you play again.

### Day 17: Quiz game

```bash
python day17_quiz.py
```

Answer 5 random multiple choice questions about Python. Your score is saved in `quiz_scores.txt`, and past scores are shown when you finish.

### Day 18: Expense tracker

```bash
python day18_expense_tracker.py
```

Add expenses with a category, view them in a table, see your spending by category, and delete entries. Data is saved in `expenses.json`.

### Day 19: Tic-Tac-Toe

```bash
python day19_tictactoe.py
```

Play against a friend or the computer. Choose a square from 1 to 9. The computer tries to win and blocks your winning moves. The game keeps the score across rounds.

### Day 20: Caesar cipher

```bash
python day20_caesar_cipher.py
```

Encrypt and decrypt messages with a shift key. You can also try all 25 shifts, or auto-crack a long message using letter frequency. Encrypted messages are saved in `secret_messages.txt`.

### Day 21: Contact book

```bash
python day21_contact_book.py
```

Add, search, update and delete contacts. Phone numbers and emails are checked with regular expressions. Contacts are saved in `contacts.json` (this file is not uploaded to GitHub, because it holds personal data).

### Day 22: Typing speed test

```bash
python day22_typing_test.py
```

Choose a level, type the sentence shown, and see your speed in words per minute and your accuracy. Scores are saved in `typing_scores.csv`.

### Day 23: Text adventure

```bash
python day23_adventure.py
```

Explore an old house, pick up items and find a way out. Commands: `go <direction>`, `take <item>`, `look at <item>`, `inventory`, `help` and `quit`.

### Day 24: Sorting race

```bash
python day24_sorting_race.py
```

Watch bubble sort work step by step, or race four sorting algorithms on random numbers and compare the number of comparisons and the time each one needs.

## Practice by topic: `basics/`

Small practice programs grouped by topic. Run any of them like this:

```bash
python basics/finally_block.py
```

| Topic | Files |
|-------|-------|
| Data types and operators | `data_types.py`, `datastypes.py`, `assignment_operators.py`, `comparison_operators.py` |
| Loops | `break_statement.py`, `continue_statement.py` |
| Functions | `basic_function.py`, `function_calculator.py`, `function_parameters.py` |
| Strings | `anagram_checker.py`, `character_frequency.py`, `count_characters.py`, `count_vowels.py` |
| Dictionaries | `dictionary_basics.py`, `dictionary_methods.py` |
| Errors and exceptions | `custom_exception.py`, `else_block.py`, `file_not_found.py`, `finally_block.py` |
| Object-oriented basics | `abstraction.py`, `class_and_object.py`, `constructor.py` |

## Object-oriented practice: `oop-practice/`

| File | What it is |
|------|------------|
| `encapsulation.py` | Encapsulation |
| `Inheritance.py` | Inheritance |
| `polymorphism.py` | Polymorphism |
| `count_words_in_file.py` | Counts words, characters and lines in a text file |
| `simple.txt` | Sample text file |

```bash
python oop-practice/encapsulation.py
```

## Data files

These files are used or created by the programs.

| File | Used by |
|------|---------|
| `sample.txt` | Day 7 word count (input text) |
| `todo.txt` | Day 9 to-do list (saved tasks) |
| `fizzbuzz_output.txt` | Day 3 FizzBuzz (saved output) |
| `palindrome_history.txt` | Day 4 palindrome checker (saved results) |
| `highscore.txt` | Day 11 guess the number (created when you win) |
| `balance.txt` | Day 15 bank account (created on first deposit) |
| `quiz_scores.txt` | Day 17 quiz game (created after the first game) |
| `expenses.json` | Day 18 expense tracker (created on the first expense) |
| `secret_messages.txt` | Day 20 Caesar cipher (created when you encrypt) |
| `contacts.json` | Day 21 contact book (created on the first contact, not uploaded) |
| `typing_scores.csv` | Day 22 typing test (created after the first test) |

## Tips

- Always run the command from inside the `python-practice` folder. If you see "No such file or directory", you are in the wrong folder.
- Use `python` on Windows. On Mac or Linux, use `python3`.
- Press `Ctrl+C` to stop a program that keeps running.
- Save the file (`Ctrl+S`) before you run or commit it.

## What I learned

- **Day 1:** input(), datetime, f-strings
- **Day 2:** % operator, try/except, while loops
- **Day 3:** for loops, if/elif/else order matters
- **Day 4:** string slicing [::-1], functions
- **Day 5:** loops vs recursion, time.perf_counter()
- **Day 6:** lists, sum, max, min, Counter
- **Day 7:** reading files, string.punctuation, Counter.most_common()
- **Day 8:** prime numbers, checking up to the square root
- **Day 9:** functions, saving data to a file, list pop()
- **Day 10:** generators with yield, swapping values a, b = b, a + b
- **Day 11:** random module, while/else, continue, saving a high score to a file
- **Day 12:** string module, random.choice and shuffle, any()
- **Day 13:** binary search, sorted lists, counting steps
- **Day 14:** if/elif chains, float(), power and remainder operators
- **Day 15:** classes and objects, custom exceptions, raise/except
- **Day 16:** lists of strings, generator expressions, game loops
- **Day 17:** list of dictionaries, random.sample and shuffle, zip(), input validation
- **Day 18:** json module, dictionaries inside lists, sorted() with lambda, formatted table output
- **Day 19:** tuples in lists, checking winning lines, writing a simple game AI
- **Day 20:** ord() and chr(), modulo for wrap-around, letter frequency analysis
- **Day 21:** classes that own data, regular expressions (re), raising and catching errors
- **Day 22:** csv module, time.sleep and perf_counter, calculating WPM and accuracy
- **Day 23:** nested dictionaries, tuple keys, parsing commands with split(), copy.deepcopy
- **Day 24:** sorting algorithms, recursion in merge sort, comparing algorithms by comparisons and time

## Author

[patilvarsha81261-lab](https://github.com/patilvarsha81261-lab)