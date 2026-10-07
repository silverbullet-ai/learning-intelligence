"""
MNAR — Missing Data Not At Random

This example demonstrates missingness that is related to
the value of the variable itself.

Here, higher Income values are more likely to be missing.
"""

import pandas as pd
import numpy as np


np.random.seed(42)

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Income": [
        25000, 30000, 35000, 40000, 45000,
        50000, 60000, 70000, 90000, 120000
    ]
})

print("Original Dataset:")
print(df)


# Make higher income values more likely to be missing.
# This creates a missingness pattern related to the
# value of Income itself.

high_income_indices = df[df["Income"] >= 70000].index

missing_indices = np.random.choice(
    high_income_indices,
    size=2,
    replace=False
)

df.loc[missing_indices, "Income"] = np.nan


print("\nDataset with MNAR Missing Values:")
print(df)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nRemaining Income Values:")
print(df["Income"])


"""
MNAR:
The probability of Income being missing is related to
the Income value itself.

In this example, higher income values were more likely
to become missing.
"""