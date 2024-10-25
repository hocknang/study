import streamlit as st

def home():

    st.title("About Us")

    st.subheader("Problem Statement")

    '''
    st.markdown(f"Uses finds it very **{inefficiency}** and time-consuming process of navigating through extensive "
             "Terms and Conditions (T&C) document. The current document is overly lengthy, making it difficult "
             "for users to quickly locate specific clauses or key information.")
    '''

    st.markdown('''
            Uses finds it very :red[inefficiency] and :red[time-consuming] process of navigating through extensive
            :blue-background[Terms and Conditions (T&C) document]''')

    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')


