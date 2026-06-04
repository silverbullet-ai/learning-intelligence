from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, monthly_salary):

        self.monthly_salary = monthly_salary

    def calculate_salary(self):

        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(self, hours, rate):

        self.hours = hours
        self.rate = rate

    def calculate_salary(self):

        return self.hours * self.rate


full_time = FullTimeEmployee(50000)

part_time = PartTimeEmployee(80, 300)

print(full_time.calculate_salary())
print(part_time.calculate_salary())