import streamlit as st
import lesson as lesson
import learn as learn

#Define the pages: 
def page_home():
    lesson.home()

def page_learn():
    learn.home()
    
# Create a dictionary of pages
pages = {
    "Explorer Chatbots": page_home,
    "Testing Chatbots" : page_learn
}

# Add a sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()