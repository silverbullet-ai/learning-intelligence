def student_report(name, marks):

    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    else:
        grade = "C"

    return average, grade


avg, grade = student_report(
    "Aahish",
    [95, 88, 92]
)

print(avg)
print(grade)