"""
Upsampling Example

Demonstrates how to balance an imbalanced dataset by
increasing the number of observations in the minority class.
"""

import numpy as np
import pandas as pd
from sklearn.utils import resample


# Reproducibility
np.random.seed(42)


# Create an imbalanced dataset
n_samples = 1000
class_zero_ratio = 0.90

n_class_zero = int(n_samples * class_zero_ratio)
n_class_one = n_samples - n_class_zero

df = pd.DataFrame({
    "feature": np.random.randn(n_samples),
    "target": [0] * n_class_zero + [1] * n_class_one
})


print("Original class distribution:")
print(df["target"].value_counts())


# Separate majority and minority classes
df_majority = df[df["target"] == 0]
df_minority = df[df["target"] == 1]


# Upsample minority class
df_minority_upsampled = resample(
    df_minority,
    replace=True,
    n_samples=len(df_majority),
    random_state=42
)


# Combine majority and upsampled minority classes
df_upsampled = pd.concat([
    df_majority,
    df_minority_upsampled
])


print("\nClass distribution after upsampling:")
print(df_upsampled["target"].value_counts())


"""
Original:

Class 0 → 900
Class 1 → 100

After upsampling:

Class 0 → 900
Class 1 → 900

Upsampling increases the minority class.
replace=True allows minority observations
to be selected more than once.
"""