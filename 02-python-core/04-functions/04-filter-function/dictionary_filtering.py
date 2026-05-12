students = [
    {"name": "A", "marks": 75},
    {"name": "B", "marks": 90},
    {"name": "C", "marks": 82}
]

top_students = list(
    filter(
        lambda student: student["marks"] > 80,
        students
    )
)

print(top_students)