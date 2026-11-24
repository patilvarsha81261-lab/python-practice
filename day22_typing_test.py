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