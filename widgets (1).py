
import streamlit as st

age = st.slider("pick your age",1,100,20)
st.write(f"You selected age as  {age}")
