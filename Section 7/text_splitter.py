from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'sample_text.txt')

loader = TextLoader(file_path) # Using TextLoader to load a plain text file

document = loader.load() # Load the document

text_splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=80) # Initialize the text splitter with 400 character chunks and 80 character overlap
texts = text_splitter.split_documents(document) # Split the document into chunks

print(f"Number of text chunks: {len(texts)}")

for i, chunk in enumerate(texts):
    print(f"\n--- Chunk {i + 1} ---\n")
    print(chunk.page_content)

# Another notable option is to use RecursiveCharacterTextSplitter for more complex splitting strategies. For the same document, the recursive splitter 
# made 7 chunks more than the Character Text Splitter