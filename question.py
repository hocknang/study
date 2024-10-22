import streamlit as st

def display_mcq(question, options, key):
    """
    Displays a multiple-choice question and returns the selected option.

    Parameters:
    - question (str): The question to be displayed.
    - options (list): List of answer options.

    Returns:
    - str: The selected option.
    """
    st.write(question)
    selected_option = st.radio("Choose an option:", options,  key=key)
    return selected_option

def home():
    # Define your questions and options
    questions = {
        "Who is eligible to rent out their flat?": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "What is the Minimum Occupation Period (MOP) for a non-subsidised flat purchased before 30 Aug 2010?": ["3", "4", "5", "6"],
        "Which of the following is NOT allowed to rent the flat?": ["Earth", "Mars", "Jupiter", "Saturn"],
	"How long must a tenant occupy the flat before they can be replaced by a new occupier?": ["Earth", "Mars", "Jupiter", "Saturn"],
	"What is the maximum period for renting out a flat per application?": ["Earth", "Mars", "Jupiter", "Saturn"],
	"If the flat owner is overseas during the rental period, what is required?": ["Earth", "Mars", "Jupiter", "Saturn"],
	"What is the consequence of renting out the flat without HDB's approval?": ["Earth", "Mars", "Jupiter", "Saturn"],
	"How many persons can live in a 3-room flat?": ["Earth", "Mars", "Jupiter", "Saturn"],
	"What happens if a non-citizen tenant's permission to remain in Singapore is revoked?": ["Earth", "Mars", "Jupiter", "Saturn"],
	"How much is the administrative fee for each rental application":  ["Earth", "Mars", "Jupiter", "Saturn"],
    }

    # Define correct answers
    correct_answers = ["Paris", "4", "Mars"]

    # Initialize score
    score = 0
    answers = []

    # Display questions
    for question, options in questions.items():
	st.write(f"mcq_{i}")
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