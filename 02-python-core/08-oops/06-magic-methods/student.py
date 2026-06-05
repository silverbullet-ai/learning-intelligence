class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def __repr__(self):

        return f"Student(name='{self.name}', marks={self.marks})"


student = Student(
    "Aahish",
    95
)

print(repr(student))