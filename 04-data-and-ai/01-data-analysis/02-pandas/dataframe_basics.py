import pandas as pd

data = {
    "Name": ["Aahish", "Manav"],
    "Age": [24, 23],
    "City": ["Gaya", "Bengaluru"]
}

df = pd.DataFrame(data)

print(df)

print("\nType:")
print(type(df))

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)