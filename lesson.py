import streamlit as st
import pypdf
import requests

def home():
    st.title("Term & Condition")
    st.write('Hi this is Term & Condition Explorer ChatBot')

    # Prompt the user to choose how they'd like to provide the document
    st.write("Would you prefer to upload a file or provide a document URL?")

    #delcare variable
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

    #https://eservices.mom.gov.sg/iwork/assets/pdf/EmPOWER%20Terms%20and%20conditions.pdf

    if st.button("Submit"):
        if document_url:
            response = requests.get(document_url)
            st.write(f"URL provided: {response.status_code}")
        else:
            st.error("Please enter something before pressing Submit!")
        
    
  
