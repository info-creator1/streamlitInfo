import streamlit as st
import google.generativeai as genai
import os

# ---------------------------
# 🌟 PAGE SETUP
# ---------------------------
st.set_page_config(page_title="🧩 Kid Riddle Generator", page_icon="🧠")
st.title("🧩 Kid Riddle Generator")
st.write("Get fun riddles for kids! Solve them yourself, or click the button to see the answer 😄")

# ---------------------------
# 🧠 GEMINI SETUP
# ---------------------------
genai.configure(api_key="AIzaSyCSBRzHltNJCf6TUfXu9KjqFV3y_pJUocQ")

# ---------------------------
# ✨ FUNCTION TO GENERATE RIDDLE
# ---------------------------
def generate_riddle():
    """Generates a kid-friendly riddle with its answer"""
    prompt = (
        "Generate one short, fun, and kid-friendly riddle. "
        "Provide the riddle first, and then the answer. "
        "Format it as: Riddle: ... Answer: ..."
    )
    model = genai.GenerativeModel("gemini-2.5-pro")  # text model
    response = model.generate_content(prompt)
    return response.text.strip()

# ---------------------------
# 🎯 MAIN APP
# ---------------------------
if st.button("✨ Generate Riddle"):
    riddle_text = generate_riddle()
    
    # Split riddle and answer
    if "Answer:" in riddle_text:
        riddle, answer = riddle_text.split("Answer:", 1)
        st.subheader("🧩 Riddle:")
        st.write(riddle.strip())

        if st.button("🔍 Show Answer"):
            st.success(answer.strip())
    else:
        st.write(riddle_text)  # fallback

st.markdown("---")
st.caption("Created with ❤️ by Early Coders | Powered by Gemini AI")
