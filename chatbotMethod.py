import streamlit as st
from openai import OpenAI

# Normal LLM
def home(pdf_text):
    #st.write(pdf_text)

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])