import streamlit as st

st.title("🎂 Birthday Age Calculator")

name = st.text_input("Enter your name:")
birth_year = st.number_input("Enter your birth year:", min_value=1900, max_value=2100, step=1)

if name and birth_year:
    current_year = 2025
    age = current_year - birth_year
    st.write(f"Hello {name}, you are **{age} years old**! 🎉")
