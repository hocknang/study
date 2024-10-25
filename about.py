import streamlit as st

def home():

    st.title("About Us")

    st.subheader("Problem Statement")

    st.markdown('''
            Uses finds it very :red[inefficiency] and :red[time-consuming] process of navigating through extensive
            :blue-background[Terms and Conditions (T&C) document]. 
            The current document is overly :red[lengthy], making it difficult 
            for users to quickly :blue-background[locate specific clauses or key information]''')

    st.subheader("Proposed Solution")

    st.markdown('''
                With Large Language Models :blue-background[(LLMs)] people can :blue-background[search] the 
                :blue-background[(Terms and Conditions (T&C)] by :blue-background[typing questions] in their 
                :blue-background[own words], without needing to know any special
                legal terms. The LLM also helps by turning :blue-background[complicated legal words into simple language]
                that anyone can understand.''')

    st.subheader("Impact")

    st.markdown('''
                   After using the :blue-background[LLMs] solution, people will find it :blue-background[easier]
                   to get the information they need by :blue-background[asking simple questions.] 
                   They will :blue-background[understand complicated legal terms]better because 
                   they’ll be explained in :blue-background[plain language.]
                   This will make everything :blue-background[clearer] and :blue-background[faster] to find.''')

    st.subheader("Project Sponsors & Users")

    st.markdown(''':blue-background[Everyone] who needs to retrieve information in the Terms and Conditions (T&C).''')

    st.subheader("Data Classification & Sensitivity")

    st.markdown('''Official (Open) / Non-sensitive''')

    st.subheader("2 Use Cases")

    st.markdown(''':blue-background[1. Use Case: ] Application for Flat Rental (HDB)''')

    st.markdown(''':blue-background[2. Use Case: ] Employment Act: who it covers (MOM)''')


