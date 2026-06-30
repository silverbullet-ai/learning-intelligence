# Streamlit Machine Learning App

## Overview

Streamlit can be combined with Machine Learning models to build interactive web applications using only Python.

In this project, a Random Forest Classifier is trained using the Iris dataset, allowing users to interactively provide flower measurements through Streamlit sliders and receive instant predictions.

This demonstrates a complete Machine Learning deployment workflow, from loading data to serving predictions through a web interface.

---

## Topics Covered

- Iris Dataset
- Loading Data
- Streamlit Caching
- Random Forest Classifier
- Model Training
- Feature Selection
- User Input with Sliders
- Making Predictions
- Displaying Results
- Application Workflow
- Best Practices
- Interview Questions

---

## Required Libraries

```python
import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
```

---

## Installing Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

requirements.txt

```text
streamlit
pandas
scikit-learn
```

---

## Iris Dataset

The Iris dataset is one of the most widely used datasets in Machine Learning.

Features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Target Classes:

- Setosa
- Versicolor
- Virginica

---

## Loading the Dataset

```python
@st.cache_data
def load_data():

    iris = load_iris()

    df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    df["species"] = iris.target

    return df, iris.target_names
```

---

## Why Use `@st.cache_data`?

Without caching:

```
Load Dataset

↓

Refresh Page

↓

Load Dataset Again
```

With caching:

```
Load Dataset

↓

Cache Data

↓

Future Requests

↓

Instant Loading
```

`@st.cache_data` stores processed data in memory and avoids unnecessary reloading.

---

## Loading Data

```python
df, target_names = load_data()
```

Returns:

- Feature DataFrame
- Species names

---

## Random Forest Classifier

Create the model:

```python
model = RandomForestClassifier()
```

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy.

---

## Training the Model

```python
model.fit(

    df.iloc[:, :-1],

    df.iloc[:, -1]

)
```

### Features (X)

```python
df.iloc[:, :-1]
```

Returns:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

---

### Target (Y)

```python
df.iloc[:, -1]
```

Returns:

```
Species
```

---

## User Input

Users provide flower measurements using sliders.

Example:

```python
sepal_length = st.slider(...)
```

The application creates four sliders:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

---

## Creating Input Data

```python
input_data = [[

    sepal_length,

    sepal_width,

    petal_length,

    petal_width

]]
```

Example:

```
[[5.1,3.5,1.4,0.2]]
```

---

## Making Predictions

```python
prediction = model.predict(input_data)
```

Possible outputs:

```
0

1

2
```

---

## Mapping Prediction

```python
prediction_species = target_names[
    prediction[0]
]
```

Example:

```
prediction[0] = 2

↓

Virginica
```

---

## Displaying the Prediction

```python
st.write(

    "Predicted Species:",

    prediction_species

)
```

Example:

```
Predicted Species:

Virginica
```

---

## Streamlit Components Used

### Cache

```python
@st.cache_data
```

Improves performance.

---

### Slider

```python
st.slider()
```

Collects feature values.

---

### Write

```python
st.write()
```

Displays results.

---

## Running the Application

```bash
streamlit run classification.py
```

Default URL:

```
http://localhost:8501
```

---

## Application Workflow

```
Load Iris Dataset

        ↓

Create DataFrame

        ↓

Train Random Forest

        ↓

User Inputs Features

        ↓

Create Input Array

        ↓

Model Prediction

        ↓

Display Species
```

---

## Why Streamlit for Machine Learning?

Traditional Deployment:

```
ML Model

↓

Flask

↓

HTML

↓

CSS

↓

JavaScript
```

Streamlit:

```
ML Model

↓

Python

↓

Streamlit

↓

Web Application
```

Benefits:

- Faster development
- Less code
- No frontend knowledge required
- Excellent for prototypes
- Interactive UI

---

## Real-World Applications

- Classification Apps
- Regression Apps
- AI Assistants
- LLM Chatbots
- Recommendation Systems
- Business Dashboards
- Data Exploration
- Proof of Concepts

---

## Best Practices

- Cache datasets using `@st.cache_data`.
- Separate data loading from UI logic.
- Keep model training modular.
- Store datasets inside the `resources/` folder.
- Use descriptive widget labels.
- Maintain dependencies in `requirements.txt`.

---

## One-Line Summary

This project demonstrates how Streamlit can integrate a Machine Learning model into an interactive web application, enabling users to provide feature values and receive real-time predictions using only Python.