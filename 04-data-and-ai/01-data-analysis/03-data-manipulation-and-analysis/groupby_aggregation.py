import pandas as pd

data = {
    "Region": ["North", "North", "South", "South"],
    "Sales": [50000, 45000, 30000, 35000]
}

df = pd.DataFrame(data)

print(
    df.groupby("Region")["Sales"].mean()
)

print(
    df.groupby("Region")["Sales"].sum()
)

print(
    df.groupby("Region")["Sales"].agg(
        ["mean", "sum", "count"]
    )
)