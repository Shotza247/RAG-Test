from VectorEmbeddings import initializedembeddings

def pagestester(pages):
    """Process pages and return vectorstore"""
    print("\n" + "=" * 50)
    print("ANALYZING PDF CONTENT")
    print("=" * 50)
    
    #display metadata from first page
    print("\nFirst Page Metadata:")
    print(pages[0].metadata)
    
    #summary of all pages within the pdf doc
    print(f"\nTotal Pages: {len(pages)}")
    print("-" * 50)
    
    total_chars = 0
    for i, page in enumerate(pages):
        char_count = len(page.page_content)
        total_chars += char_count
        print(f"Page {i + 1}: {char_count:,} characters")
    
    print(f"\nTotal content: {total_chars:,} characters")
    
    #simple search for demonstration
    print("\n" + "=" * 50)
    print("SAMPLE CONTENT PREVIEW (First 300 chars of page 1)")
    print(pages[0].page_content[:300] + "...\n")
    
    # Initialize embeddings and return vectorstore
    print("INITIALIZING VECTOR STORE")
    vectorstore = initializedembeddings(pages)
    
    return vectorstore