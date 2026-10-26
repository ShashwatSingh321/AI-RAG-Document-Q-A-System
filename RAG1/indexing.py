from dotenv import load_dotenv
from file_reader import extract_paragraphs
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vector_store = InMemoryVectorStore(embedding)

chunks = extract_paragraphs("../pdfs/Rag_Test.pdf")
vector_store.add_texts(texts=chunks)

print(f"indexed {len(chunks)} chunks")
