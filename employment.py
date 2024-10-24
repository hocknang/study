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
    columnName = "basic salary"
    columnName1 = "workman"

    questions = {
        "Under the Employment Act, which of the following categories of employees is explicitly excluded from Part IV provisions regarding rest days and hours of work?":
            ["A) Employees earning less than $2,600", "B) Workmen earning less than $4,500", "C) Managers and executives regardless of salary",
                                                    "D) Full-time employees with fixed-term contracts"],

        "Which of the following statements regarding coverage under the Employment Act is FALSE?": [
            "A) All local employees are covered under the Act.", "B) Foreign employees holding work passes are covered under the Employment of Foreign Manpower Act.",
            "C) Part-time employees are covered under the Employment Act if they meet specific criteria.", "D) Domestic workers are fully covered by the Employment Act."],

        "If a workman is employed at piece rates, what conditions must be met for them to fall under the definition of a workman according to the Employment Act?": ["A) They must work at least 40 hours a week.",
                                                                    "B) They must operate commercial vehicles.",
                                                                    "C) They must perform manual work more than half their working time.",
                                                                    "D) They must be paid on a monthly basis."],

        f"Which of the following best describes the term **{columnName}** in the context of the Employment Act": [
            "A) It includes all bonuses and allowances.",
            "B) It includes overtime payments and annual wage supplements.",
            "C) It is the fixed amount earned before deductions and excludes bonuses and allowances.",
            "D) They must be paid on a monthly basis."],

        f"Which of the following employees would NOT be considered a **{columnName1}** under the Employment Act?": [
            "A) A construction worker who primarily performs manual labour.",
            "B) A supervisor who spends 60% of their time supervising and 40% performing manual tasks.",
            "C) A bus driver who operates a commercial vehicle.",
            "D) A project manager with specialized knowledge in construction."],

        "What is the significance of the Tripartite Advisory on Employment of Term Contract Employees in relation to the Employment Act?": [
            "A) It provides legal protections to all contract employees.",
            "B) It sets out best practices for employers in managing term contract employees.",
            "C) It allows employers to bypass the Employment Act for contract employees.",
            "D) It specifically applies to foreign employees holding work passes."],

        "Which of the following statements regarding the Employment Act's provisions for foreign employees is TRUE?": [
            "A) All foreign employees are covered under the Employment Act.",
            "B) Foreign employees are covered under the Employment of Foreign Manpower Act only.",
            "C) Foreign employees with work passes are exempt from any employment regulations.",
            "D) Foreign employees are entitled to the same benefits as local employees under the Employment Act."],

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
