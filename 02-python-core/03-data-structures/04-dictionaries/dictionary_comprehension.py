# Squares dictionary
squares = {x: x**2 for x in range(5)}

print(squares)

# Even squares
even_squares = {
    x: x**2
    for x in range(10)
    if x % 2 == 0
}

print(even_squares)