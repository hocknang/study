import streamlit as st

def home():
    st.title("Methodology")

    st.subheader("Retrieval Augmented Generation (RAG)")

    st.image("https://github.com/hocknang/study/blob/main/resource/RAG1_Diagram.png?raw=true")

    st.subheader("Vector Store Loading")

    st.markdown(''':blue-background[Step 1:] User can choose to :blue-background[Upload a file] 
    or Provide a :blue-background[Document URL]''')

    st.markdown(''':blue-background[Step 2:] The text from the :blue-background[documents]
     is split into :blue-background[smaller chunks] or :blue-background[segments.]''')

    st.markdown(''':blue-background[Step 3:] Generate :blue-background[embeddings] for each chunk of text 
    and :blue-background[store] these embeddings in a vector database, ''')

    st.subheader("Retrieval")