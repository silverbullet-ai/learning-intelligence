fruits = ["apple", "banana", "cherry"]

print(fruits[0])
print(fruits[-1])

fruits.append("orange")
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

fruits.remove("banana")
print(fruits)

for fruit in fruits:
    print(fruit)