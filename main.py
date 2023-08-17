from tempfile import NamedTemporaryFile
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.llms import HuggingFaceHub
from langchain.llms import HuggingFacePipeline
# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain.llms import GooseAI
from tools import ImageCaptionTool, ObjectDetectionTool
from bardapi import Bard
from htmlTemplates import css, bot_template, user_template

load_dotenv()
##############################
### initialize agent #########
##############################
tools = [ImageCaptionTool(), ObjectDetectionTool()]

conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo"  #gpt-3.5-turbo text-davinci-003
)
# llm = HuggingFaceHub(
#         repo_id="gpt2" , #google/flan-t5-xl
#         model_kwargs={ "temperature" : 0},
#         verbose=True,
#
# )

# model_id = "gpt2"
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(model_id)
# pipe = pipeline(
#     "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10
# )
# llm = HuggingFacePipeline(pipeline=pipe)

# llm = GooseAI(model_name="gpt-neo-20b",
#               gooseai_api_key="sk-Cmxeq4tUCAVawiaeJYYzBH5it29qEzwPHRp3hAd3NjywMWJP",
#               temperature=0.3,
#               verbose=True
# )

# token = 'ZwivMJybAIBnD9Rac-NsPx3_q1rsRLV1Sj4YfbJ9c5c0PafMtmOAjo0jHJkUG7Oq9o051A.'
# llm = Bard(token=token).get_answer()

agent = initialize_agent(
    agent="chat-conversational-react-description",
    llm=llm,
    tools=tools,
    max_iterations=5,
    verbose=True,
    memory=conversational_memory,
    early_stopping_method='generate',
    handle_parsing_errors=True,
    kwargs={'truncation': 'only_first'}
)

# set title
st.title('Ask a question to an image')

# set header
st.header("Please upload an image")

# upload file
file = st.file_uploader("", type=["jpeg", "jpg", "png"])

if file:
    # display image
    st.image(file, use_column_width=True)

    # text input
    user_question = st.text_input('Ask a question about your image:')

    # #load_dotenv()
    # st.set_page_config(page_title="Chat with multiple PDFs",
    #                    page_icon=":books:")
    # st.write(css, unsafe_allow_html=True)
    #
    # if "conversation" not in st.session_state:
    #     st.session_state.conversation = None
    # if "chat_history" not in st.session_state:
    #     st.session_state.chat_history = None
    #
    # st.header("Chat with multiple PDFs :books:")
    # user_question = st.text_input("Ask a question about your documents:")
    # if user_question:
    #     handle_userinput(user_question)

    ##############################
    ### compute agent response ###
    ##############################
    with NamedTemporaryFile(dir='.') as f:
        f.write(file.getbuffer())
        image_path = f.name

        # write agent response
        if user_question and user_question != "":
            with st.spinner(text="In progress..."):
                print(user_question," ",image_path)
                response = agent.run('{}, this is the image path: {}'.format(user_question, image_path))
                st.write(response)