import streamlit as st
import study as study

#Define the pages: 
def page_home():
    study.home()

# Create a dictionary of pages
pages = {
    "EmPOWER": page_home,
}

# Add a sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()
