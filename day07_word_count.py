# day07_word_count.py
from collections import Counter
import string

# 1. Read the file (handle a missing file)
filename = input("Enter file name (like sample.txt): ")

try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Make sure it is in the same folder.")
    exit()

# 2. Basic counts
words = content.split()
print("Total Words:", len(words))
print("Total Characters:", len(content))
print("Total Lines:", len(content.splitlines()))

# 3. Clean the text: lowercase and no punctuation
cleaned = content.lower()
for p in string.punctuation:
    cleaned = cleaned.replace(p, "")
clean_words = cleaned.split()

# 4. Unique words and top 3
print("Unique Words:", len(set(clean_words)))

counts = Counter(clean_words)
print("Top 3 words:")
for word, count in counts.most_common(3):
    print(" ", word, "->", count)