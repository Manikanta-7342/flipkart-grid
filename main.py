from tempfile import NamedTemporaryFile
import streamlit as st
from dotenv import load_dotenv
import requests
import io
from setup import API_URL,API_TOKEN
from PIL import Image
from htmlTemplates import css, bot_template, user_template

st.set_page_config(page_title="Chat to generate images ",
                       page_icon=":chatbot:")
st.write(css, unsafe_allow_html=True)

if "conversation" not in st.session_state:
    st.session_state.conversation = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
def handle_userinput(user_question):
    st.session_state.conversation = {'question': user_question}
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def query(payload):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# set title
st.title('Ask a question to generate an image')

st.header("Chat with Bot to Generate Images :hugging_face:")

user_question = st.text_input("Give a prompt to generate image:")

if user_question:
    #handle_userinput(user_question)
    st.write(user_template.replace(
        "{{MSG}}", user_question), unsafe_allow_html=True)
    qs = st.session_state.conversation['question'] = user_question
    with st.spinner(text="In progress..."):
        image_bytes = query({
            "inputs": user_question,  # Replace with your fashion-related text input
        })
        # Open and display the generated image
        generated_image = Image.open(io.BytesIO(image_bytes))
        st.session_state.chat_history.append([qs,generated_image])
        st.image(generated_image)

