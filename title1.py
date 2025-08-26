import streamlit as st

# Main Title
st.title("📌 This is the Main Title")

# Section Heading
st.header("💠 This is a Section Heading")

# Subheading
st.subheader("✅ This is a Subheading")

# Normal Paragraph
st.write("➡️ This is normal paragraph text. It's great for descriptions.")

# Markdown with bold, italic, link, and colors
st.markdown(
    """
    ✨ Here is some **I am in bold**, *I am italic*, and a [link to Google](https://www.google.com/) 🚀  
    <br>
    <span style="color:red;">🔴 This is red text</span><br>
    <span style="color:green;">🟢 This is green text</span><br>
    <span style="color:blue;">🔵 This is blue text</span><br>
    """,
    unsafe_allow_html=True
)

# Caption (small text)
st.caption("📝 This is a small caption text.")
