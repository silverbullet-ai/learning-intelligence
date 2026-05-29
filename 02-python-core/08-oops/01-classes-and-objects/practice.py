class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def display_info(self):

        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


student1 = Student("Aahish", 95)

student1.display_info()