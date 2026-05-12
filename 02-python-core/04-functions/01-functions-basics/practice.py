def even_or_odd(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(24))


def greet(name="Guest"):
    return f"Hello, {name}"


print(greet())
print(greet("Aahish"))