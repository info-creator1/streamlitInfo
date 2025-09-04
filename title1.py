import streamlit as st

st.title("🎥My Photo Album")

#upload multiple image files
uploaded_files = st.file_uploader("Upload one or more images", type = ["png","jpg","jpeg"],
                                  accept_multiple_files = True)

if uploaded_files:
  img_width = st.slider("Resize Image Width",100,500,250)

  captions = []

  for i, file in enumerate(uploaded_files):
    caption = st.text_input(f"My Image no {i + 1}")
    captions.append(caption)

  #show uploaded images with respective captions
  st.image(uploaded_files, caption = captions, width = img_width) 

  st.success("Your photo album is displayed above")

else:
  st.info("Please upload one or more images to get started")






