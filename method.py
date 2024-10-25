import streamlit as st

def home():
    st.title("Methodology")

    st.subheader("Retrieval Augmented Generation (RAG)")

    st.image("https://github.com/hocknang/study/blob/main/resource/RAG1_Diagram.png?raw=true")

    st.subheader("Vector Store Loading")

    st.markdown(''':blue-background[Step 1:] User can choose to :blue-background[Upload a file] 
    or Provide a :blue-background[Document URL]''')

    st.markdown(''':blue-background[Step 2:] The text from the documents is split into smaller chunks or segments.''')