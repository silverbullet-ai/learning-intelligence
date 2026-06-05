class Car:

    def __init__(
        self,
        brand,
        horsepower
    ):

        self.brand = brand
        self.horsepower = horsepower

    def __gt__(self, other):

        return (
            self.horsepower >
            other.horsepower
        )

    def __repr__(self):

        return (
            f"Car("
            f"brand='{self.brand}', "
            f"horsepower={self.horsepower})"
        )


revuelto = Car(
    "Lamborghini Revuelto",
    1001
)

huracan = Car(
    "Lamborghini Huracan",
    631
)

print(revuelto > huracan)