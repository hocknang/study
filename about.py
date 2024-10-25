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
                   With Large Language Models :blue-background[(LLMs)] people can :blue-background[search] the 
                   :blue-background[(Terms and Conditions (T&C)] by :blue-background[typing questions] in their 
                   :blue-background[own words], without needing to know any special
                   legal terms. The LLM also helps by turning :blue-background[complicated legal words into simple language]
                   that anyone can understand.''')



