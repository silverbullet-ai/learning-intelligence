"""
Assignment:
Create a timer-style decorator.

Expected Output:

Function Started
Hello Aahish
Function Finished
"""


def timer(func):

    def wrapper():

        print("Function Started")

        func()

        print("Function Finished")

    return wrapper


@timer
def greet():

    print("Hello Aahish")


greet()