import pandas as pd

df = pd.read_csv("'../../resources/datasets/wine.csv")

print(df.head())

df.to_csv("../../resources/examples/output.csv", index=False)