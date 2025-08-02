import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from backend.chunking import split_text
from backend.vector_store import build_vector_store, retrieve_relevant_chunks
from backend.qa_engine import answer_question

st.title("📚 Ask Your Notes")

uploaded_file = st.file_uploader("Upload your notes (PDF)", type="pdf")
query = st.text_input("Ask a question about your notes:")

if uploaded_file:
    st.info("Extracting text from PDF...")
    try:
        text = extract_text_from_pdf(uploaded_file)
        st.success(f"Extracted {len(text)} characters of text.")
    except Exception as e:
        st.error(f"Error extracting text: {e}")
        st.stop()

    st.info("Splitting text into chunks...")
    try:
        chunks = split_text(text)
        st.success(f"Split text into {len(chunks)} chunks.")
    except Exception as e:
        st.error(f"Error splitting text: {e}")
        st.stop()

    st.info("Building vector store...")
    try:
        vector_store = build_vector_store(chunks)
        st.success("Vector store built successfully.")
    except Exception as e:
        st.error(f"Error building vector store: {e}")
        st.stop()

    if query:
        st.info("Retrieving relevant chunks and answering your question...")
        try:
            relevant_docs = retrieve_relevant_chunks(query, vector_store)
            answer = answer_question(query, relevant_docs)
            st.markdown("### Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"Error during question answering: {e}")
