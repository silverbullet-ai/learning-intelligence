"""Target-guided ordinal encoding: mean and median target mapping.

Educational demonstration of the lecture's City–Price example.
For production ML, fit mappings on training data only and consider
out-of-fold encoding for training rows to reduce target leakage.
"""

import pandas as pd


# 1. Create the dataset

df = pd.DataFrame(
    {
        "city": ["London", "New York", "Paris", "Tokyo", "New York", "Paris"],
        "price": [150, 200, 320, 250, 180, 300],
    }
)
print("Original DataFrame:")
print(df)


# 2. Calculate mean target value for each category
mean_price = df.groupby("city")["price"].mean().to_dict()
print("\nMean price mapping:")
print(mean_price)


# 3. Map categories to their mean target values
df["city_encoded"] = df["city"].map(mean_price)
print("\nMean target-encoded DataFrame:")
print(df)


# 4. Optional: use median instead of mean
median_price = df.groupby("city")["price"].median().to_dict()
df["city_median_encoded"] = df["city"].map(median_price)
print("\nWith median target encoding:")
print(df)


# 5. Transform new categories using the existing mean mapping
# Use the overall mean as a fallback for a category not in the mapping.
new_data = pd.DataFrame({"city": ["Paris", "Berlin"]})
new_data["city_encoded"] = (
    new_data["city"].map(mean_price).fillna(df["price"].mean())
)
print("\nNew observations (Berlin uses the overall mean fallback):")
print(new_data)

# IMPORTANT: In real ML, derive mappings using training data only.
# Out-of-fold target encoding is preferable for encoding training rows.
