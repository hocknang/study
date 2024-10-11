import streamlit as st


def home():
    st.title("Term & Condition")
    st.write('Hi this is Term & Condition Explorer ChatBot')
    
    # Dropdown with options
    options = ["Search Using Provided Url", "Option 2"]

    # Create a dropdown selectbox
    selected_option = st.selectbox("Choose an option:", options)

    # Display the selected option
    st.write(f"You selected: {selected_option}")
