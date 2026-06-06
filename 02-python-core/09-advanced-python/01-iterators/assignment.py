"""
Assignment:
Manually recreate a for loop using:

- iter()
- next()
- while True
- StopIteration
"""

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

while True:
    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        print("Iterator exhausted")
        break