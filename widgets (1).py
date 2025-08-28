
import streamlit as st

color = st.selectbox("pick your color",["Red","Green","Blue"])
st.write(f"You selected color {color}")
