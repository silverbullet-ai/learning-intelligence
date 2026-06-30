import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Demo")

st.header("Basic Components")

st.write("Welcome to Streamlit!")

# DataFrame
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})

st.write(df)

# Chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(chart_data)

# Text Input
name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}")

# Slider
age = st.slider("Age", 0, 100, 25)

st.write(age)

# Dropdown
language = st.selectbox(
    "Favorite Language",
    ["Python", "Java", "C++"]
)

st.write(language)