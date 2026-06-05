class Laptop:

    def __init__(
        self,
        name,
        ram,
        processor
    ):

        self.name = name
        self.ram = ram
        self.processor = processor

    def __str__(self):

        return (
            f"{self.name} | "
            f"{self.ram}GB RAM | "
            f"{self.processor}"
        )

    def __repr__(self):

        return (
            f"Laptop("
            f"name='{self.name}', "
            f"ram={self.ram}, "
            f"processor='{self.processor}')"
        )


laptop = Laptop(
    "Ashwing",
    16,
    "Ryzen 7"
)

print(laptop)
print(repr(laptop))