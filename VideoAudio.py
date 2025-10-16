import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
from io import BytesIO
import base64

# ---------------------------
# 🌟 APP SETUP
# ---------------------------

st.set_page_config(page_title="AI Drawing Prompt Generator 🎨", page_icon="🎨", layout="centered")

st.title("🎨 AI Drawing Prompt Generator")
st.write("Click below to get a **fun drawing idea** and see what it might look like — all powered by AI!")

# ---------------------------
# 🧠 GEMINI SETUP
# ---------------------------

# 🔑 Replace with your Gemini API key (keep it secret in Streamlit Cloud secrets)
genai.configure(api_key="AIzaSyAnn_UrQdTnTi5LMy1H7CG_w-77QwRA7ZI")

# ---------------------------
# ✨ FUNCTIONS
# ---------------------------

def generate_prompt():
    """Generate a fun, imaginative drawing prompt using Gemini."""
    prompt = (
        "Create a fun and creative drawing idea for kids. "
        "It should be imaginative, simple to draw, and suitable for all ages. "
        "Example: 'A panda painting a rainbow' or 'A robot watering flowers in space'. "
        "Give just one unique prompt idea."
    )
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_image(prompt_text):
    """Generate an AI image based on the drawing prompt."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    image_response = model.generate_content(
        [f"Create a colorful and cute drawing of: {prompt_text}"],
        generation_config={"response_mime_type": "image/png"}
    )
    image_data = image_response.candidates[0].content.parts[0].inline_data.data
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    return image

# ---------------------------
# 🎨 USER INTERFACE
# ---------------------------

if st.button("✨ Generate Drawing Idea"):
    with st.spinner("AI is thinking of a fun idea... 🎨"):
        idea = generate_prompt()
        st.subheader("🖍️ Your Drawing Idea:")
        st.success(idea)

        st.write("Now creating your AI drawing... please wait! 🧠🎨")
        image = generate_image(idea)
        st.image(image, caption=idea, use_container_width=True)

        # Download button
        buf = BytesIO()
        image.save(buf, format="PNG")
        st.download_button(
            label="📥 Download This Drawing",
            data=buf.getvalue(),
            file_name="ai_drawing.png",
            mime="image/png"
        )

# ---------------------------
# 🌈 FOOTER
# ---------------------------

st.markdown("---")
st.caption("Created with ❤️ by Early Coders | Powered by Gemini + Streamlit")
