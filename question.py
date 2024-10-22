import streamlit as st

def display_mcq(question, options, key):
    """
    Displays a multiple-choice question and returns the selected option.

    Parameters:
    - question (str): The question to be displayed.
    - options (list): List of answer options.
    - key (str): Unique key for the radio element.

    Returns:
    - str: The selected option.
    """
    st.write(question)
    selected_option = st.radio("Choose an option:", options, key=key)
    return selected_option

def home():
    # Define your questions and options
    questions = {
        "Who is eligible to rent out their flat?": ["Singapore Permanent Residents", "Singapore Citizens", "Foreigners", "Both A and C"],
        "What is 2 + 2?": ["3", "4", "5", "6"],
        "Which planet is known as the Red Planet?": ["Earth", "Mars", "Jupiter", "Saturn"],
    }

    # Define correct answers
    correct_answers = ["Paris", "4", "Mars"]

    # Initialize score
    score = 0
    answers = []

    # Display questions with unique keys
    for i, (question, options) in enumerate(questions.items()):
        answer = display_mcq(question, options, key=f"mcq_{i}")
        answers.append(answer)

    # Submit button
    if st.button("Submit"):
        # Calculate score
        for i, question in enumerate(questions.keys()):
            if answers[i] == correct_answers[i]:
                score += 1

        # Show results
        st.write(f"You scored **{score} out of {len(questions)}!**")
        for i, question in enumerate(questions.keys()):
            st.write(f"- {question}: Your answer: {answers[i]}, Correct answer: {correct_answers[i]}")
