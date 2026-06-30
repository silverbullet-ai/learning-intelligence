import streamlit as st

st.title("Practice")

number = st.number_input("Enter a Number")

if st.button("Square"):

    st.write(number ** 2)

option = st.radio(

    "Choose One",

    ["AI", "ML", "DL"]

)

st.write(option)