from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def initializedembeddings(pages):
    #Create embeddings model
    print("Creating embeddings using SentenceTransformer...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    #Create FAISS vector store
    print("Building vector database...")
    vectorstore = FAISS.from_documents(pages, embeddings)
    print("✅ Vector store built successfully!\n")