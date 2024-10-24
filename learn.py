import streamlit as st
from openai import OpenAI

def home():
     if prompt := st.chat_input("What is up?"):
          st.chat_message("user").markdown(prompt)