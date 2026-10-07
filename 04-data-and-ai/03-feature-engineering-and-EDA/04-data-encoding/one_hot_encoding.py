"""
One-Hot Encoding Example

Demonstrates:
- Creating categorical data
- OneHotEncoder
- fit_transform()
- Sparse matrix
- Converting to array
- Feature names
- Creating an encoded DataFrame
- Concatenating encoded data
- Transforming new data
"""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder


# 1. Create the Dataset

df = pd.DataFrame({
    "color": [
        "red",
        "blue",
        "blue",
        "green",
        "green",
        "red",
        "blue"
    ]
})

print("Original DataFrame:")
print(df)


# 2. Create the Encoder

encoder = OneHotEncoder()


# 3. Fit and Transform

encoded = encoder.fit_transform(df[["color"]])

print("\nEncoded Sparse Matrix:")
print(encoded)


# 4. Convert Sparse Matrix to Normal Array

encoded_array = encoded.toarray()

print("\nEncoded Array:")
print(encoded_array)


# 5. Get Feature Names

feature_names = encoder.get_feature_names_out()

print("\nEncoded Feature Names:")
print(feature_names)


# 6. Create a DataFrame from Encoded Data

encoded_df = pd.DataFrame(
    encoded_array,
    columns=feature_names
)

print("\nEncoded DataFrame:")
print(encoded_df)


# 7. Concatenate with Original DataFrame

df_encoded = pd.concat(
    [df, encoded_df],
    axis=1
)

print("\nCombined DataFrame:")
print(df_encoded)


# 8. Transform New Data

new_data = [["blue"]]

new_encoded = encoder.transform(new_data)

print("\nNew Data Encoded:")
print(new_encoded.toarray())


# Important:
# Training data:
# encoder.fit_transform(...)

# New data:
# encoder.transform(...)
#
# We do not fit the encoder again on new data.
