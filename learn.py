import streamlit as st

def home():
     st.title("Chatbot Learning")

     with st.chat_message("user"):
          st.write("Hello 👋")

     prompt = st.chat_input("Say something")
     if prompt:
          st.write(f"User has sent the following prompt: {prompt}")

     st.write(st.secrets["DB_PASSWORD"])