import pandas as pd

df = pd.read_csv("../assets/wine.csv")

print(df.head())

df.to_csv("../assets/output.csv", index=False)