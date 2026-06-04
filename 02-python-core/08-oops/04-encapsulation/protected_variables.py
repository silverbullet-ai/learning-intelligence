class Person:

    def __init__(self, name):

        self._name = name


class Employee(Person):

    pass


employee = Employee("Aahish")

print(employee._name)