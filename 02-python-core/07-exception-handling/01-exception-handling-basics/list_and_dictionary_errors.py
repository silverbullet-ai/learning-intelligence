# IndexError example

try:

    numbers = [1, 2, 3]

    print(numbers[10])

except IndexError:

    print("Invalid list index")


# KeyError example

try:

    student = {
        "name": "Aahish"
    }

    print(student["age"])

except KeyError:

    print("Key does not exist")