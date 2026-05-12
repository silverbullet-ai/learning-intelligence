# Uppercase conversion
words = ["aahish", "python", "ai"]

upper_words = list(
    map(str.upper, words)
)

print(upper_words)


# Length of words
lengths = list(
    map(len, words)
)

print(lengths)


# Squares
numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda x: x ** 2, numbers)
)

print(squares)