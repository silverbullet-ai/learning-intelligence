import pandas as pd

data = {
    "Name": ["Aahish", "Manav"],
    "Age": [24, 23]
}

df = pd.DataFrame(data)

df.to_pickle("../../resources/examples/data.pkl")

loaded_df = pd.read_pickle("../../resources/examples/data.pkl")

print(loaded_df)