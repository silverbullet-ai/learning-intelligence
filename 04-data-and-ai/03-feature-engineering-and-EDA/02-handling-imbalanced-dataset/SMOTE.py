"""
SMOTE — Synthetic Minority Oversampling Technique

Demonstrates how SMOTE creates synthetic observations
for the minority class using interpolation.
"""

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE


# Create an imbalanced classification dataset
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_clusters_per_class=1,
    weights=[0.90, 0.10],
    random_state=12,
    n_redundant=0
)


# Convert to DataFrame
df = pd.DataFrame(
    X,
    columns=["f1", "f2"]
)

df["target"] = y


print("Original class distribution:")
print(df["target"].value_counts())


# Visualize original dataset
plt.figure(figsize=(8, 6))

plt.scatter(
    df["f1"],
    df["f2"],
    c=df["target"]
)

plt.title("Before SMOTE")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


# Create SMOTE object
oversample = SMOTE(random_state=42)


# Apply SMOTE
X_resampled, y_resampled = oversample.fit_resample(
    X,
    y
)


# Create resampled DataFrame
df_resampled = pd.DataFrame(
    X_resampled,
    columns=["f1", "f2"]
)

df_resampled["target"] = y_resampled


print("\nClass distribution after SMOTE:")
print(df_resampled["target"].value_counts())


# Visualize SMOTE dataset
plt.figure(figsize=(8, 6))

plt.scatter(
    df_resampled["f1"],
    df_resampled["f2"],
    c=df_resampled["target"]
)

plt.title("After SMOTE")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()


"""
Before SMOTE:

Class 0 → approximately 900
Class 1 → approximately 100

After SMOTE:

Class 0 → approximately 900
Class 1 → approximately 900

SMOTE does not simply duplicate minority observations.

It identifies nearby minority observations and generates
synthetic observations through interpolation.

Memory:

SMOTE =
Find nearby minority points
→ interpolate between them
→ create synthetic minority points
→ balance the dataset
"""