import streamlit as st
from datetime import date

# 🎉 Title with style
st.markdown("<h2 style='color: purple;'>🎂 Emoji Birthday Card Creator 🎂</h2>", unsafe_allow_html=True)

# 🎈 Ask for Birthday
bday = st.date_input("📅 Pick your Birthday:")

# ✍️ Ask for a fun message
message = st.text_area("💌 Write your Birthday Message:")

# 🎁 Button to create card
if st.button("🎉 Make My Card!"):
    if not message.strip():
        st.error("❌ Oops! You forgot to write your message!")
    else:
        # Show card
        st.image("HB.gif")

        st.markdown(
            f"""
            <div style='border: 3px solid purple; border-radius: 15px; padding: 15px; background-color: #ffe6ff;'>
                <h2 style='color: purple;'>💜 Happy Birthday! 💜</h2>
                <p style='font-size:18px; color: black;'>{message}</p>
                <p style='font-size:16px;'>🎂 Your Birthday is on: <b>{bday}</b></p>
                <p style='font-size:20px;'>🎉🥳🎈 Have the best day ever! 🎁🍰🎊</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.success("✅ Your Birthday Card is ready!")
        st.info("ℹ️ You can share this with your friends!")
        st.warning("⚠️ Don’t eat too much cake! 🍰😅")
