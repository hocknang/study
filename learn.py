import streamlit as st
from openai import OpenAI

def init():
    st.write("Please enter your password:")

    password = st.text_input("Password", type="password")

    if st.secrets["PASSWORD"] == password:
        st.success("Valid Credential")
        home()
    else:
        st.error("Invalid Credential")

def home():
     st.title("Chatbot Learning")

     condition = "IMPORTANT NOTICE: This web application is developed as a proof-of-concept prototype. The information provided here is NOT intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters." \
                 "Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output." \
                 "Always consult with qualified professionals for accurate and personalized advice."

     with st.expander("Disclaimer on the main page of your application"):
          st.text_area("Disclaimer Content", value=condition, height=150)

     client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

     if "openai_model" not in st.session_state:
          st.session_state["openai_model"] = "gpt-4o-mini"

     if "messages" not in st.session_state:
          st.session_state.messages = []

     for message in st.session_state.messages:
          with st.chat_message(message["role"]):
               st.markdown(message["content"])

     if prompt := st.chat_input("What is up?"):
          st.session_state.messages.append({"role": "user", "content": prompt})
          with st.chat_message("user"):
               st.markdown(prompt)

          with st.chat_message("assistant"):
               stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=[
                         {"role": m["role"], "content": m["content"]}
                         for m in st.session_state.messages
                    ],
                    stream=True,
               )
               response = st.write_stream(stream)
          st.session_state.messages.append({"role": "assistant", "content": response})