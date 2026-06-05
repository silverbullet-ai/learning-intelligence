class Student:

    def __init__(
        self,
        name,
        marks
    ):

        self.name = name
        self.marks = marks

    def __gt__(self, other):

        return self.marks > other.marks

    def __repr__(self):

        return (
            f"Student("
            f"name='{self.name}', "
            f"marks={self.marks})"
        )


student1 = Student(
    "Aahish",
    95
)

student2 = Student(
    "Manav",
    88
)

print(student1 > student2)