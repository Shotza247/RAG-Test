from PDFImport import pdfimport
from VectorEmbeddings import semantic_search, ask_llm

print("Welcome to the PDF RAG System!")
print("=" * 50 + "\n")

# Load PDF once at startup
print("Please load your PDF file first.")
vectorstore = pdfimport()

if vectorstore:
    print("\n" + "=" * 50)
    print("PDF loaded successfully! You can now ask questions.")
    print("=" * 50 + "\n")
    
    while True:
        query = input("\nEnter your query (or 'exit' to quit): ").strip()
        
        if query.lower() == "exit":
            print("\nThank you for using the PDF RAG System!")
            break
        
        if not query:
            print("Please enter a valid query.")
            continue
        
        # Perform semantic search
        semantic_search(vectorstore, query, top_k=3)
        
        # Get LLM answer
        ask_llm(vectorstore, query)
else:
    print("Failed to load PDF. Exiting...")