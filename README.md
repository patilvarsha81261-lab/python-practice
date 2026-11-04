# Python Practice

Daily Python practice programs, a 15-day GitHub streak challenge.

I wrote one small program every day, added my own twist to it, and pushed it to GitHub. All 15 days are complete.

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

## Project structure

```
python-practice/
├── day01_hello.py
├── day02_even_odd.py
├── day03_fizzbuzz.py
├── day04_palindrome.py
├── day05_factorial.py
├── day06_list_stats.py
├── day07_word_count.py
├── day08_prime_checker.py
├── day09_todo.py
├── day10_fibonacci.py
├── day11_guess_number.py
├── day12_password_generator.py
├── day13_binary_search.py
├── day14_calculator.py
├── day15_bank_account.py
├── count_words_in_file.py
├── encapsulation.py
├── Inheritance.py
├── polymorphism.py
├── fizzbuzz_output.txt
├── palindrome_history.txt
├── sample.txt
├── simple.txt
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

Enter a start, an end, and two numbers (like 3 and 5). It prints Fizz, Buzz or FizzBuzz and saves the result to `fizzbuzz_output.txt`.

### Day 4: Palindrome checker

```bash
python day04_palindrome.py
```

Type a word or sentence to check if it reads the same backwards. Results can be saved in `palindrome_history.txt`.

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

Deposit and withdraw money, view your balance and transaction history. Withdrawing more than you have shows an insufficient funds error.

## Extra practice files

| File | What it is |
|------|------------|
| `count_words_in_file.py` | Counts words, characters and lines in a text file |
| `encapsulation.py` | Object-oriented practice: encapsulation |
| `Inheritance.py` | Object-oriented practice: inheritance |
| `polymorphism.py` | Object-oriented practice: polymorphism |

Run them the same way:

```bash
python encapsulation.py
python Inheritance.py
python polymorphism.py
python count_words_in_file.py
```

## Data files

These text files are used or created by the programs.

| File | Used by |
|------|---------|
| `sample.txt` | Day 7 word count (input text) |
| `simple.txt` | Extra text file for practice |
| `todo.txt` | Day 9 to-do list (saved tasks) |
| `fizzbuzz_output.txt` | Day 3 FizzBuzz (saved output) |
| `palindrome_history.txt` | Day 4 palindrome checker (saved results) |

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

## Author

[patilvarsha81261-lab](https://github.com/patilvarsha81261-lab)