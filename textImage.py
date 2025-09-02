import streamlit as st
st.title("My file uploader playground")

#upload homework(only text files allowed")
hw_files = st.file_uploader("Upload your HW text files", type = ["txt","pdf"]
                            , accept_multiple_files=True,key="homework")

if hw_files:
  st.write("Your HW files uploaded succesfully")
  for i in hw_files:
    st.write(i.name)

#upload homework(only text files allowed")
dr_files = st.file_uploader("Upload your DR files", type = ["png","jpg","jpeg"]
                            , accept_multiple_files=True,key="drawing")

if dr_files:
  st.write("Your DR files uploaded succesfully")
  for i in dr_files:
    st.image(i,width=200)     
