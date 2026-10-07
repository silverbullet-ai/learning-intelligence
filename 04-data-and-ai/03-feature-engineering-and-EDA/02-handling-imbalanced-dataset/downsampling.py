"""
Downsampling Example

Demonstrates how to balance an imbalanced dataset by
reducing the number of observations in the majority class.
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


# Downsample majority class
df_majority_downsampled = resample(
    df_majority,
    replace=False,
    n_samples=len(df_minority),
    random_state=42
)


# Combine minority and downsampled majority classes
df_downsampled = pd.concat([
    df_minority,
    df_majority_downsampled
])


print("\nClass distribution after downsampling:")
print(df_downsampled["target"].value_counts())


"""
Original:

Class 0 → 900
Class 1 → 100

After downsampling:

Class 0 → 100
Class 1 → 100

Downsampling reduces the majority class.

replace=False is used because we select
a smaller number of existing observations.

Important:
900 + 100 = 1000
100 + 100 = 200

Therefore, 800 observations are discarded.
"""