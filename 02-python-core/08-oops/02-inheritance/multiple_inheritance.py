class Animal:

    def __init__(self, name):

        self.name = name


class Pet:

    def __init__(self, owner):

        self.owner = owner


class Dog(Animal, Pet):

    def __init__(self, name, owner):

        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):

        print(f"{self.name} says woof")


dog = Dog("Spike", "Aahish")

dog.speak()

print(dog.owner)