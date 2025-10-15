from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from sentence_transformers import CrossEncoder


# Load LLM (Mistral-7B) for NLP Capabilities
print("Loading text-generation model...")
qa_pipeline = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    torch_dtype="auto",
    device_map="auto",
    max_new_tokens=512
)
print("Model loaded successfully!\n")

#Load Cross-Encoder Reranker for Better Search Accuracy
print("Loading reranker model...")
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-12-v2")
print("Reranker loaded successfully!\n")


#Initializing Embeddings and Vector Store
def initializedembeddings(pages):
    """Create embeddings and build FAISS vector store"""
    print("\nCreating embeddings using SentenceTransformer...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("Building FAISS vector database for embedding and semantic search...")
    vectorstore = FAISS.from_documents(pages, embeddings)

    print("Vector store built successfully!\n")
    return vectorstore

# Semantic Search with Reranking
def semantic_search(vectorstore, query, k=8, top_k=3):
    """Perform semantic search + reranking on the vectorstore"""
    print("\n" + "=" * 50)
    print(f"SEMANTIC SEARCH RESULTS (reranked)")
    print("=" * 50)
    print(f"Query: '{query}'")
    print("-" * 50)

    # Retrieve initial candidates
    results = vectorstore.similarity_search(query, k=k)

    # Prepare query-document pairs for reranking
    pairs = [[query, res.page_content] for res in results]
    scores = reranker.predict(pairs)

    #Combine results and sort based of confidence scores
    ranked = sorted(zip(results, scores), key=lambda x: x[1], reverse=True)
    top_results = ranked[:top_k]

    for i, (res, score) in enumerate(top_results, 1):
        page_num = res.metadata.get('page', i - 1) + 1
        print(f"\n[Result {i}] Page {page_num} | Confidence: {score:.2f}")
        print("-" * 50)
        content = res.page_content.strip()
        preview_length = min(400, len(content))
        print(content[:preview_length] + ("..." if len(content) > preview_length else ""))

    print("\n" + "=" * 50)
    return top_results


#We then ask the LLM with High-Confidence Context
def ask_llm(vectorstore, question):
    print("\n" + "=" * 50)
    print("LLM ANSWER")
    print("=" * 50)
    print(f"Question: {question}")
    print("-" * 50)

    # Retrieve and re-rank top documents
    results = semantic_search(vectorstore, question, k=8, top_k=3)
    avg_confidence = sum(score for _, score in results) / len(results)

    # Warn on low average confidence
    if avg_confidence < 0.7:
        print(f"\n Warning: Retrieval confidence is low ({avg_confidence:.2f}). Answer may be unreliable.\n")

    # Combine top-ranked contexts
    context = "\n\n".join([doc.page_content for doc, _ in results])
    prompt = f"""You are an expert assistant. Use the following context to answer the question accurately.
    Context: {context}
    Question: {question}
    Answer clearly and in detail. End your answer with a confidence rating (0–100) based on how sure you are."""

    #generate response with Mistral
    response = qa_pipeline(prompt, temperature=0.2, max_new_tokens=400)
    print(response[0]['generated_text'])

    print("\n" + "=" * 50)
