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
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

# ---------------------------
# 🎯 MAIN APP WITH SESSION STATE
# ---------------------------

# Initialize session state
if "riddle" not in st.session_state:
    st.session_state.riddle = ""
if "answer" not in st.session_state:
    st.session_state.answer = ""
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# Generate riddle button
if st.button("✨ Generate Riddle"):
    riddle_text = generate_riddle()
    if "Answer:" in riddle_text:
        riddle, answer = riddle_text.split("Answer:", 1)
        st.session_state.riddle = riddle.strip()
        st.session_state.answer = answer.strip()
        st.session_state.show_answer = False
    else:
        st.session_state.riddle = riddle_text
        st.session_state.answer = ""
        st.session_state.show_answer = False

# Display riddle
if st.session_state.riddle:
    st.subheader("🧩 Riddle:")
    st.write(st.session_state.riddle)

    # Show answer button
    if st.button("🔍 Show Answer"):
        st.session_state.show_answer = True

# Display answer if requested
if st.session_state.show_answer and st.session_state.answer:
    st.success(st.session_state.answer)

st.markdown("---")
st.caption("Created with ❤️ by Early Coders | Powered by Gemini AI")
