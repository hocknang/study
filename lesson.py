import requests
import streamlit as st
from PyPDF2 import PdfReader
from io import BytesIO
from openai import OpenAI


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
        pdf_text += page.extract_text()  # Extract text from the page

    # Display the extracted text
    if pdf_text:
        st.write("### Extracted PDF Text:")
       # Working
       #st.write(pdf_text)
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

