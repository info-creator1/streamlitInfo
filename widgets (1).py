
import streamlit as st

color = st.multiselect("pick your fav colors",["Red","Green","Blue","yellow"])
st.write(f"You selected color {color}")
