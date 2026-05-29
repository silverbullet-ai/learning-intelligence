class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def annual_salary(self):

        return self.salary * 12


employee = Employee("Aahish", 50000)

print(employee.annual_salary())