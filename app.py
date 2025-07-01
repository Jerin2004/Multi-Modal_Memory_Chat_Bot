# # app.py

# import streamlit as st
# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
# import os

# # Initialize embeddings
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# def ingest_pdf(pdf_path, db_path):
#     loader = PyPDFLoader(pdf_path)
#     pages = loader.load()
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#     docs = text_splitter.split_documents(pages)
#     vectorstore = FAISS.from_documents(docs, embeddings)
#     vectorstore.save_local(db_path)
#     return vectorstore

# def query_vector_db(db_path, user_query, k=3):
#     vectorstore = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
#     results = vectorstore.similarity_search(user_query, k=k)
#     answer = "\n".join([res.page_content for res in results])
#     return answer

# # Streamlit UI
# st.title("📚 Multi-Modal Memory Chatbot")

# uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

# if uploaded_file is not None:
#     with open("uploaded.pdf", "wb") as f:
#         f.write(uploaded_file.read())
#     st.success("✅ PDF uploaded successfully.")

#     # Automatically ingest upon upload (optional)
#     ingest_pdf("uploaded.pdf", "vector_db")
#     st.success("✅ Embeddings generated and stored successfully for this PDF.")


# query = st.text_input("Ask a question based on the PDF content:")

# if query:
#     if os.path.exists("vector_db"):
#         answer = query_vector_db("vector_db", query)
#         st.write("### 🤖 Answer")
#         st.write(answer)
#     else:
#         st.warning("Please upload and ingest a PDF first.")




# app.py

import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ---------------------- Styling ---------------------- #
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .title {
            color: #2c3e50;
            text-align: center;
        }
        .subtitle {
            color: #34495e;
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .stButton>button {
            background-color: #2c3e50;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 10em;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #34495e;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------- App Header ---------------------- #
st.markdown("<h1 class='title'>📚 Multi-Modal Memory Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Upload PDFs, ask context-aware questions, and get semantic answers instantly.</div>", unsafe_allow_html=True)

# ---------------------- Embeddings Init ---------------------- #
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def ingest_pdf(pdf_path, db_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(pages)
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(db_path)
    return vectorstore

def query_vector_db(db_path, user_query, k=3):
    vectorstore = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
    results = vectorstore.similarity_search(user_query, k=k)
    answer = "\n".join([res.page_content for res in results])
    return answer

# ---------------------- File Upload ---------------------- #
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ PDF uploaded successfully.")

    # Automatically ingest upon upload
    ingest_pdf("uploaded.pdf", "vector_db")
    st.success("✅ Embeddings generated and stored successfully for this PDF.")

# ---------------------- Query Input ---------------------- #
query = st.text_input("Ask a question based on the PDF content:")

if query:
    if os.path.exists("vector_db"):
        answer = query_vector_db("vector_db", query)
        st.write("### 🤖 Answer")
        st.write(answer)
    else:
        st.warning("Please upload and ingest a PDF first.")

# ---------------------- Footer ---------------------- #
st.markdown("""
    <hr>
    <div style='text-align: center'>
        <small>Developed by Jerin | Powered by Hugging Face Embeddings</small>
    </div>
""", unsafe_allow_html=True)
