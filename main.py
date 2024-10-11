import streamlit as st

#Define the pages: 
def page_home():

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
