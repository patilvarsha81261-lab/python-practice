# Dictionary Methods

student = {
    "name": "Samarth",
    "age": 21,
    "course": "AIML"
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Name:", student.get("name"))

student.pop("age")

print("Updated Dictionary:", student)

