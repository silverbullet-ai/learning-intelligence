import gc


def squares(n):

    for i in range(n):
        yield i * i


gen = squares(5)

for value in gen:
    print(value)

print("\nManual Garbage Collection")

print(gc.collect())