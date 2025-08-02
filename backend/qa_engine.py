# # backend/qa_engine.py

# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import HuggingFacePipeline
# from transformers import pipeline

# def answer_question(query, docs):
#     if not docs:
#         return "No relevant content found to answer your question."

#     try:
#         # Use a local LLM for question answering
#         qa_pipeline = pipeline("text-generation", model="google/flan-t5-base", max_new_tokens=512)

#         llm = HuggingFacePipeline(pipeline=qa_pipeline)

#         chain = load_qa_chain(llm, chain_type="refine")

#         response = chain.run(input_documents=docs, question=query)
#         return response
#     except Exception as e:
#         return f"Error generating answer: {e}"

# backend/qa_engine.py

# backend/qa_engine.py

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

def answer_question(query, docs):
    if not docs:
        return "No relevant content found to answer your question."

    try:
        # Use a publicly available LLM for question answering
        qa_pipeline = pipeline(
            "text-generation",
            model="tiiuae/falcon-7b-instruct",
            max_new_tokens=512,
            temperature=0.3,
            do_sample=True
        )

        llm = HuggingFacePipeline(pipeline=qa_pipeline)
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=query)
        
        return response.strip()

    except Exception as e:
        return f"Error generating answer: {e}"
