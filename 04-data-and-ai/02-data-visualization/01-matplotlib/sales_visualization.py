import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv("../assets/sales_data.csv")

total_sales = (
    sales_data
    .groupby("Product")["Revenue"]
    .sum()
)

total_sales.plot(
    kind="bar"
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.show()