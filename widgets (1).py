import streamlit as st
import random

st.set_page_config(page_title="Mood Player 🎶🎬", page_icon="🎧", layout="centered")

st.title("🎬 Mood-Based Audio & Video Player 🎶")

st.write("Pick a mood and enjoy matching audio + video! (All media is Creative Commons licensed)")

# 🎥 Mood options with CC YouTube videos + free music
moods = {
    "😊 Happy": {
        "video": ""https://www.youtube.com/watch?v=0st0DkIoS-w"",  # CC Stock Footage
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    },
    "😌 Calm": {
        "video": "https://www.youtube.com/watch?v=OPqFiADJPMM",  # CC explainer
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    },
    "⚡ Excited": {
        "video": "https://www.youtube.com/watch?v=4b9_OzecYQg",  # CC video
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    },
    "👻 Spooky": {
        "video": "https://www.youtube.com/watch?v=ezJB6_cFD2I",  # YouTube CC demo video
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
    }
}

# User choice
choice = st.radio("Choose a mood 🎭", list(moods.keys()))

# Add a "Surprise Me" button
if st.button("🎲 Surprise Me!"):
    choice = random.choice(list(moods.keys()))

# Show video
st.subheader(f"Video for {choice}")
st.video(moods[choice]["video"])

# Play audio
st.subheader(f"Audio for {choice}")
st.audio(moods[choice]["audio"])
