import streamlit as st
import google.generativeai as genai
import base64
from io import BytesIO
from PIL import Image
import os

# ---------------------------
# 🌟 PAGE SETUP
# ---------------------------

st.set_page_config(page_title="🎨 AI Text-to-Drawing Generator", page_icon="🖍️")
st.title("🎨 AI Text-to-Drawing Generator")
st.write("Type anything fun — like *‘A robot watering flowers in space’* — and AI will draw it for you! 🚀")

# ---------------------------
# 🧠 GEMINI SETUP
# ---------------------------

genai.configure(api_key="AIzaSyAnn_UrQdTnTi5LMy1H7CG_w-77QwRA7ZI")

# ---------------------------
# ✨ IMAGE GENERATION FUNCTION
# ---------------------------

def generate_image(user_prompt):
    """Generate image using Gemini-2.5-Flash-Image model."""
    model = genai.GenerativeModel("gemini-2.5-flash-image")

    try:
        response = model.generate_content([
            f"Create a colorful, cute, and kid-friendly digital drawing of: {user_prompt}"
        ])
        image_data = response.candidates[0].content.parts[0].inline_data.data
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        return image
    except Exception as e:
        st.error(f"Image generation failed: {e}")
        return None

# ---------------------------
# 🎨 MAIN APP INTERFACE
# ---------------------------

user_prompt = st.text_input("🖊️ What should I draw?", placeholder="e.g. A panda painting a rainbow")

if st.button("✨ Generate Drawing"):
    if user_prompt.strip():
        with st.spinner("AI is creating your masterpiece... 🎨✨"):
            image = generate_image(user_prompt)
            if image:
                st.image(image, caption=user_prompt, use_container_width=True)

                # Download option
                buf = BytesIO()
                image.save(buf, format="PNG")
                st.download_button(
                    label="📥 Download This Drawing",
                    data=buf.getvalue(),
                    file_name="ai_drawing.png",
                    mime="image/png"
                )
    else:
        st.warning("Please type something to draw!")

st.markdown("---")
st.caption("Created with ❤️ by Early Coders | Powered by Gemini-2.5-Flash-Image + Streamlit")
