"""
Box Plot with Python

Demonstrates:
- Five-number summary
- Quantiles
- Median
- IQR
- Lower and upper fences
- Outlier detection
- Box plot using Seaborn
"""

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Original data
marks = [
    45, 32, 56, 75, 89, 54, 32, 89,
    90, 87, 67, 54, 45, 98, 99, 67, 74
]


# Five-number summary
minimum, q1, median, q3, maximum = np.quantile(
    marks,
    [0, 0.25, 0.50, 0.75, 1.0]
)


# Calculate IQR
iqr = q3 - q1


# Calculate fences
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr


# Detect outliers
outliers = [
    value
    for value in marks
    if value < lower_fence or value > upper_fence
]


# Display results
print("Five-Number Summary")
print("-" * 25)
print("Minimum:", minimum)
print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("Maximum:", maximum)

print("\nIQR:", iqr)

print("\nFences")
print("-" * 25)
print("Lower Fence:", lower_fence)
print("Upper Fence:", upper_fence)

print("\nOutliers")
print("-" * 25)

if outliers:
    print(outliers)
else:
    print("No outliers")


# Create box plot
sns.boxplot(marks)

plt.title("Box Plot of Marks")
plt.ylabel("Marks")

plt.show()