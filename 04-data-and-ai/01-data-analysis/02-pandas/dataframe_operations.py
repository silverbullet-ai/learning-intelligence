import pandas as pd

data = {
    "Name": ["Aahish", "Manav"],
    "Age": [24, 23],
    "City": ["Gaya", "Bengaluru"]
}

df = pd.DataFrame(data)

# Add Column
df["Salary"] = [50000, 60000]

print("After Adding Salary:")
print(df)

# Update Column
df["Age"] = df["Age"] + 1

print("\nAfter Updating Age:")
print(df)

# Drop Column
df.drop("Salary", axis=1, inplace=True)

print("\nAfter Removing Salary:")
print(df)

# Drop Row
df.drop(0, inplace=True)

print("\nAfter Removing Row 0:")
print(df)