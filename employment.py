import streamlit as st

my_dict = {}

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
    my_dict[key] = selected_option
    return selected_option

def home():
    # Define your questions and options
    questions = {
        "Under the Employment Act, which of the following categories of employees is explicitly excluded from Part IV provisions regarding rest days and hours of work?":
            ["A) Employees earning less than $2,600", "B) Workmen earning less than $4,500", "C) Managers and executives regardless of salary",
                                                    "D) Full-time employees with fixed-term contracts"],
        "Which of the following statements regarding coverage under the Employment Act is FALSE?": [
            "A) All local employees are covered under the Act.", "B) Foreign employees holding work passes are covered under the Employment of Foreign Manpower Act.",
            "C) Part-time employees are covered under the Employment Act if they meet specific criteria.", "D) Domestic workers are fully covered by the Employment Act."],
        "Which of the following is NOT allowed to rent the flat?": ["Singapore Citizens",
                                                                    "Non-Malaysian Work Permit holders from the Construction sector",
                                                                    "Singapore Permanent Residents",
                                                                    "Students on a Student Pass"],
        "If a workman is employed at piece rates, what conditions must be met for them to fall under the definition of a workman according to the Employment Act?": ["A) They must work at least 40 hours a week.",
                                                                                                  "B) They must operate commercial vehicles.",
                                                                                                  "C) They must perform manual work more than half their working time.",
                                                                                                  "D) They must be paid on a monthly basis."],
        "Which of the following best describes the term basic salary in the context of the Employment Act?": ["A) It includes all bonuses and allowances.", "B) It includes overtime payments and annual wage supplements.",
         "C) It is the fixed amount earned before deductions and excludes bonuses and allowances.", "D)  It is the total earnings an employee receives, including piece rates."],
        "If the flat owner is overseas during the rental period, what is required?": ["No additional action needed",
                                                                                      "A certified copy of the Power of Attorney",
                                                                                      "Notification to HDB",
                                                                                      "All of the above"],
        "What is the consequence of renting out the flat without HDB's approval?": ["The rental agreement is void",
                                                                                    "HDB may take action to repossess the flat",
                                                                                    "Notification to HDB",
                                                                                    "The flat owner receives a warning"],
        "How many persons can live in a 3-room flat?": ["4", "6", "8", "10"],
        "What happens if a non-citizen tenant's permission to remain in Singapore is revoked": [
            "The flat owner can keep renting", "HDB's consent to rent is automatically revoked",
            "The flat owner must inform the tenant", "Nothing happens"],
        "How much is the administrative fee for each rental application?": ["$10", "$18", "$50", "$100"],
    }

    # Define correct answers
    correct_answers = ["Singapore Citizens", "3 years",
                       "Non-Malaysian Work Permit holders from the Construction sector", "6 months", "36 months",
                       "A certified copy of the Power of Attorney", "HDB may take action to repossess the flat", "6",
                       "HDB's consent to rent is automatically revoked", "$18"]

    # Initialize score
    score = 0
    answers = []
    for i, (question, options) in enumerate(questions.items()):
        answer = display_mcq(question, options, key=f"mcq_{i}")
        # st.write(f"**Answer:** {answer}")
        answers.append(answer)

    if st.button("Submit"):
        for i, key in enumerate(my_dict):
            m = i + 1
            if correct_answers[i] == my_dict[key]:
                score += 1
                st.write(f"{m}: Correct! 🎉 The answer is {correct_answers[i]}.")
            else:
                st.write(f"{m}: Wrong! 😞 The correct answer is {correct_answers[i]}. You selected " + my_dict[key] + ".")

        st.write(f"Your final score is: {score}/{len(my_dict)}")
