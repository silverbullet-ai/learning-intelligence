import numpy as np

data = np.arange(1, 21)

matrix = data.reshape(4, 5)

print("Matrix:")
print(matrix)

print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Std:", np.std(data))

print("\nValues > 10:")
print(data[data > 10])

normalized = (data - np.mean(data)) / np.std(data)

print("\nNormalized:")
print(normalized)

print("\nSquare Roots:")
print(np.sqrt(data))