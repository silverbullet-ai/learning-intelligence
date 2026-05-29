class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        return "C"


student = Student("Aahish", 92)

print(student.grade())