import os
import sys
from langchain_community.document_loaders import PyPDFLoader
from RAGTest import pagestester

def main():
    print("=== PDF Loader ===")
    file_path = input("Enter or paste the full path to your PDF file: ").strip()

    if not file_path:
        print("No file path provided. Exiting...")
        sys.exit(1)

    if not os.path.exists(file_path):
        print("File not found. Please check the path and try again.")
        sys.exit(1)

    if not file_path.lower().endswith(".pdf"):
        print("The selected file is not a PDF. Please provide a .pdf file.")
        sys.exit(1)

    print("\nLoading your PDF file...")
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    print(f"Success! Loaded {len(pages)} pages from '{os.path.basename(file_path)}'\n")
    pagestester(pages)

if __name__ == "__main__":
    main()
