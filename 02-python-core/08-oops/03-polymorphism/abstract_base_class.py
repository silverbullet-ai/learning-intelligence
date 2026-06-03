from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):

    def start_engine(self):

        return "Car engine started"


class Bike(Vehicle):

    def start_engine(self):

        return "Bike engine started"


car = Car()
bike = Bike()

print(car.start_engine())
print(bike.start_engine())