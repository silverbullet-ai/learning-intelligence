# Names starting with A
names = ["Alice", "Bob", "Ankit", "Jack"]

a_names = list(
    filter(lambda name: name.startswith("A"), names)
)

print(a_names)


# Numbers divisible by 3
numbers = [1,2,3,4,5,6,7,8,9]

divisible_by_3 = list(
    filter(lambda x: x % 3 == 0, numbers)
)

print(divisible_by_3)