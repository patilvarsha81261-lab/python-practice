
#simple code
"""word = input("Enter a word: ")

reversed_word = word[::-1]

print("Reversed:", reversed_word)

if word == reversed_word:
    print("It is a palindrome")
else:
    print("Not a palindrome")"""


#advanced code

# day04_palindrome_advanced.py

def clean(text):
    # keep only letters and numbers, all lowercase
    return "".join(ch for ch in text.lower() if ch.isalnum())


def is_palindrome(text):
    cleaned = clean(text)
    return cleaned == cleaned[::-1]


def is_palindrome_two_pointers(text):
    # same check, but compares from both ends moving inward
    cleaned = clean(text)
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def find_palindromes(words):
    # only words with 2+ letters that read the same backwards
    return [w for w in words if len(clean(w)) > 1 and is_palindrome(w)]


def longest_palindrome_inside(text):
    # finds the longest palindrome hidden inside a text
    s = clean(text)
    best = ""
    for center in range(len(s)):
        # try odd length (center, center) and even length (center, center + 1)
        for left, right in ((center, center), (center, center + 1)):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            candidate = s[left + 1:right]
            if len(candidate) > len(best):
                best = candidate
    return best


def next_palindrome_number(n):
    n += 1
    while str(n) != str(n)[::-1]:
        n += 1
    return n


def save_result(line):
    with open("palindrome_history.txt", "a") as f:
        f.write(line + "\n")


def main():
    while True:
        print("\n--- Palindrome Tool ---")
        print("1. Check a word or sentence")
        print("2. Find palindromes in a list of words")
        print("3. Find longest palindrome inside a text")
        print("4. Next palindrome number")
        print("5. Show history")
        print("6. Quit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            text = input("Enter text: ")
            if is_palindrome(text):
                result = f'"{text}" is a palindrome'
            else:
                result = f'"{text}" is NOT a palindrome'
            print(result)
            save_result(result)

        elif choice == "2":
            words = input("Enter words separated by spaces: ").split()
            found = find_palindromes(words)
            print("Palindromes:", found if found else "none found")
            print("Count:", len(found))

        elif choice == "3":
            text = input("Enter text: ")
            best = longest_palindrome_inside(text)
            print("Longest palindrome inside:", best if best else "none")

        elif choice == "4":
            try:
                n = int(input("Enter a number: "))
                print("Next palindrome number:", next_palindrome_number(n))
            except ValueError:
                print("Please type a valid number")

        elif choice == "5":
            try:
                with open("palindrome_history.txt") as f:
                    print(f.read())
            except FileNotFoundError:
                print("No history yet")

        elif choice == "6":
            print("Bye! Day 4 done.")
            break

        else:
            print("Please choose 1 to 6")


main()