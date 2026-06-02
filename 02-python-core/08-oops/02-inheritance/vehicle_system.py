class Vehicle:

    def start(self):

        print("Vehicle started")


class Bike(Vehicle):

    def helmet(self):

        print("Helmet required")


bike = Bike()

bike.start()
bike.helmet()