import streamlit as st
import random

st.title("🎵 Mood Based Audio and Video Player")

st.write("Pick a mood and enjoy matching video and audio")

moods = {
    "Happy" : {
        "video" : "https://www.youtube.com/watch?v=0st0DkIoS-w",
        "audio" : "happy.mp3"
    }

    "Calm" : {
        "video" : "https://www.youtube.com/watch?v=OPqFiADJPMM",
        "audio" : "calm.mp3"
    }

    "Excited" : {
        "video" : "https://www.youtube.com/watch?v=tKx1FVdyhzg",
        "audio" : "excited.mp3"
    }

    "Spooky" : {
        "video" : "https://www.youtube.com/watch?v=f5-EbZSyfjs",
        "audio" : "spooky.mp3"
    } 
}

choice = st.radio("Choose a mood:",list(moods.keys())

if st.button("Surprise Me!"):
  choice = random.choice(list(moods.keys())   

st.subheader(f"Video for {choice}")    
st.video(moods[choice]["video"])                                  
st.subheader(f"Audio for {choice}")    
st.video(moods[choice]["audio"])
                         
