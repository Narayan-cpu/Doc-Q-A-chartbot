# 📄 Gemma Model Document Q&A

An interactive document-based Q&A web application built with **Streamlit**, **LangChain**, **Groq's LLaMA3**, and **FAISS vector store**. Upload your PDF documents and ask questions — get accurate answers using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📁 Upload and process PDF documents
- ✂️ Chunk and embed document text using Google GenAI embeddings
- 🤖 Ask natural language questions
- 🔍 Retrieves and ranks relevant document chunks using FAISS
- 💬 Answers generated via Groq’s fast LLaMA3-8B model
- 📦 Simple and interactive Streamlit UI
- ⏱️ Shows response time and similar document chunks

---

## 🖼️ Screenshots

### 🏠 Home Page
![Screenshot (17)](https://github.com/user-attachments/assets/ce9debab-17c5-4081-8929-218f2c09ee89)

### 📚 Document Embedding
![Screenshot (18)](https://github.com/user-attachments/assets/2d1cebc0-cba8-4204-a1a9-df5f2c8f9531)

### ❓ Ask Questions
![Screenshot (19)](https://github.com/user-attachments/assets/3f37e277-c3c3-4cc2-a812-c695fec6e869)

---

## ⚙️ Tech Stack

| Component | Tool |
|----------|------|
| UI       | [Streamlit](https://streamlit.io) |
| LLM      | [LLaMA3 via Groq API](https://console.groq.com/) |
| Embeddings | Google Generative AI Embeddings |
| Vector Store | [FAISS](https://github.com/facebookresearch/faiss) |
| Text Processing | LangChain Text Splitters |
| Document Loading | LangChain PDF Directory Loader |
| Prompting | LangChain Prompt Templates |

---

## 🛠️ Setup Instructions

### 🔐 1. Clone the repository

```bash
git clone https://github.com/Narayan-CPU/Doc-Q-A-chartbot
cd Doc-Q-A-chartbot
