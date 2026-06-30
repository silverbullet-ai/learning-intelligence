import streamlit as st
import pandas as pd

st.title('File Uploader')

data = {
    "Name":['Lamborghini', 'Toyota', 'Tesla'],
    "Car":["Revuelto", "Etios Liva", "Model S"],
    "City":["Italy", "Japan", "America"]
}

# File Creation
df = pd.DataFrame(data)
df.to_csv('../resources/sampledata.csv')

# File Uploader
uploaded_file = st.file_uploader('Choose a CSV file', type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)