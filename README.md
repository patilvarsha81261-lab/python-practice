# Python Practice

Daily Python practice programs, a 15-day GitHub streak challenge.

I write one small program every day, add my own twist to it, and push it to GitHub.

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
- [ ] Day 10: Fibonacci
- [ ] Day 11: Guess the number
- [ ] Day 12: Password generator
- [ ] Day 13: Binary search
- [ ] Day 14: Calculator
- [ ] Day 15: Bank account

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

Type a word or sentence to check if it reads the same backwards.

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

## Author

[patilvarsha81261-lab](https://github.com/patilvarsha81261-lab)