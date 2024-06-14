from dotenv import load_dotenv
load_dotenv() ## loading all the env variables


import streamlit as st
import os
import google.generativeai as genai
# os.environ["GOOGLE_API_KEY"] = ["AIzaSyBX9oImBSUMyDLncB8EgTfKAJ4PQ8PvkC8"]
# os.environ["GOOGLE_API_KEY"] = "AIzaSyBX9oImBSUMyDLncB8EgTfKAJ4PQ8PvkC8"
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro")

def get_generate_output(question):
    response = model.generate_content(question)
    return response.text

# initialize our streamlit app

st.set_page_config(page_title="Ques and Ans Demoo")

st.header('Gemini LLM application ',divider='rainbow')
input = st.text_input("Input" , key="input")
submit = st.button("Ask the question ")

## when submit is clicked

if submit:
    response = get_generate_output(input)
    st.subheader("The response is \n")
    st.write(response)


