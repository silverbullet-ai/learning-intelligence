class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):

        return f"{self.name}, {self.age} years old"

    def __repr__(self):

        return f"Person(name='{self.name}', age={self.age})"


person = Person("Aahish", 23)

print(person)
print(repr(person))