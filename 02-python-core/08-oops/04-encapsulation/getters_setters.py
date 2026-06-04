class Person:

    def __init__(self, name, age):

        self.__name = name
        self.__age = age

    def get_name(self):

        return self.__name

    def get_age(self):

        return self.__age

    def set_age(self, age):

        if age > 0:

            self.__age = age

        else:

            print("Age cannot be negative")


person = Person("Aahish", 23)

print(person.get_name())

person.set_age(25)

print(person.get_age())