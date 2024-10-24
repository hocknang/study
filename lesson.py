import string

import requests
import streamlit as st
from PyPDF2 import PdfReader
from io import BytesIO
from openai import OpenAI

def pdfReader(document_url, uploaded_file):
    if document_url is not None:
        st.write(f"URL provided: {document_url}")
        response = requests.get(document_url)
        return readPDF(response)
        #
    elif uploaded_file is not None:
        # Working code to read the pdf content
        pdf_reader = PdfReader(uploaded_file)
        return readContentPDF(pdf_reader)
    else:
        st.error("Please enter something before pressing Submit!")

# Testing to read PDF Content
def readContentPDF(pdf_reader):
    # Extract and display text from the PDF
    pdf_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        #this is what i need
        pdf_text += page.extract_text()  # Extract text from the page

    # Display the extracted text
    if pdf_text:
        st.write("### Extracted PDF Text (Document Had been Uploaded Successfully (Please start to enter your question):")
        #Working
        #st.write(pdf_text)
        return pdf_text
    else:
        st.write("No text could be extracted from the PDF.")

def readPDF(response):
    if response.status_code == 200:
        pdf_data = BytesIO(response.content)
        st.write(f"Bytes provided: {pdf_data}")
        pdf_reader = PdfReader(pdf_data)

        #Working code to read the pdf content
        return readContentPDF(pdf_reader)

    else:
        st.write("Not able to read the pdf")

def init():
    st.write("Please enter your password:")

    password = st.text_input("Password", type="password")

    if st.secrets["PASSWORD"] == password:
        st.success("Valid Credential")
        home()
    else:
        st.error("Invalid Password")

def home():

    st.title("Term & Condition")
    st.write('Hi this is Term & Condition Explorer ChatBot')

    condition = "IMPORTANT NOTICE: This web application is developed as a proof-of-concept prototype. The information provided here is NOT intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters." \
                "Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output." \
                "Always consult with qualified professionals for accurate and personalized advice."

    with st.expander("Disclaimer on the main page of your application"):
        st.text_area("Disclaimer Content", value=condition, height=150)

    # Prompt the user to choose how they'd like to provide the document
    st.write("Would you prefer to upload a file or provide a document URL?")
    st.info('This Explore ChatBot Current It only Support PDF Document Only, Aplogise for the Inconvience we will try to support More document format in our next release', icon="ℹ️")

    # delcare variable
    uploaded_file = None
    document_url = None

    pdf_text_File = None
    pdf_text_Url = None

    isReadFile = False

    # Create a dropdown for the user to select an option
    option = st.selectbox(
        "Choose an option:",
        ["Upload a file",
         "Provide a document URL"]
    )

    # Handle the option selected by the user
    if option == "Upload a file":
        uploaded_file = st.file_uploader("Please upload your file here:", type="pdf")
        document_url = None

    if uploaded_file is not None:
        # Display a confirmation message or handle the uploaded file
        st.write(f"File uploaded: {uploaded_file.name}")
        if st.button("Submit"):
            pdf_text_File = pdfReader(document_url, uploaded_file)

    elif option == "Provide a document URL":
        document_url = st.text_input("Please enter the document URL:")
        # Display a confirmation message or handle the URL

    if document_url is not None:
        uploaded_file = None
        st.write(f"URL provided: {document_url}")
        #
        if st.button("Submit"):
            pdf_text_Url = pdfReader(document_url, uploaded_file)

    #st.write('pdf Text File: ' + str(pdf_text_File))

    #st.write("pdf URL Text: " + str(pdf_text_Url))

    if pdf_text_File is not None:
        isReadFile = True
        st.write("Hit")
        st.session_state.pdf_content = pdf_text_File

    if pdf_text_Url is not None:
        st.session_state.pdf_content = pdf_text_Url

    #LLM Chatbot (General)
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o-mini"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        if isReadFile:
            st.write("Hit 2")
            combined_content = (
                f"Here is the content from the uploaded document:\n\n{st.session_state.pdf_content}\n\n"
                f"User question: {prompt}\n"
            )
        else:
            st.write("MISS")
            combined_content = (
                f"User question: {prompt}\n"
            )
        st.session_state.messages.append({"role": "user", "content": combined_content})
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

    '''
    if st.button("Submit"):
        pdfReader(document_url, uploaded_file)
    '''

