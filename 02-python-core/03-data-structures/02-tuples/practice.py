# Creating tuples
numbers = (1, 2, 3, 4, 5)

print(numbers[0])
print(numbers[-1])

# Slicing
print(numbers[1:4])
print(numbers[::-1])

# Count and index
nums = (1, 2, 2, 3)

print(nums.count(2))
print(nums.index(3))

# Tuple to list
nums_list = list(nums)
nums_list.append(100)

print(tuple(nums_list))