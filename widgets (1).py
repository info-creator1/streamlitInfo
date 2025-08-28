
import streamlit as st

age = st.slider("pick your age",1.0,100.0,1.0)
st.write(f"You selected age as  {age}")
