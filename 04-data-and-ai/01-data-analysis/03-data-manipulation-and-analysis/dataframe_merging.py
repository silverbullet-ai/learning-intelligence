import pandas as pd

df1 = pd.DataFrame({
    "Key": ["A", "B", "C"],
    "Value1": [1, 2, 3]
})

df2 = pd.DataFrame({
    "Key": ["A", "B", "D"],
    "Value2": [4, 5, 6]
})

print(pd.merge(df1, df2, on="Key", how="inner"))

print(pd.merge(df1, df2, on="Key", how="outer"))

print(pd.merge(df1, df2, on="Key", how="left"))

print(pd.merge(df1, df2, on="Key", how="right"))