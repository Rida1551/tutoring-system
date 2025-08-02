# backend/vector_store.py

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def build_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embeddings)

def retrieve_relevant_chunks(query, vector_store, k=3):
    return vector_store.similarity_search(query, k=k)
