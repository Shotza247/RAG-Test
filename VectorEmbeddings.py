from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

def initializedembeddings(pages):
    #Create embeddings model
    print("Creating embeddings using SentenceTransformer...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    #Create FAISS vector store
    print("Building vector database...")
    vectorstore = FAISS.from_documents(pages, embeddings)
    print("Vector store built successfully!\n")
    
def semantic_search(query, top_k=3):
    results = vectorstore.similarity_search(query, k=top_k)
    print(f"\nTop {top_k} results for: '{query}'\n" + "=" * 50)
    for i, res in enumerate(results, 1):
        print(f"\nResult {i} (Page {res.metadata['page'] + 1}):")
        print(res.page_content[:500], "...\n")

# Load a local or Hugging Face hosted model for NLP reasoning
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def ask_llm(question):
    docs = vectorstore.similarity_search(question, k=3)
    context = " ".join([d.page_content for d in docs])
    result = qa_pipeline(question=question, context=context)
    print(f"\nLLM Answer: {result['answer']}")
