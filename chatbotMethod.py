import streamlit as st
from openai import OpenAI

# Normal LLM
def home(pdf_text):
    #st.write(pdf_text)

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Initialize session state for model and messages
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o-mini"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input and message handling
    if prompt := st.chat_input("What is up?"):
        # Append user message to session state
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display the user message immediately in the chat
        with st.chat_message("user"):
            st.markdown(prompt)