import streamlit as st
import os
import time
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# Load API keys
groq_api_key = os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

st.title("📄 Gemma Model RAG Document Q&A Model")

# Initialize LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="Llama3-8b-8192"
)

# Prompt template
prompt = ChatPromptTemplate.from_template("""
<context>
{context}
</context>

Question: {input}
""")

# Document vector embedding function
def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader = PyPDFDirectoryLoader("./data_files")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

# UI: Button to prepare DB
if st.button("📚 Prepare Document Embeddings"):
    vector_embedding()
    st.success("✅ Vector Store is ready.")

# User Input
query = st.text_input("❓ Ask a question from the documents:")

# Handle question
if query and "vectors" in st.session_state:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({'input': query})
    end = time.process_time()

    st.markdown(f"⏱️ **Response time:** `{end - start:.2f}` seconds")
    st.write("### 💬 Answer:")
    st.write(response['answer'])

    # Similar Documents
    with st.expander("🔍 Similar Document Chunks"):
        docs = retriever.get_relevant_documents(query)
        for doc in docs:
            st.write(doc.page_content)
            st.write("----")
else:
    if query:
        st.warning("⚠️ Please embed documents first by clicking the button above.")



