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

    # Define correct answers
    correct_answers = ["Paris", "4", "Mars"]

    # Initialize score
    score = 0
    answers = []

    # Display questions
    for question, options in questions.items():
        answer = display_mcq(question, options)
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