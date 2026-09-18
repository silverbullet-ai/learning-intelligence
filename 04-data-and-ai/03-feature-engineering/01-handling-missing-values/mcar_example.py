"""
MCAR — Missing Completely At Random

This example demonstrates missing values where the missingness
has no systematic relationship with the data.
"""

import pandas as pd
import numpy as np


# Create sample data
np.random.seed(42)

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Age": [21, 24, 22, 27, 25, 23, 28, 26, 30, 29],
    "Score": [85, 72, 90, 65, 78, 88, 91, 70, 82, 95]
})

print("Original Dataset:")
print(df)


# Randomly select rows for missing values
missing_indices = np.random.choice(df.index, size=3, replace=False)

df.loc[missing_indices, "Score"] = np.nan


print("\nDataset with MCAR Missing Values:")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())


"""
MCAR:
The missing values were introduced randomly.

There is no systematic relationship between the missingness
and the observed or missing data.
"""