import pandas as pd

data = {
    "Name": ["Aahish", "Manav"],
    "Age": [24, 23]
}

df = pd.DataFrame(data)

df.to_pickle("../assets/data.pkl")

loaded_df = pd.read_pickle("../assets/data.pkl")

print(loaded_df)