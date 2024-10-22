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
        "Who is eligible to rent out their flat?": ["Singapore Permanent Residents", "Singapore Citizens", "Foreigners", "Both A and C"],
        "What is the Minimum Occupation Period (MOP) for a non-subsidised flat purchased before 30 Aug 2010?": ["3 years", "5 years", "1 year", "No MOP required"],
        "Which of the following is NOT allowed to rent the flat?": ["Singapore Citizens", "Non-Malaysian Work Permit holders from the Construction sector", ") Singapore Permanent Residents", "Students on a Student Pass"],
	"How long must a tenant occupy the flat before they can be replaced by a new occupier?": ["3 months", "6 months", "12 months", "24 months"],
	"What is the maximum period for renting out a flat per application?": ["12 months", "24 months", "36 months", "48 months"],
	"If the flat owner is overseas during the rental period, what is required?": ["No additional action needed", "A certified copy of the Power of Attorney", "Notification to HDB", "All of the above"],
	"What is the consequence of renting out the flat without HDB's approval?": ["The rental agreement is void", "HDB may take action to repossess the flat", "The flat owner receives a warning", "There are no consequences"],
	"How many persons can live in a 3-room flat?": ["4", "6", "8", "10"],
	"The flat owner can keep renting?": ["The flat owner can keep renting", "HDB's consent to rent is automatically revoked", "The flat owner must inform the tenant", "Nothing happens"],
        "How much is the administrative fee for each rental application?": ["$10", "$18", "$50", "$100"],
    }

    # Initialize score
    score = 0
    correct_answers = ["Singapore Citizens", "3 years", "Non-Malaysian Work Permit holders from the Construction sector", "6 months", "36 months", "A certified copy of the Power of Attorney",
		       "HDB may take action to repossess the flat", "6", "HDB's consent to rent is automatically revoked", "$18"]  # List of correct answers

    # Display questions
    for question, options in questions.items():
        answer = display_mcq(question, options)
        # Check if the selected answer is correct
        if answer == correct_answers[list(questions.keys()).index(question)]:
            score += 1

    # Show results
    if st.button("Submit"):
        st.write(f"You scored {score} out of {len(questions)}!")