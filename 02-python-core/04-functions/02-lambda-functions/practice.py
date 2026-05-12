# Square using lambda
square = lambda x: x * x

print(square(5))


# Even/Odd checker
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even_odd(10))
print(even_odd(7))


# Multiple arguments
addition = lambda x, y, z: x + y + z

print(addition(1, 2, 3))