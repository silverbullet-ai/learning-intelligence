import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Laptop", "Tablet"],
    "Sales": [50000, 30000, 45000, 20000],
    "Region": ["North", "South", "North", "West"]
}

df = pd.DataFrame(data)

print(df.head())

print(df.describe())

print(df.groupby("Product")["Sales"].mean())