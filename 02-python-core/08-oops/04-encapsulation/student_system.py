class Student:

    def __init__(self, name, marks):

        self.__name = name
        self.set_marks(marks)

    def set_marks(self, marks):

        if 0 <= marks <= 100:

            self.__marks = marks

        else:

            print("Marks must be between 0 and 100")

    def get_marks(self):

        return self.__marks


student = Student("Aahish", 95)

print(student.get_marks())