
# Streamlit Introduction

## Overview

Streamlit is an open-source Python framework used to build interactive web applications directly using Python.

Unlike traditional web frameworks, Streamlit does not require knowledge of HTML, CSS, or JavaScript, making it one of the easiest tools for deploying Data Science, Machine Learning, and AI applications.

Streamlit is widely used for:

- Machine Learning Model Deployment
- Data Science Dashboards
- Data Visualization
- AI & Generative AI Applications
- Exploratory Data Analysis (EDA)
- Rapid Prototyping

---

## Topics Covered

- What is Streamlit?
- Why Streamlit?
- Installing Streamlit
- Running a Streamlit Application
- Streamlit Application Structure
- Display Components
- DataFrames
- Charts
- Input Widgets
- File Upload
- Streamlit Workflow
- Common Components
- Best Practices
- Interview Questions

---
## requirements

- streamlit
- pandas
- numpy

---

## What is Streamlit?

Streamlit is a lightweight Python framework for building interactive web applications.

Instead of creating:

```
Frontend (HTML + CSS + JavaScript)
        +
Backend (Python)
```

Streamlit allows developers to build complete applications using only Python.

Example:

```python
import streamlit as st

st.title("Hello Streamlit")
```

Output:

```
Hello Streamlit
```

---

## Why Streamlit?

Streamlit is especially popular among Data Scientists and AI Engineers because it enables rapid deployment of models and visualizations without frontend development.

Common use cases include:

- Machine Learning Model Deployment
- AI Applications
- Chatbots
- Data Dashboards
- Exploratory Data Analysis
- Business Reports
- Proof of Concepts (POCs)

Advantages:

- Pure Python development
- No HTML, CSS, or JavaScript required
- Interactive UI components
- Fast prototyping
- Easy deployment

---

## Installation

Install Streamlit using pip:

```bash
pip install streamlit
```

or include it in `requirements.txt`:

```text
streamlit
```

---

## Importing Streamlit

```python
import streamlit as st
```

The alias `st` is the standard convention used in almost every Streamlit application.

---

## Running a Streamlit Application

Create a Python file:

```
app.py
```

Run the application:

```bash
streamlit run app.py
```

Default URL:

```
http://localhost:8501
```

Stop the server:

```
Ctrl + C
```

---

## Basic Application Structure

```python
import streamlit as st

st.title("Hello Streamlit")

st.write("Welcome!")
```

Every Streamlit application starts with importing the library and adding UI components.

---

## Creating a Title

```python
st.title("Hello Streamlit")
```

Displays a large heading.

Equivalent HTML:

```html
<h1>Hello Streamlit</h1>
```

---

## Displaying Text

```python
st.write("This is a simple text.")
```

`st.write()` is the most versatile output function.

It can display:

- Text
- Numbers
- Variables
- Lists
- Dictionaries
- DataFrames
- Charts
- Images

Example:

```python
name = "Aahish"

st.write(name)
```

---

## Displaying DataFrames

```python
import pandas as pd

df = pd.DataFrame({
    "First Column":[1,2,3],
    "Second Column":[4,5,6]
})

st.write(df)
```

Features:

- Interactive table
- Scrollable
- Sortable
- CSV download support

Alternatively:

```python
st.dataframe(df)
```

or

```python
st.table(df)
```

---

## Creating Charts

Example:

```python
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["A","B","C"]
)

st.line_chart(chart_data)
```

Creates an interactive line chart.

Other chart types:

```python
st.bar_chart()

st.area_chart()
```

---

## Text Input Widget

```python
name = st.text_input("Enter your name")
```

Example:

```python
if name:

    st.write(f"Hello {name}")
```

Workflow:

```
User

 ↓

Text Input

 ↓

Python Variable

 ↓

Display Output
```

---

## Slider Widget

```python
age = st.slider(
    "Select your age",
    0,
    100,
    25
)
```

Parameters:

```python
st.slider(
    label,
    min_value,
    max_value,
    default_value
)
```

Example Output:

```
Your age is 25
```

---

## Select Box

Creates a dropdown menu.

```python
languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

choice = st.selectbox(
    "Choose your favorite language",
    languages
)

st.write(choice)
```

---

## File Upload

```python
uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type="csv"
)
```

Reading uploaded CSV:

```python
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write(df)
```

Common use cases:

- Upload datasets
- Data exploration
- Machine Learning prediction
- Report analysis

---

## Common Streamlit Components

### Text Components

```python
st.title()

st.header()

st.subheader()

st.text()

st.write()
```

---

### Input Components

```python
st.text_input()

st.number_input()

st.slider()

st.selectbox()

st.checkbox()

st.radio()

st.button()
```

---

### Data Components

```python
st.dataframe()

st.table()

st.write()
```

---

### File Components

```python
st.file_uploader()
```

---

### Visualization Components

```python
st.line_chart()

st.bar_chart()

st.area_chart()
```

---

## Typical Streamlit Workflow

```
User Input

      ↓

Streamlit Widget

      ↓

Python Processing

      ↓

Display Result
```

Example:

```
Text Input

      ↓

Python Variable

      ↓

Computation

      ↓

Display Output
```

---

## Why Streamlit is Popular in AI?

Streamlit is widely used because it makes deploying AI applications extremely simple.

Typical projects include:

- Machine Learning Model Deployment
- Deep Learning Applications
- NLP Applications
- LLM Chatbots
- Business Dashboards
- Data Exploration Tools

Benefits:

- Very fast development
- Interactive interface
- Beginner-friendly
- Pure Python
- Excellent Pandas integration

---

## Best Practices

- Keep UI code organized.
- Use descriptive widget labels.
- Store datasets inside a `resources/` folder.
- Separate data processing from UI logic.
- Use functions to organize larger applications.
- Use `requirements.txt` for dependency management.

---

## Common Beginner Mistakes

### Forgetting to Run with Streamlit

Wrong:

```bash
python app.py
```

Correct:

```bash
streamlit run app.py
```

---

### Forgetting to Import Streamlit

Error:

```
NameError:
st is not defined
```

Solution:

```python
import streamlit as st
```

---

### Forgetting to Install Streamlit

Error:

```
ModuleNotFoundError

No module named 'streamlit'
```

Solution:

```bash
pip install streamlit
```

---


## Quick Revision

```python
import streamlit as st

st.title()

st.header()

st.subheader()

st.write()

st.text_input()

st.slider()

st.selectbox()

st.file_uploader()

st.dataframe()

st.line_chart()

streamlit run app.py
```

---

## One-Line Summary

Streamlit is a lightweight Python framework that enables developers to build interactive web applications for Data Science, Machine Learning, and AI using only Python, without requiring HTML, CSS, or JavaScript.