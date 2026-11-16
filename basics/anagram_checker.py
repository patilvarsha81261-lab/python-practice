# Check Whether Two Strings Are Anagrams

text1 = input("Enter first string: ").lower().replace(" ", "")
text2 = input("Enter second string: ").lower().replace(" ", "")

if sorted(text1) == sorted(text2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
