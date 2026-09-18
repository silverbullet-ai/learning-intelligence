"""
MAR — Missing At Random

This example demonstrates missingness that depends on
an observed variable.

Here, missing Income values are associated with Gender.
"""

import pandas as pd
import numpy as np


np.random.seed(42)

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Gender": [
        "Male", "Male", "Female", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],
    "Income": [
        30000, 45000, 50000, 42000, 60000,
        55000, 48000, 52000, 70000, 65000
    ]
})

print("Original Dataset:")
print(df)


# Introduce missing Income values based on the observed
# Gender variable.
male_indices = df[df["Gender"] == "Male"].index

missing_indices = np.random.choice(
    male_indices,
    size=2,
    replace=False
)

df.loc[missing_indices, "Income"] = np.nan


print("\nDataset with MAR Missing Values:")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nMissing Income by Gender:")
print(df.groupby("Gender")["Income"].apply(lambda x: x.isnull().sum()))


"""
MAR:
The missingness of Income is related to the observed
Gender variable.

Gender is observed, while Income is the variable containing
missing values.
"""