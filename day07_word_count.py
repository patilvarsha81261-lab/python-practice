# day07_word_count.py


from collections import Counter
import string

# 1. Ask for the file name (press Enter to use sample.txt)

filename = input("Enter file name (press Enter for sample.txt): ").strip()
if filename == "":
    filename = "sample.txt"

# 2. Read the file; if it's missing, create it with sample text

try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print(f"{filename} not found. Creating it with sample text...")
    content = (
        "The quick brown fox jumps over the lazy dog.\n"
        "The dog barks, and the fox runs away!\n"
    )
    with open(filename, "w") as file:
        file.write(content)

# 3. Basic counts

words = content.split()
print("Total Words:", len(words))
print("Total Characters:", len(content))
print("Total Lines:", len(content.splitlines()))

# 4. Clean the text: lowercase and no punctuation

cleaned = content.lower()
for p in string.punctuation:
    cleaned = cleaned.replace(p, "")
clean_words = cleaned.split()

# 5. Unique words and top 3

print("Unique Words:", len(set(clean_words)))

counts = Counter(clean_words)
print("Top 3 words:")
for word, count in counts.most_common(3):
    print(" ", word, "->", count)