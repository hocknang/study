import requests
import streamlit as st
from PyPDF2 import PdfReader
from io import BytesIO
from openai import OpenAI


def chatbot(pdf_text):
    #working
    st.title("Chatbot Learning")

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

def pdfReader(document_url, uploaded_file):
    if document_url is not None:
        st.write(f"URL provided: {document_url}")
        response = requests.get(document_url)
        readPDF(response)
        #
    elif uploaded_file is not None:
        # Working code to read the pdf content
        pdf_reader = PdfReader(uploaded_file)
        readContentPDF(pdf_reader)
        #
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
        st.write("### Extracted PDF Text:")
        #Working
        #st.write(pdf_text)
        chatbot(pdf_text)
    else:
        st.write("No text could be extracted from the PDF.")

def readPDF(response):
    if response.status_code == 200:
        pdf_data = BytesIO(response.content)
        st.write(f"Bytes provided: {pdf_data}")
        pdf_reader = PdfReader(pdf_data)

        #Working code to read the pdf content
        #readContentPDF(pdf_reader)

    else:
        st.write("Not able to read the pdf")


def home():
    st.title("Term & Condition")
    st.write('Hi this is Term & Condition Explorer ChatBot')

    # Prompt the user to choose how they'd like to provide the document
    st.write("Would you prefer to upload a file or provide a document URL?")

    # delcare variable
    uploaded_file = None
    document_url = None

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
            pdfReader(document_url, uploaded_file)

    elif option == "Provide a document URL":
        document_url = st.text_input("Please enter the document URL:")
        # Display a confirmation message or handle the URL

    if document_url is not None:
        uploaded_file = None
        st.write(f"URL provided: {document_url}")
        #
        if st.button("Submit"):
            pdfReader(document_url, uploaded_file)

    '''
    if st.button("Submit"):
        pdfReader(document_url, uploaded_file)
    '''

