"""Ordinal Encoding: preserve a meaningful order among categories."""

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder


# 1. Create a dataset with naturally ordered categories.
df = pd.DataFrame({
    "size": ["small", "medium", "large", "medium", "small", "large"]
})

print("Original DataFrame:")
print(df)

# 2. Specify the intended category order explicitly.
encoder = OrdinalEncoder(categories=[["small", "medium", "large"]])

# 3. Fit and transform. OrdinalEncoder expects a 2D input.
df["size_encoded"] = encoder.fit_transform(df[["size"]]).astype(int)

print("\nOrdinal-Encoded DataFrame:")
print(df)

# 4. Inspect the intended ordering.
print("\nCategory Order:")
for rank, category in enumerate(encoder.categories_[0]):
    print(f"{category} -> {rank}")

# 5. Transform new observations without fitting again.
new_sizes = pd.DataFrame({"size": ["small", "medium", "large"]})
print("\nNew Values:")
print(new_sizes)
print("Encoded New Values:")
print(encoder.transform(new_sizes).astype(int))

# Note: 0 < 1 < 2 preserves small < medium < large.
