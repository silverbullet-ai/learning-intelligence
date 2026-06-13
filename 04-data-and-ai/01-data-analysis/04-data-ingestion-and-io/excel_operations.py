import pandas as pd

df = pd.read_excel(
    "../../resources/datasets/data.xlsx",
    sheet_name="Sheet1"
)

print(df.head())