import pandas as pd

# Series from List
data = [1, 2, 3, 4, 5]

series = pd.Series(data)

print(series)

# Series from Dictionary
data_dict = {
    "A": 10,
    "B": 20,
    "C": 30
}

series_dict = pd.Series(data_dict)

print("\nSeries from Dictionary:")
print(series_dict)

# Custom Index
series_custom = pd.Series(
    [100, 200, 300],
    index=["X", "Y", "Z"]
)

print("\nCustom Index:")
print(series_custom)