# Count Words in a File

with open("sample.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total Words:", len(words))
print("Total Characters:", len(content))
print("Total Lines:", len(content.splitlines()))