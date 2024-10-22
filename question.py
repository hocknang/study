import streamlit as st

def display_mcq(question, options):
    """
    Displays a multiple-choice question and returns the selected option.

    Parameters:
    - question (str): The question to be displayed.
    - options (list): List of answer options.

    Returns:
    - str: The selected option.
    """
    st.write(question)
    selected_option = st.radio("Choose an option:", options)
    return selected_option

def home():
    # Define your questions and options
    questions = {
        "What is the capital of France?": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "What is 2 + 2?": ["3", "4", "5", "6"],
        "Which planet is known as the Red Planet?": ["Earth", "Mars", "Jupiter", "Saturn"],
    }

    # Initialize score
    score = 0
    correct_answers = ["Paris", "4", "Mars"]  # List of correct answers

    # Display questions
    for question, options in questions.items():
        answer = display_mcq(question, options)
        # Check if the selected answer is correct
        if answer == correct_answers[list(questions.keys()).index(question)]:
            score += 1

    # Show results
    if st.button("Submit"):
        st.write(f"You scored {score} out of {len(questions)}!")