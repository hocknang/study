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
        "1. Who is eligible to rent out their flat?": ["Singapore Permanent Residents", "Singapore Citizens", "Foreigners", "Both A and C"],
        "2. What is the Minimum Occupation Period (MOP) for a non-subsidised flat purchased before 30 Aug 2010?": ["3 years", "5 years", "1 year", "No MOP required"],
        "3. Which of the following is NOT allowed to rent the flat?": ["Singapore Citizens", "Non-Malaysian Work Permit holders from the Construction sector", "Singapore Permanent Residents", "Students on a Student Pass"],
	"4. How long must a tenant occupy the flat before they can be replaced by a new occupier?": ["3 months", "6 months", "12 months", "24 months"],
	"5. What is the maximum period for renting out a flat per application?": ["12 months", "24 months", "36 months", "48 months"],
	"6. If the flat owner is overseas during the rental period, what is required?": ["No additional action needed", "A certified copy of the Power of Attorney", "Notification to HDB", "All of the above"],
	"7. What is the consequence of renting out the flat without HDB's approval?": ["The rental agreement is void", "HDB may take action to repossess the flat", "Notification to HDB", "The flat owner receives a warning"],
	"8. How many persons can live in a 3-room flat?": ["4", "6", "8", "10"],
	"9. What happens if a non-citizen tenant's permission to remain in Singapore is revoked": ["The flat owner can keep renting", "HDB's consent to rent is automatically revoked", "The flat owner must inform the tenant", "Nothing happens"],
	"10. How much is the administrative fee for each rental application?": ["$10", "$18", "$50", "$100"],
    }

    # Define correct answers
    correct_answers = ["Singapore Citizens", "3 years", "Non-Malaysian Work Permit holders from the Construction sector", "6 months", "36 months", "A certified copy of the Power of Attorney", "HDB may take action to repossess the flat", "6", "HDB's consent to rent is automatically revoked", "$18"]

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
            st.write(f"{question}:
            st.write(Your answer: f"{answers[i]}})
	    st.write(Correct answer: f"{correct_answers[i]}")