import streamlit as st

# Function to display the MCQ
def display_mcq(question, options):
    st.write(question)
    selected_option = st.radio("Choose an option:", options)
    return selected_option

# Define your questions and options
questions = {
    "What is the capital of France?": ["Berlin", "Madrid", "Paris", "Lisbon"],
    "What is 2 + 2?": ["3", "4", "5", "6"],
    "Which planet is known as the Red Planet?": ["Earth", "Mars", "Jupiter", "Saturn"],
}

# Initialize score
score = 0

# Display questions
for question, options in questions.items():
    answer = display_mcq(question, options)
    if answer == options[2]:  # Assuming the correct answer is always the third option
        score += 1

# Show results
if st.button("Submit"):
    st.write(f"You scored {score} out of {len(questions)}!")