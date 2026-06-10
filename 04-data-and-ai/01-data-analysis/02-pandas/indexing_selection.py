import pandas as pd

data = {
    "Name": ["Aahish", "Manav"],
    "Age": [24, 23],
    "City": ["Gaya", "Bengaluru"]
}

df = pd.DataFrame(data)

# Column Access
print(df["Name"])

# loc
print("\nloc[0]")
print(df.loc[0])

# iloc
print("\niloc[0]")
print(df.iloc[0])

# at
print("\nat[1, 'Age']")
print(df.at[1, "Age"])

# iat
print("\niat[1,2]")
print(df.iat[1, 2])