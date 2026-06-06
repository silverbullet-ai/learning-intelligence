"""
Assignment:
Create a generator that yields
all even numbers between 1 and 20.
"""


def even_numbers():

    for num in range(1, 21):

        if num % 2 == 0:
            yield num


for value in even_numbers():
    print(value)