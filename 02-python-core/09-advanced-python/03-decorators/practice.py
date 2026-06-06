def decorator(func):

    def wrapper():

        print("Before Function")

        func()

        print("After Function")

    return wrapper


@decorator
def say_hello():

    print("Hello")


say_hello()