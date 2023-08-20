import streamlit as st
from streamlit_chat import message
from PIL import Image
import io
from setup import API_URL,API_TOKEN
import requests

i = 1

st.title('Project: GenTech')

st.header("Interact with ChatBot to Generate Images :hugging_face:")

def query(payload):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)


    with st.spinner(text="In progress..."):
        image_bytes = query({
            "inputs": user_input,  # Replace with your fashion-related text input
        })
        # Open and display the generated image
        generated_image = Image.open(io.BytesIO(image_bytes))
        temp = globals()["i"]
        generated_image.save("./generatedData/response{}.png".format(temp))
        img_path = r"http://localhost:8080/response{}.png".format(temp)  #python -m http.server 8080
        globals()["i"] += 1
        print(globals()["i"])


    # Store the image response in the generated list
    st.session_state.generated.append({'type': 'normal', 'data': f'<img width="100%" height="200" src="{img_path}"/>'})
    print(st.session_state.generated)


def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]


st.session_state.setdefault(
    'past',
    []
)
st.session_state.setdefault(
    'generated',
    []
)

chat_placeholder = st.empty()

with chat_placeholder.container():
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state['generated'][i]['data'],
            key=f"{i}",
            allow_html=True,
            is_table=True if st.session_state['generated'][i]['type'] == 'table' else False
        )

    st.button("Clear message", on_click=on_btn_click)

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")
