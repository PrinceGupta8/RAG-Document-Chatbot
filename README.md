# Context-Aware PDF Question Answering with Groq and FAISS

This project is a **Streamlit-based AI assistant** that enables users to **ask context-aware questions from a PDF document**. It uses **Groq's Mixtral model** for intelligent responses and **FAISS** for efficient similarity search on embedded text chunks.

## Features

- **PDF-Based Question Answering**: Upload a PDF and ask questions related to its content.
- **Context-Aware Responses**: Ensures answers are derived directly from the uploaded document.
- **Efficient Text Embedding & Retrieval**: Uses OpenAI embeddings and FAISS for fast search.
- **Interactive Chat**: Enables a conversational experience for users.

## Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq (Mixtral-8x7B-32768 model)**
- **FAISS (Facebook AI Similarity Search)**
- **OpenAI Embeddings**

## Installation

### Prerequisites

- Python 3.8+
- Groq API Key
- OpenAI API Key

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/PrinceGupta8/context-aware-pdf-qa.git
   cd context-aware-pdf-qa
   ```
2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Enter your Groq API Key** in the environment variables or Streamlit sidebar.
2. **Upload a PDF document** (e.g., `attention.pdf`).
3. **Click 'Embedding'** to process the document.
4. **Ask a question** related to the document's content.
5. **Receive an AI-generated response** based on retrieved context.

## Example

**Input:**

```
What is the main concept discussed in the first section of the document?
```

**Output:**

```
The first section of the document discusses the concept of self-attention in transformer models...
```

## API Keys

- Get your **Groq API Key** from [Groq](https://groq.com/).
- Get your **OpenAI API Key** from [OpenAI](https://openai.com/).
- Set these as environment variables (`groq_api_key` and `openai_api_key`) or input them in the Streamlit UI.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

🚀 **Enhance your PDF-based research with AI-powered context-aware answers!**

