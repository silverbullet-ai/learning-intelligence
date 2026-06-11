import pandas as pd
import numpy as np

data = {
    "Product": ["Laptop", "Phone", "Tablet"],
    "Sales": [50000, np.nan, 25000]
}

df = pd.DataFrame(data)

print(df.isnull())

print(df.isnull().sum())

df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

print(df)