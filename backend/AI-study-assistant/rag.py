from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = PyPDFLoader("notes.pdf")
documents = loader.load()

print("Total pages loaded:", len(documents))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

docs = text_splitter.split_documents(documents)

print("Total chunks created:", len(docs))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

vectorstore = FAISS.from_documents(docs, embeddings)


def get_answer_from_notes(query: str):
    results = vectorstore.similarity_search(query, k=3)

    if not results:
        return "No relevant information found in notes."

    combined_text = "\n\n".join([doc.page_content for doc in results])
    return combined_text
