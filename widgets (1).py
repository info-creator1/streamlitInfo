import streamlit as st
import random

st.set_page_config(page_title="Mood Player 🎶🎬", page_icon="🎧", layout="centered")

st.title("🎬 Mood-Based Audio & Video Player for Kids")
st.write("Pick a mood and enjoy matching video + background music!")

# Mood options with YouTube videos + Pixabay audio
moods = {
    "😊 Happy": {
        "video": "https://www.youtube.com/watch?v=0st0DkIoS-w",
        "audio": "https://cdn.pixabay.com/download/audio/2022/10/03/audio_927f9cfeb5.mp3?filename=happy-kids-11854.mp3"
    },
    "😌 Calm": {
        "video": "https://www.youtube.com/watch?v=OPqFiADJPMM",
        "audio": "https://cdn.pixabay.com/download/audio/2021/10/21/audio_4c1d71db8c.mp3?filename=calm-piano-ambient-118199.mp3"
    },
    "⚡ Excited": {
        "video": "https://www.youtube.com/watch?v=tKx1FVdyhzg",
        "audio": "https://cdn.pixabay.com/download/audio/2022/03/15/audio_3096f36c24.mp3?filename=energetic-upbeat-fun-12556.mp3"
    },
    "👻 Spooky": {
        "video": "https://www.youtube.com/watch?v=f5-EbZSyfjs",
        "audio": "https://github.com/info-creator1/streamlitInfo/blob/main/halloween-music-400868.mp3"
    }
}

choice = st.radio("Choose a mood 🎭", list(moods.keys()))

if st.button("🎲 Surprise Me!"):
    choice = random.choice(list(moods.keys()))

st.subheader(f"Video for {choice}")
st.video(moods[choice]["video"])

st.subheader(f"Sound for {choice}")
st.audio(moods[choice]["audio"])

# Attribution info
st.markdown("---")
st.markdown("**Audio from [Pixabay](https://pixabay.com/music/)** — free for all uses, no attribution required 🎶")
