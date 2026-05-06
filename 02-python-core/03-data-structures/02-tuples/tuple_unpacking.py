# Tuple unpacking
packed = (1, "hello", 3.14)

a, b, c = packed

print(a)
print(b)
print(c)

# Star unpacking
nums = (1, 2, 3, 4, 5, 6)

first, *middle, last = nums

print(first)
print(middle)
print(last)