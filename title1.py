import streamlit as st

# Main Title
st.title("📌 This is the Main Title")

# Section Heading
st.header("💠 This is a Section Heading")

# Subheading
st.subheader("✅ This is a Subheading")

# Normal Paragraph
st.write("➡️ This is normal paragraph text. It's great for descriptions.")

# Markdown with custom bold, italic, and Google link
st.markdown(
    """
    ✨ Here is some **I am in bold**, *I am in Italic*,  
    and a [link to Google](https://www.google.com) 🚀
    """,
    unsafe_allow_html=True
)

# Colored text examples
st.markdown(
    """
    <span style="color:red;">🔴 I am red text</span><br>
    <span style="color:green;">🟢 I am green text</span><br>
    <span style="color:blue;">🔵 I am blue text</span>
    """,
    unsafe_allow_html=True
)

# Caption (small text)
st.caption("📝 This is a small caption text.")
