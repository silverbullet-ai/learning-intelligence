# Streamlit Machine Learning Application

## Overview

One of Streamlit's greatest strengths is its ability to integrate Machine Learning models into interactive web applications using only Python.

In this project, we build a simple Machine Learning classification application that predicts the species of an Iris flower based on user-provided measurements.

The application demonstrates the complete workflow of deploying a Machine Learning model—from loading a dataset and training a model to collecting user input and displaying predictions through an intuitive web interface.

---

# Learning Objectives

In this project, you will learn:

- Loading datasets using Scikit-learn
- Caching data with Streamlit
- Training a Random Forest Classifier
- Selecting features and target variables
- Creating interactive UI components
- Collecting user input using sliders
- Making predictions with a trained model
- Displaying prediction results
- Building an end-to-end Machine Learning application

---

# Required Libraries

```python
import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
```

---

# Installing Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`

```text
streamlit
pandas
scikit-learn
```

---

# Project Workflow

The application follows the workflow below:

```
Load Iris Dataset

        ↓

Create DataFrame

        ↓

Train Random Forest Model

        ↓

Create Streamlit Interface

        ↓

Collect User Input

        ↓

Generate Prediction

        ↓

Display Result
```

---

# Iris Dataset

The Iris dataset is one of the most popular datasets used for learning Machine Learning classification algorithms.

It contains measurements from three different species of Iris flowers.

### Input Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target Classes

- Setosa
- Versicolor
- Virginica

---

# Loading the Dataset

The dataset is loaded using Scikit-learn and converted into a Pandas DataFrame.

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

# Why Use `@st.cache_data`?

Without caching, Streamlit reloads the dataset every time the application refreshes.

Without cache:

```
Load Dataset

↓

Refresh Page

↓

Reload Dataset
```

With cache:

```
Load Dataset

↓

Store in Cache

↓

Future Requests

↓

Reuse Cached Data
```

Benefits:

- Faster application startup
- Reduced processing time
- Better user experience

---

# Preparing the Dataset

Load the dataset:

```python
df, target_names = load_data()
```

The function returns:

- A Pandas DataFrame containing the flower measurements
- A list of species names

---

# Building the Machine Learning Model

The project uses the Random Forest Classifier.

```python
model = RandomForestClassifier(
    random_state=42
)
```

Random Forest is an ensemble learning algorithm that combines multiple decision trees to produce more accurate and stable predictions.

---

# Training the Model

Train the classifier using:

```python
model.fit(

    df.iloc[:, :-1],

    df.iloc[:, -1]

)
```

### Feature Matrix (X)

```python
df.iloc[:, :-1]
```

Contains:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

### Target Vector (Y)

```python
df.iloc[:, -1]
```

Contains:

- Flower Species

---

# Creating the User Interface

Streamlit sliders allow users to provide flower measurements interactively.

Example:

```python
st.slider()
```

Four sliders are created for:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The selected values become the input for the model.

---

# Creating the Input Data

User selections are stored as:

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
[[5.1, 3.5, 1.4, 0.2]]
```

---

# Making Predictions

Generate predictions using:

```python
prediction = model.predict(input_data)
```

The model returns a numerical class label.

Possible outputs:

```
0

1

2
```

---

# Mapping Predictions

Convert the numerical prediction into a readable flower name.

```python
prediction_species = target_names[
    prediction[0]
]
```

Example:

```
Prediction

↓

2

↓

Virginica
```

---

# Displaying Results

The prediction is displayed using Streamlit.

```python
st.success(
    f"Predicted Species: {prediction_species.title()}"
)
```

Example Output:

```
Predicted Species

Virginica
```

---

# Streamlit Components Used

### Cache

```python
@st.cache_data
```

Caches processed data for improved performance.

---

### Slider

```python
st.slider()
```

Collects user input interactively.

---

### Success

```python
st.success()
```

Displays prediction results in a highlighted success message.

---

### DataFrame

```python
st.dataframe()
```

Displays the selected feature values in a structured table.

---

# Running the Application

Run the application using:

```bash
streamlit run classification.py
```

By default, Streamlit launches the application at:

```
http://localhost:8501
```

---

# Why Use Streamlit for Machine Learning?

Traditional deployment often requires multiple technologies.

```
Machine Learning Model

↓

Flask / Django

↓

HTML

↓

CSS

↓

JavaScript

↓

Web Application
```

Using Streamlit:

```
Machine Learning Model

↓

Python

↓

Streamlit

↓

Interactive Web Application
```

Advantages:

- Pure Python development
- No frontend technologies required
- Rapid prototyping
- Interactive user interface
- Ideal for AI and Data Science projects

---

# Real-World Applications

This workflow can be extended to build:

- Classification Systems
- Regression Applications
- Recommendation Engines
- AI Assistants
- LLM Chatbots
- Data Analytics Dashboards
- Data Exploration Tools
- Proof of Concept (POC) Applications

---

# Best Practices

- Cache datasets using `@st.cache_data`.
- Separate data loading, model training, and UI logic.
- Store datasets inside the `resources/` directory.
- Keep project dependencies inside `requirements.txt`.
- Use meaningful widget labels.
- Display predictions in a user-friendly format.
- Organize Streamlit applications into reusable components for larger projects.

---

### How is the predicted class converted into a flower name?

By indexing the `target_names` array using the predicted class label.

---

# Key Takeaways

- Streamlit enables rapid deployment of Machine Learning models using only Python.
- The Iris dataset is used to demonstrate a multiclass classification problem.
- `@st.cache_data` improves application performance by caching processed data.
- Random Forest is used to train the classification model.
- Interactive widgets allow users to provide feature values dynamically.
- Predictions are generated in real time and displayed through an intuitive web interface.
- Streamlit significantly reduces the complexity of deploying Machine Learning applications by eliminating the need for traditional frontend development.