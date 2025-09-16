import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("🍭 Candy Sales Dashboard for Kids 🍬")

# Create fake candy sales data
np.random.seed(42)
days = pd.date_range("2025-01-01", periods=7)  # 1 week
candy_types = ["Lollipop", "Chocolate", "Gummy Bears"]

# Random sales numbers
data = {
    "Day": days,
    "Lollipop": np.random.randint(20, 100, size=7),
    "Chocolate": np.random.randint(30, 120, size=7),
    "Gummy Bears": np.random.randint(10, 80, size=7),
}

df = pd.DataFrame(data)

# ---- DISPLAY DATA ----
st.subheader("📋 Candy Sales Table")
st.table(df)  # simple table

st.subheader("📊 Candy Sales DataFrame (interactive)")
st.dataframe(df)  # interactive version

# ---- METRICS ----
st.subheader("✨ Sales Highlights")
st.metric("Best Lollipop Sale", f"{df['Lollipop'].max()} 🍭")
st.metric("Best Chocolate Sale", f"{df['Chocolate'].max()} 🍫")
st.metric("Best Gummy Bears Sale", f"{df['Gummy Bears'].max()} 🐻")

# ---- CHARTS ----
st.subheader("📈 Candy Sales Over Time")
st.line_chart(df.set_index("Day"))  # line chart

st.subheader("📊 Candy Sales Comparison")
st.bar_chart(df.set_index("Day"))   # bar chart

st.subheader("🌈 Candy Sales Growth")
st.area_chart(df.set_index("Day"))  # area chart
