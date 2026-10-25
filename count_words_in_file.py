# day04_word_count.py
from collections import Counter
import string

filename = input("Enter file name (like sample.txt): ")

try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Make sure it is in the same folder.")
    exit()

# Basic counts
words = content.split()
lines = content.splitlines()

print("Total Words:", len(words))
print("Total Characters:", len(content))
print("Total Lines:", len(lines))

# Clean the text: lowercase and remove punctuation
cleaned = content.lower()
for p in string.punctuation:
    cleaned = cleaned.replace(p, "")

clean_words = cleaned.split()

# Unique words
print("Unique Words:", len(set(clean_words)))

# Top 3 most common words
counts = Counter(clean_words)
print("Top 3 words:")
for word, count in counts.most_common(3):
    print(" ", word, "->", count)