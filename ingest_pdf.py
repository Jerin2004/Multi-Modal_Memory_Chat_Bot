# ingest_pdf.py

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def ingest_pdf(pdf_path, db_path):
    # Step 1: Load PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # Step 2: Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(pages)

    print(f"Loaded {len(docs)} document chunks.")

    # Step 3: Generate embeddings using Hugging Face models
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Step 4: Save vectorstore locally
    vectorstore.save_local(db_path)
    print(f"Embeddings saved to {db_path}")

if __name__ == "__main__":
    pdf_path = "sample.pdf"  # replace with your PDF file
    db_path = "vector_db"
    ingest_pdf(pdf_path, db_path)
