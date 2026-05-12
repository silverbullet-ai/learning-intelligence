# Filter odd numbers
numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = list(
    filter(lambda x: x % 2 != 0, numbers)
)

print(odd_numbers)


# Filter positive numbers
nums = [-5, -2, 0, 3, 7]

positive = list(
    filter(lambda x: x > 0, nums)
)

print(positive)