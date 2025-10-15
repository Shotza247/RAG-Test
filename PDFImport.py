import os
import sys
from langchain_community.document_loaders import PyPDFLoader
from RAGTest import pagestester

def pdfimport():
    """Load PDF and return initialized vectorstore"""
    print("\n=== PDF Loader ===")
    file_path = input("Example file path:C:\\Users\\RomeoNdlovu\\Downloads\\Grad skills\\Role Based\\AI Based\\RAG-Test\\Enterprise Systems.pdf \nexitEnter or paste the full path to your PDF file: ").strip()
    
    #we remove quotes
    file_path = file_path.strip('"').strip("'")

    if not file_path:
        print("No file path provided. Exiting...")
        return None

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        print("Please check the path and try again.")
        return None

    if not file_path.lower().endswith(".pdf"):
        print("The selected file is not a PDF. Please provide a .pdf file.")
        return None

    print("\nLoading your PDF file...")
    try:
        loader = PyPDFLoader(file_path)
        pages = loader.load()
        print(f"Success! Loaded {len(pages)} pages from '{os.path.basename(file_path)}'")
        
        #process pages and returns the vectorstore
        vectorstore = pagestester(pages)
        return vectorstore
    
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None