def square(n):

    for i in range(n):
        yield i ** 2


gen = square(5)

print(next(gen))
print(next(gen))
print(next(gen))

print("\nRemaining values:")

for value in gen:
    print(value)