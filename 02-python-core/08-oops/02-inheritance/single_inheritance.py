class Car:

    def __init__(self, windows, doors, engine_type):

        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def drive(self):

        print(f"Driving {self.engine_type} car")


class Tesla(Car):

    def __init__(self, windows, doors, engine_type, self_driving):

        super().__init__(windows, doors, engine_type)

        self.self_driving = self_driving

    def auto_pilot(self):

        print(f"Self driving enabled: {self.self_driving}")


tesla = Tesla(4, 5, "electric", True)

tesla.drive()
tesla.auto_pilot()