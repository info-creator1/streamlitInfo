import streamlit as st
drawing_files = st.file_uploader(
    "🎨 Upload your drawings", 
    type=["png", "jpg", "jpeg"],      # only images allowed
    accept_multiple_files=False,       # many files allowed
    key="drawings"                    # different key
)

if drawing_files:
    st.write("🖼️ Yay! You uploaded drawings:")
    for file in drawing_files:
        st.image(file, caption=file.name, width=200)
