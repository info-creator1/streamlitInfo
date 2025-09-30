import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyACpzKhjB4-_ESpBFqt9LZP0-KUPxfXWTk")  # replace with your key

model = genai.GenerativeModel('gemini-2.5-pro')

st.write("testing")
