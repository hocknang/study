import streamlit as st
import lesson as lesson
import learn as learn
import question as question
import employment as employment

#Define the pages: 
def page_home():
    lesson.init()

def page_learn():
    learn.home()

def page_question():
    question.home()

def page_employment():
    employment.home()
    
# Create a dictionary of pages
pages = {
    "Explorer Chatbots (Retrieving from File Or Url)": page_home,
    "Testing Chatbots (Retrieving From Internet)" : page_learn,
    "Knowledge & Understanding (MCQ) - HDB" : page_question,
    "Knowledge & Understanding (MCQ) - MOM" : page_employment
}

# Add a sidebar for navigation
st.sidebar.title("Navigation")
#Clear the Text Message
st.session_state.messages = []
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()