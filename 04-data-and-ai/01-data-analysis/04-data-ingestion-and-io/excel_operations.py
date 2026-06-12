import pandas as pd

df = pd.read_excel(
    "../assets/data.xlsx",
    sheet_name="Sheet1"
)

print(df.head())