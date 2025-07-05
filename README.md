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
![Home Screenshot](Screenshot (17).png)

### 📚 Document Embedding
![Embedding Screenshot](Screenshot (18).png)

### ❓ Ask Questions
![QA Screenshot](Screenshot (19).png)

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
