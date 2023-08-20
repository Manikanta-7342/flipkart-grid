from dotenv import load_dotenv
import streamlit as st
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from PIL import Image
import io
from tools import ImageGeneratorTool, WebSrappingTool

load_dotenv()

i = 1
##############################
### initialize agent #########
##############################
tools = [ImageGeneratorTool(), WebSrappingTool()]

conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo"
)

agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools=tools,
    llm=llm,
    max_iterations=5,
    verbose=True,
    memory=conversational_memory,
    early_stopping_method='generate'
)
def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]

# set title
st.title('Project: GenTech')

# set header
st.header("Interact with ChatBot to Generate Images :hugging_face:")

def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)

    ##############################
    ### compute agent response ###
    ##############################

    # write agent response
    with st.spinner(text="In progress..."):
        generated_image = agent.run('this is the user prompt: {}'.format(user_question))
        # Open and display the generated image
        generated_image = Image.open(io.BytesIO(generated_image))
        temp = globals()["i"]
        generated_image.save("./generatedData/response{}.png".format(temp))
        img_path = r"http://localhost:8080/response{}.png".format(temp)  #python -m http.server 8080
        globals()["i"] += 1

with st.container():
    st.text_input("User Input:", on_change=on_input_change, key="user_input")


