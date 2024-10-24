import streamlit as st

def home():
     st.title("Chatbot Learning")

     with st.chat_message("user"):
          st.write("Hello 👋")