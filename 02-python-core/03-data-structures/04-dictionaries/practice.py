student = {
    "name": "Aahish",
    "age": 23,
    "grade": "A"
}

print(student["name"])

student["age"] = 24

student["country"] = "India"

print(student)

for key, value in student.items():
    print(f"{key} : {value}")