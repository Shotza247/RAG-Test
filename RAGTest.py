from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

#Look at the first page
#print("FIRST PAGE CONTENT")
#print("=" * 50)
#print(pages[0].page_content)
#print("\n")

def pagestester(pages):
    #See what information is on the 1st page
    print("FIRST PAGE METADATA")
    print("=" * 50)
    print(pages[0].metadata)
    print("\n")
    
    #Loop through all pages and print summary info
    print("ALL PAGES SUMMARY")
    print("=" * 50)
    
    for i, page in enumerate(pages):
        print(f"Page {i + 1}: {len(page.page_content)} characters")
    print("\n")
        
    # Search for a specific word
    print("SEARCHING FOR 'React' IN ALL PAGES")
    print("=" * 50)
    search_word = "React"
        
    for i, page in enumerate(pages):
        if search_word in page.page_content:
            print(f"✓ Found '{search_word}' on page {i + 1}")
            print("\n")
            
            # Want to see page 2? Just change the number below!
            page_number = 1 
            print("=" * 50)
            print(f"VIEWING PAGE {page_number + 1}")
            print("=" * 50)
            print(pages[page_number].page_content[:500]) 
            print("...\n")

#Exercises
#Exercise 1: Print the last page
#print(pages[-1].page_content)

#Exercise 2: Count total characters in all pages
#total_chars = sum(len(page.page_content) for page in pages)
#print(f"Total characters in document: {total_chars}")

#Exercise 3: Find which page mentions "MongoDB"

#print("SEARCHING FOR 'MongoDB' IN ALL PAGES")
#print("=" * 50)

#pageholder = " "

#for i, page in enumerate(pages):
#    if "MongoDB" in page.page_content:
#        results = f"MongoDB mentioned on page {i + 1}"
#    else:
#        results = pageholder + f"{i + 1},"
#    print(results)

# Exercise 4: Save first page to a text file
# with open("first_page.txt", "w", encoding="utf-8") as f:
#     f.write(pages[0].page_content)
# print("Saved first page to first_page.txt")