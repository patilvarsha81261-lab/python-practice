word = input("Enter a word: ")

reversed_word = word[::-1]

print("Reversed:", reversed_word)

if word == reversed_word:
    print("It is a palindrome")
else:
    print("Not a palindrome")