import streamlit as st

def home():
     st.title("Chatbot Learning")

     with st.chat_message("user"):
          st.write("Hello 👋")

     prompt = st.chat_input("Say something")
     if prompt:
          st.write(f"User has sent the following prompt: {prompt}")

     client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])