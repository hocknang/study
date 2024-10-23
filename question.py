import streamlit as st

def home():
    st.button("Reset", type="primary")
    if st.button("Say hello"):
       st.write("hello world")