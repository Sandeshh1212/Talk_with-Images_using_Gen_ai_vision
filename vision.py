from dotenv import load_dotenv
load_dotenv() ## loading all the env variables


import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
# os.environ["GOOGLE_API_KEY"] = ["AIzaSyBX9oImBSUMyDLncB8EgTfKAJ4PQ8PvkC8"]
# os.environ["GOOGLE_API_KEY"] = "AIzaSyBX9oImBSUMyDLncB8EgTfKAJ4PQ8PvkC8"
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get responses
model = genai.GenerativeModel("gemini-pro-vision")

def get_generate_output(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

# initialize our streamlit app

st.set_page_config(page_title="Vision model")
st.header("Gemini Vision application")
input = st.text_input("Input Prompt : ",key = "input")

uploaded_file = st.file_uploader("Choose an image ...", type = ["jpg","png","jpeg"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image ",use_column_width=True)

submit = st.button("Tell me about the image ..")
if submit :
    response = get_generate_output(input,image)
    st.subheader("The response is ")
    st.write(response)

