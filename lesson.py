import requests
import streamlit as st
from PyPDF2 import PdfReader
from io import BytesIO


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
        st.write(pdf_text)
    else:
        st.write("No text could be extracted from the PDF.")


def readPDF(response):
    st.write(f"URL provided: {response.status_code}")
    if response.status_code == 200:
        pdf_data = BytesIO(response.content)
        st.write(f"Bytes provided: {pdf_data}")
        pdf_reader = PdfReader(pdf_data)
        
        readContentPDF(pdf_reader)

    else:
        st.write("Not able to read the pdf")


def home():
    st.title("Term & Condition")
    st.write('Hi this is Term & Condition Explorer ChatBot')

    # Prompt the user to choose how they'd like to provide the document
    st.write("Would you prefer to upload a file or provide a document URL?")

    # delcare variable
    uploaded_file = None
    document_url = ""

    # Create a dropdown for the user to select an option
    option = st.selectbox(
        "Choose an option:",
        ["Upload a file",
         "Provide a document URL"]
    )

    # Handle the option selected by the user
    if option == "Upload a file":
        uploaded_file = st.file_uploader("Please upload your file here:")

    if uploaded_file is not None:
        # Display a confirmation message or handle the uploaded file
        st.write(f"File uploaded: {uploaded_file.name}")

    elif option == "Provide a document URL":
        document_url = st.text_input("Please enter the document URL:")

    if document_url:
        # Display a confirmation message or handle the URL
        st.write(f"URL provided: {document_url}")

    # https://eservices.mom.gov.sg/iwork/assets/pdf/EmPOWER%20Terms%20and%20conditions.pdf

    if st.button("Submit"):
        if document_url:
            response = requests.get(document_url)
            readPDF(response)

        else:
            st.error("Please enter something before pressing Submit!")
