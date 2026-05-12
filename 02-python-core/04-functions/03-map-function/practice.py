# Double numbers
numbers = [1, 2, 3, 4]

double_numbers = list(
    map(lambda x: x * 2, numbers)
)

print(double_numbers)


# Convert strings to float
string_numbers = ["1.5", "2.8", "3.2"]

float_numbers = list(
    map(float, string_numbers)
)

print(float_numbers)