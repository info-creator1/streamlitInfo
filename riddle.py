import streamlit as st
import google.generativeai as genai

#Page setup
st.set_page_config(page_title="AI Riddle Generator")
st.title("Riddle generator")
st.write("Get fun riddles for kids! Solve them yourself or click the button to see the answer")

#Gemini setup
genai.configure(api_key="AIzaSyAKVsWpUSlPHoK57ByKCuUth5QFX4kDaXo")

def generate_riddle():
  """Generates a user-friendly riddle with its answer"""
  prompt = ("Generate one short, fun, and kid friendly riddle"
  "Provide the riddle first, and then the answer."
  "Format it as: Riddle: ... Answer: ...")

  model = genai.GenerativeModel("gemini-2.5-pro")
  response = model.generate_content(prompt)
  return response.text.strip()

#main app with session state
# Initialise session state
if "riddle" not in st.session_state:
  st.session_state.riddle = ""  
if "answer" not in st.session_state:
  st.session_state.answer = "" 
if "show_answer" not in st.session_state:
  st.session_state.show_answer = False   

#Generate Riddle button
if st.button("Generate Riddle"):
  riddle_text = generate_riddle()#function call  
  if "Answer:" in riddle_text:
    riddle1,answer1 = riddle_text.split("Answer:",1)
    st.session_state.riddle = riddle1
    st.session_state.answer = answer1
    st.session_state.show_answer = False  
  else:
    st.session_state.riddle = riddle_text 
    st.session_state.answer = ""
    st.session_state.show_answer = False 

 #Display riddle
if st.session_state.riddle:
  st.write(st.session_state.riddle)

  #show answer button
  if st.button("Show Answer"):
    st.session_state.show_answer = True

#Display answer if requested
if st.session_state.show_answer  and st.session_state.answer:
  st.success(st.session_state.answer) 
