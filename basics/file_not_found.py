# Handle File Not Found Error

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File does not exist.")
