"""Label Encoding: assign numeric identifiers to categorical labels."""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


# 1. Create a dataset of nominal categories.
df = pd.DataFrame({
    "color": ["red", "blue", "green", "red", "blue", "green"]
})

print("Original DataFrame:")
print(df)

# 2. Fit the encoder and transform the categories.
label_encoder = LabelEncoder()
df["color_encoded"] = label_encoder.fit_transform(df["color"])

print("\nLabel-Encoded DataFrame:")
print(df)

# 3. Inspect the learned mapping.
print("\nLearned Category Mapping:")
for category, label in zip(label_encoder.classes_,
                           label_encoder.transform(label_encoder.classes_)):
    print(f"{category} -> {label}")

# 4. Transform new values without fitting again.
new_colors = ["red", "blue", "green"]
print("\nNew Values:", new_colors)
print("Encoded New Values:", label_encoder.transform(new_colors))

# Note: These labels are arbitrary identifiers, not meaningful ranks.
# For nominal input features, One-Hot Encoding is generally preferable.
# LabelEncoder is primarily intended for target labels (y).
