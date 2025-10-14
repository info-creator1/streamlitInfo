#Story Generator tool
import streamlit as st
import google.generativeai as genai

#set Gemini API key
genai.configure(api_key="AIzaSyAnn_UrQdTnTi5LMy1H7CG_w-77QwRA7ZI")

#Load gemini model
model = genai.GenerativeModel("gemini-2.5-pro")

#streamlit app
st.set_page_config(page_title="Text to Story Gen AI Tool",page_icon="📜")

st.title("AI Story Generator")
st.write("Enter your idea and get a magical story!")

#Input box
prompt = st.text_input("Enter your story idea")

#create button to generate story
if st.button("Generate Story"):
  if prompt.strip() != "":
    with st.spinner("Thinking..."):
      response = model.generate_content(prompt + "Create a fun and simple story")
      story = response.text
      st.success("Here's your story:")
      st.write(story)
  else:
    st.warning("Please enter something to get a story") 
#Footer
st.caption("Made with streamlit and Gemini AI")  



