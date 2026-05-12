a = [1, 2, 3]
b = [10, 20, 30]

# Add lists
result = list(
    map(lambda x, y: x + y, a, b)
)

print(result)


# Multiply lists
products = list(
    map(lambda x, y: x * y, a, b)
)

print(products)