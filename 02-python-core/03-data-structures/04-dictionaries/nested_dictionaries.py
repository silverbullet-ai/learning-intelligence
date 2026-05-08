students = {
    "student1": {
        "name": "Aahish",
        "age": 23
    },

    "student2": {
        "name": "Manav",
        "age": 22
    }
}

print(students["student2"]["name"])

for student_id, info in students.items():
    print(student_id)

    for key, value in info.items():
        print(f"{key} : {value}")