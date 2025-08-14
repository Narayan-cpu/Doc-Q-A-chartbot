# 📄 Gemma Document Q&A RAG Model

An interactive document-based Q&A web application built with **Streamlit**, **LangChain**, **Groq's LLaMA3**, and **FAISS vector store**. Upload your PDF documents and ask questions — get accurate answers using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features:

- 📁 Upload and process PDF documents
- ✂️ Chunk and embed document text using Google GenAI embeddings
- 🤖 Ask natural language questions
- 🔍 Retrieves and ranks relevant document chunks using FAISS
- 💬 Answers generated via Groq’s fast LLaMA3-8B model
- 📦 Simple and interactive Streamlit UI
- ⏱️ Shows response time and similar document chunks

---

## 🖼️ Screenshots :

### 🏠 Home Page
![Screenshot (17)](https://github.com/user-attachments/assets/ce9debab-17c5-4081-8929-218f2c09ee89)

### 📚 Document Embedding
![Screenshot (18)](https://github.com/user-attachments/assets/2d1cebc0-cba8-4204-a1a9-df5f2c8f9531)

### ❓ Ask Questions
![Screenshot (19)](https://github.com/user-attachments/assets/3f37e277-c3c3-4cc2-a812-c695fec6e869)

---

## ⚙️ Tech Stack

| Component         | Tool |
|------------------|------|
| Frontend (UI)     | [Streamlit](https://streamlit.io) |
| Language Model    | [LLaMA3 via Groq API](https://console.groq.com/) |
| Text Embeddings   | Google Generative AI Embeddings |
| Vector Store      | [FAISS](https://github.com/facebookresearch/faiss) |
| Text Chunking     | LangChain Text Splitters |
| PDF Document Loading | LangChain PDF Directory Loader |
| Prompt Formatting | LangChain Prompt Templates |

---

## 🛠️ Setup Instructions :

Follow these steps to set up and run the application on your local machine.

---

### 🔐 1. Clone the Repository :

```bash
git clone https://github.com/Narayan-CPU/Doc-Q-A-chartbot
cd Doc-Q-A-chartbot
````

This will download the full project to your local machine.

---

### 🛠️ 2. Create a Virtual Environment (Recommended) :

```bash
python -m venv venv
# Activate the environment:
# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate
```

A virtual environment keeps your project’s dependencies isolated.

---

### 📦 3. Install Dependencies :

Install all required Python libraries using:

```bash
pip install -r requirements.txt
```

Make sure your `requirements.txt` includes:

```txt
streamlit
python-dotenv
langchain
langchain-community
langchain-groq
langchain-google-genai
faiss-cpu
```

---

### 🔑 4. Set Environment Variables

Create a `.env` file in the root directory and add the following:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

These keys are required to access Groq's LLaMA3 model and Google's embedding model.

---

### 📁 5. Add Your PDF Documents

Create a folder called `data_files` in the root directory and place your PDF documents inside it:

```
data_files/
 ├── doc1.pdf
 ├── doc2.pdf
```

The app will load and process all PDF files from this folder.

---

### ▶️ 6. Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open your browser and navigate to:

```
http://localhost:8501
```

---

## 💡 How It Works (Behind the Scenes)

This app uses **Retrieval-Augmented Generation (RAG)**. Here’s the flow:

1. **Document Loading**: PDF files are loaded and converted to text using `PyPDFDirectoryLoader`.
2. **Chunking**: Long texts are split into smaller chunks with overlaps for better context.
3. **Embedding**: Chunks are converted to numerical vectors using Google GenAI embeddings.
4. **Storage**: Vectors are stored in a FAISS vector store.
5. **User Query**: When a question is asked, relevant document chunks are retrieved using vector similarity.
6. **Answer Generation**: Retrieved chunks + question are passed to Groq's LLaMA3 model.
7. **Response**: The generated answer and matching documents are shown on the UI.

---

## 🧭 Architecture Overview

```
PDFs → Text Loader → Text Splitter → Embeddings → FAISS Store
                                    ↑
     User Question → Retriever ← Similar Chunks
                          ↓
                      Prompt Template
                          ↓
                   Groq LLaMA3 via LangChain
                          ↓
                      Final Answer
```

---

## 📁 Project Structure

```
Gemma-Doc-QA/
│
├── app.py                 # Streamlit application
├── data_files/            # Folder containing PDF documents
├── .env                   # Environment file (API keys)
├── requirements.txt       # All Python dependencies
└── README.md              # Project documentation
```

---

## ☁️ Deployment (Streamlit Cloud)

You can deploy the app on [Streamlit Cloud](https://streamlit.io/cloud):

1. Push your code to a GitHub repository.
2. Login to Streamlit Cloud and click "New App".
3. Connect your GitHub repo.
4. Add secrets in **Settings > Secrets**:

   ```
   GROQ_API_KEY=your_groq_key
   GOOGLE_API_KEY=your_google_key
   ```
5. Click **Deploy**.

Your app will be live on a public URL!

---

## ✅ Use Cases

* 🧑‍🎓 Academic Research Assistants
* 📚 FAQ Bots for Technical Manuals
* 💼 Legal Document Analysis
* 🏥 Medical Report Question Answering
* 🧠 Personal Knowledgebase Assistant

---

## 🧠 What You'll Learn :

* ✅ How to build Retrieval-Augmented Generation (RAG) pipelines
* ✅ How to connect LangChain with Groq and Google AI
* ✅ How to build interactive LLM apps with Streamlit
* ✅ How to use FAISS for semantic search

---

## 🙌 Credits :

* [LangChain](https://www.langchain.com/)
* [Groq API](https://console.groq.com/)
* [Google Generative AI](https://ai.google.dev/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Streamlit](https://streamlit.io)

---

## 📬 Contact

Developed with ❤️ by [Narayan Naik](https://github.com/Narayan-CPU)
If you found this helpful, feel free to ⭐ the repo and share feedback!
