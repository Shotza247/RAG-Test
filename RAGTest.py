from VectorEmbeddings import initializedembeddings

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
            print(f"VIEWING PAGE {page_number + 1}")
            print("=" * 50)
            print(pages[page_number].page_content[:500])
            print("\n")
    
    initializedembeddings(pages)


# Exercise 4: Save first page to a text file
# with open("first_page.txt", "w", encoding="utf-8") as f:
#     f.write(pages[0].page_content)
# print("Saved first page to first_page.txt")