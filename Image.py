import streamlit as st
import requests
from PIL import Image
from io import BytesIO

API_KEY = "sk-yV29jKQEtmv4ZwXGLx6d04I6huWtR4kpndoLhIT1VFJjocD7"
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

st.title("AI Picture Maker")
st.write("Type anything and AI will draw it!")

prompt = st.text_input("What should AI draw?")

if st.button("Generate Image"):
  if prompt:
    st.info("Please wait..AI is creating your image!")

    headers = {
        "Authorization":f"Bearer {API_KEY}",
        "Accept":"image/*"
    }
    files={
        'prompt':(None,prompt),
        'output_format':(None,'png')
    } 

    response = requests.post(API_URL,headers=headers,files=files)

    if response.status_code == 200:
      image = Image.open(BytesIO(response.content))
      st.image(image,caption="Here's your AI generated image")
      st.download_button("Download Image",response.content,"AI_picture.png","image/png")
    else:
      st.error("Try Again")
