class Person:

    def __init__(self, name, age):

        self.__name = name
        self.__age = age


person = Person("Aahish", 23)

print(dir(person))