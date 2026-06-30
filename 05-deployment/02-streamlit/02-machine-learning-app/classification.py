import os

import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# ----------------------------
# Load Dataset
# ----------------------------

@st.cache_data
def load_data():
    iris = load_iris()

    df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    df["species"] = iris.target

    return df, iris.target_names


df, target_names = load_data()

# ----------------------------
# Save Dataset
# ----------------------------

os.makedirs("../resources", exist_ok=True)

dataset_path = os.path.join(
    "../resources",
    "iris_dataset.csv"
)

if not os.path.exists(dataset_path):
    df.to_csv(
        dataset_path,
        index=False
    )

# ----------------------------
# Train Model
# ----------------------------

model = RandomForestClassifier(
    random_state=42
)

model.fit(
    df.iloc[:, :-1],  # Features
    df.iloc[:, -1]    # Target
)

# ----------------------------
# Streamlit UI
# ----------------------------

st.title("🌸 Iris Flower Classification App")

st.write(
    """
    Adjust the flower measurements using the sliders below.
    The model will predict the flower species.
    """
)

# ----------------------------
# User Inputs
# ----------------------------

sepal_length = st.slider(
    "Sepal Length (cm)",
    float(df.iloc[:, 0].min()),
    float(df.iloc[:, 0].max()),
    float(df.iloc[:, 0].mean())
)

sepal_width = st.slider(
    "Sepal Width (cm)",
    float(df.iloc[:, 1].min()),
    float(df.iloc[:, 1].max()),
    float(df.iloc[:, 1].mean())
)

petal_length = st.slider(
    "Petal Length (cm)",
    float(df.iloc[:, 2].min()),
    float(df.iloc[:, 2].max()),
    float(df.iloc[:, 2].mean())
)

petal_width = st.slider(
    "Petal Width (cm)",
    float(df.iloc[:, 3].min()),
    float(df.iloc[:, 3].max()),
    float(df.iloc[:, 3].mean())
)

# ----------------------------
# Prediction
# ----------------------------

input_data = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

prediction = model.predict(input_data)

prediction_species = target_names[prediction[0]]

# ----------------------------
# Output
# ----------------------------

st.subheader("Prediction")

st.success(
    f"Predicted Species: {prediction_species.title()}"
)

# ----------------------------
# Display Input Data
# ----------------------------

st.subheader("Selected Features")

input_df = pd.DataFrame(
    input_data,
    columns=df.columns[:-1]
)

st.dataframe(input_df)

# ----------------------------
# Dataset Preview
# ----------------------------

st.subheader("Iris Dataset")

st.dataframe(df.head())

st.caption(
    "A copy of the dataset is automatically saved to "
    "../resources/iris_dataset.csv"
)