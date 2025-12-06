from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.vectorstores import FAISS
from fastembed import TextEmbedding
from dotenv import load_dotenv
import random
import os

load_dotenv()

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Resume.csv')
persist_dir = os.path.join(script_dir, 'faiss_index')

def get_resume_embeddings(embedding_model: str = "models/gemini-embedding-001") -> FAISS:
    """
    Load resume data from a CSV file, generate embeddings using Google Generative AI,
    and store them in a FAISS vector store.

    Args:
        file_path (str): The path to the CSV file containing resume data.
        embedding_model (str): The embedding model to use. Default is "gemini-pro".

    Returns:
        FAISS: A FAISS vector store containing the resume embeddings.
    """
    # Load the CSV file
    loader = CSVLoader(file_path=file_path,
                       encoding='utf-8',
                       csv_args={"delimiter": ",", "quotechar": '"'})

    all_documents = loader.load()

    # Randomly sampling 50 resumes, running the embedding model locally. Taking too long for large number of documents.
    documents = random.sample(all_documents, min(50, len(all_documents)))

    # Initialize the embedding model
    embeddings = FastEmbedEmbeddings(model_name='BAAI/bge-small-en-v1.5')

    if not os.path.exists(persist_dir):
        # Create a FAISS vector store from the documents and embeddings
        vector_store = FAISS.from_documents(documents, embeddings)
        vector_store.save_local(persist_dir)
    else:
        # Load the existing FAISS vector store
        vector_store = FAISS.load_local(persist_dir, embeddings, allow_dangerous_deserialization=True)

    # Create a retriever from the vector store to get top 5 similar resumes
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    return retriever

def get_relevant_resumes(query: str, retriever: FAISS) -> list:
    """
    Retrieve relevant resumes based on a query.

    Args:
        query (str): The search query.
        retriever (FAISS): The FAISS retriever containing resume embeddings.

    Returns:
        list: A list of relevant resumes.
    """
    relevant_resumes = retriever.invoke(query)
    return relevant_resumes

if __name__ == "__main__":
    retriever = get_resume_embeddings()
    resumes = get_relevant_resumes("Experienced software engineer with expertise in machine learning and data science.", retriever)
    for i, resume in enumerate(resumes):
        print(f"----- Resume {i} -----")
        print(resume.page_content)
        print("\n")