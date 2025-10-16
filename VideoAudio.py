import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
import base64
import google.generativeai as genai
import os

# ---------------------------
# 🌟 PAGE SETUP
# ---------------------------
st.set_page_config(page_title="🎨 AI Doodle Critic", page_icon="🖍️")
st.title("🎨 AI Doodle Critic")
st.write("Draw something fun on the canvas below, and the AI will give you a **kid-friendly review**! 😄")

# ---------------------------
# 🧠 GEMINI SETUP
# ---------------------------
genai.configure(api_key="AIzaSyCSBRzHltNJCf6TUfXu9KjqFV3y_pJUocQ")

# ---------------------------
# 🖌️ CANVAS SETUP
# ---------------------------
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Orange fill for fun
    stroke_width=5,
    stroke_color="#000000",
    background_color="#ffffff",
    height=300,
    width=400,
    drawing_mode="freedraw",
    key="doodle_canvas"
)

# ---------------------------
# ✨ AI CRITIC FUNCTION
# ---------------------------
def generate_critique(image_bytes):
    """
    Sends the drawing to Gemini (or text API) and gets a fun critique.
    We describe the image as a text-based review.
    """
    model = genai.GenerativeModel("models/gemini-2.5-flash-image")

    prompt = (
        "You are a fun and friendly AI art critic for kids. "
        "Look at this drawing and give a creative, encouraging, and funny comment in 1-2 sentences: "
        f"{image_bytes[:50]}... (describe the drawing as if you saw it)"
    )
    response = model.generate_content(prompt)
    return response.text.strip()

# ---------------------------
# 🎨 GENERATE CRITIQUE BUTTON
# ---------------------------
if st.button("🖍️ Get AI Critique"):
    if canvas_result.image_data is not None:
        # Convert canvas image to bytes
        img = Image.fromarray(canvas_result.image_data.astype("uint8"), "RGBA")
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        image_bytes = buf.getvalue()

        # Generate critique
        with st.spinner("AI is thinking of a fun comment... 🤔🎨"):
            critique = generate_critique(base64.b64encode(image_bytes).decode("utf-8"))
            st.subheader("🤖 AI Critique:")
            st.success(critique)
    else:
        st.warning("Please draw something first!")

st.markdown("---")
st.caption("Created with ❤️ by Early Coders | Powered by Gemini + Streamlit")
