# 🧠 TalkToPDF – AI-Powered PDF Chatbot

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-orange)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-005571)](https://fastapi.tiangolo.com/)
[![Gemini API](https://img.shields.io/badge/LLM-Gemini%202.5%20Pro-34a853)](https://ai.google.dev/)
[![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)](https://www.trychroma.com/)

> 💬 Ask your PDFs anything — and get smart answers instantly. No fluff. No hallucination. Just knowledge.

---

## 📌 What is TalkToPDF?

**TalkToPDF** is an AI chatbot that allows you to interact with your PDF documents using natural language. Powered by **Google Gemini 2.5 Pro** and **ChromaDB**, it performs semantic search on document chunks and generates highly relevant answers with context.

Whether it’s academic papers, legal docs, contracts, or reports — this bot understands and responds like a real assistant.

---

## ✨ Features

- ✅ Upload any PDF (up to 200MB)
- 🧠 LLM-based Q&A using **Gemini 2.5 Pro**
- 🧩 Chunked document parsing & semantic embeddings
- 🗃️ Persistent vector DB with **ChromaDB**
- 🚀 FastAPI backend for file ingestion and query routing
- ⚡ Interactive **Streamlit** frontend for chatting

---

## 🛠️ Tech Stack

| Layer        | Tech Used                         |
|--------------|----------------------------------|
| Frontend     | Streamlit                        |
| Backend      | FastAPI                          |
| Embeddings   | SentenceTransformers (MiniLM)    |
| Vector DB    | ChromaDB                         |
| LLM          | Gemini 2.5 Pro                   |
| Utilities    | PyMuPDF, dotenv, uvicorn         |

---

## 🧪 How It Works

1. 📄 You upload a PDF.
2. ✂️ The PDF is split into semantically meaningful chunks.
3. 🧬 Chunks are embedded using `all-MiniLM-L6-v2`.
4. 🧠 Embeddings are stored in **ChromaDB**.
5. ❓ You ask a question.
6. 🔍 Similar chunks are retrieved based on embedding similarity.
7. 🗣️ A prompt is constructed and sent to **Gemini 2.5 Pro**.
8. 🤖 You get a relevant and context-aware answer.

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/talktopdf.git
cd talktopdf
````

### 2. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
.\venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

### 4. Start the backend

```bash
uvicorn backend.main:app --reload
```

### 5. Launch the frontend

```bash
streamlit run app.py
```

> ⚠️ Make sure both `app.py` (frontend) and `backend/` (FastAPI backend) are in the root directory or appropriately routed.

---

## 📁 Project Structure

```bash
talktopdf/
├── frontend/
|   |──app.py                # Streamlit frontend
├── backend/
│   ├── main.py                # FastAPI app
│   ├── rag_core.py            # RAG logic
│   ├── utils.py               # Text extraction and chunking
│   ├── model_config.py        # Gemini + embedder config
├── chroma_db/                 # Persistent vector DB storage
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Roadmap

* [ ] Chat history with timestamped logs
* [ ] Source highlighting in answers
* [ ] Support for multi-PDF queries
* [ ] Export Q\&A history as PDF
* [ ] Hugging Face or Vercel deployment

---

## 📚 Use Cases

* Research paper Q\&A
* Business or pitch deck understanding
* Legal contract clarification
* Personal note summarization
* Resume or SOP analyzers

---

## 🧠 Example Prompt

> **"What does Section 3.2 of the agreement say about termination rights?"**

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE). Feel free to use it, modify it, and deploy it.

---

## 🙌 Contributions

Pull requests and stars are always welcome!

If you like the project, consider dropping a ⭐ — it helps more people discover it.

---

## ✉️ Contact

Created by [Your Name](https://github.com/your-username).
DMs open for collabs, contributions, or questions!

---

```


