import streamlit as st
import lesson as lesson
import learn as learn
import question as question
import employment as employment
import about as about
import rag as rag

#Define the pages:
def page_about():
    about.home()

def page_home():
    lesson.init()

def page_learn():
    learn.init()

def page_question():
    question.home()

def page_employment():
    employment.home()

def page_rag():
    rag.home()
    
# Create a dictionary of pages
pages = {
    "Explorer Chatbots (Retrieving from File Or Url) - Normal": page_home,
    "Testing Chatbots (Retrieving From Internet) - Normal" : page_learn,
    "Knowledge & Understanding (MCQ) - HDB" : page_question,
    "Knowledge & Understanding (MCQ) - MOM" : page_employment,
    "About Us" : page_about,
    "Explorer Chatbots (Retrieving from File Or Url) - RAG": page_rag()

}

# Add a sidebar for navigation
st.sidebar.title("Navigation")
#Clear the Text Message
st.session_state.messages = []
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()