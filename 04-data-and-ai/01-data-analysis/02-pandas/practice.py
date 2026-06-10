import pandas as pd

students = {
    "Name": ["Aahish", "Manav"],
    "Age": [24, 23],
    "Marks": [95, 97]
}

df = pd.DataFrame(students)

print("Original DataFrame:")
print(df)

print("\nFirst Row:")
print(df.head(1))

print("\nMarks Column:")
print(df["Marks"])

# Add Grade Column
df["Grade"] = ["A", "A"]

print("\nWith Grade Column:")
print(df)

print("\nStatistics:")
print(df.describe())