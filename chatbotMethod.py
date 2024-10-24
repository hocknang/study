import streamlit as st
from openai import OpenAI

# Normal LLM

def history():
    if "messages" not in st.session_state:
        st.session_state.messages = []

        # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
def home(pdf_text):
    #st.write(pdf_text)

    # React to user input
    if prompt := st.chat_input("What is up?"):
        st.chat_message("user").markdown(prompt)
        