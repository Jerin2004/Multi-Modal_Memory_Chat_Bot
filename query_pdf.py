# query_pdf.py

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def query_vector_db(db_path, user_query, k=3):
    # Load embeddings model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Load existing vectorstore
    vectorstore = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
    
    # Perform similarity search
    results = vectorstore.similarity_search(user_query, k=k)
    
    # Concatenate results as final 'answer' (Placeholder logic)
    answer = "\n".join([res.page_content for res in results])

    return answer

if __name__ == "__main__":
    db_path = "vector_db"
    user_query = input("Enter your query: ")
    final_answer = query_vector_db(db_path, user_query)
    print("\nFinal Answer:")
    print(final_answer)
