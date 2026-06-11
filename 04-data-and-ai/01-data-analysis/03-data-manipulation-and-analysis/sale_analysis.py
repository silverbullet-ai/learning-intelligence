import pandas as pd

sales_data = {
    "Product": ["Laptop", "Phone", "Laptop", "Tablet"],
    "Region": ["North", "South", "West", "North"],
    "Sales": [50000, 30000, 45000, 25000]
}

df = pd.DataFrame(sales_data)

print(df)

print(df.describe())

avg_sales = (
    df.groupby("Product")["Sales"]
      .mean()
)

print(avg_sales)

total_sales = (
    df.groupby("Region")["Sales"]
      .sum()
)

print(total_sales)