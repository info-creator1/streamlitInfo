import streamlit as st
import google.generativeai as genai
import PyPDF2
genai.configure(api_key="AIzaSyAnn_UrQdTnTi5LMy1H7CG_w-77QwRA7ZI")

model = genai.GenerativeModel("gemini-2.5-pro")

st.set_page_config(page_title="PDF Chatbot using Gemini")
st.title("PDF Chatbot using Gemini")
st.write("Upload a PDF, then ask questions from it")

#this creates a button that lets user upload a pdf file
pdf_file = st.file_uploader("Upload your pdf file",type=['pdf'])

if pdf_file is not None:
  pdf_reader = PyPDF2.PdfReader(pdf_file)#it reads the uploaded pdf
  full_text = ""

  for i in pdf_reader.pages: #10 pages
    full_text = full_text + i.extract_text()
  st.success("uploaded")
  context = ("use foll text to answer" + full_text)  
  question = st.text_input("As question about pdf")
  if st.button("Get answer"):
    if question.strip():
      with st.spinner("Thinking"):
        response = model.generate_content(context + "Question\n" + question)
        answer = response.text
        st.success("\nHere is the answer")
        st.write(answer)
    else:
      st.warning("please enter question")
st.caption("made with love")        




