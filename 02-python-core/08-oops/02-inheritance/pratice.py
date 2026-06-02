class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, grade):

        super().__init__(name, age)

        self.grade = grade

    def display(self):

        print(self.name, self.age, self.grade)


student = Student("Aahish", 21, "A")

student.display()