import streamlit as st

st.set_page_config(page_title="Mood Player 🎶🎬", page_icon="🎧", layout="centered")

st.title("🎬 Mood-Based Audio & Video Player 🎶")

st.write("Pick a mood and enjoy matching audio + video!")

# Mood options
moods = {
    "😊 Happy": {
        "video": "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4",
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    },
    "😌 Calm": {
        "video": "https://sample-videos.com/video123/mp4/720/sample-5s.mp4",
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"
    },
    "⚡ Excited": {
        "video": "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_2mb.mp4",
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
    },
    "👻 Spooky": {
        "video": "https://sample-videos.com/video123/mp4/720/sample-10s.mp4",
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
    }
}

# Select mood
choice = st.radio("Choose a mood 🎭", list(moods.keys()))

# Display video
st.subheader(f"Video for {choice}")
st.video(moods[choice]["video"])

# Play audio
st.subheader(f"Audio for {choice}")
st.audio(moods[choice]["audio"])
