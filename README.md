## Introduction

The **MultiPDF Chat App** is a Python application that allows you to chat with **multiple PDF documents** using natural language. You can ask questions about the PDFs, and the app will provide accurate responses based on their content. It uses a language model (via OpenAI and LangChain) to generate intelligent answers.

The chatbot will only respond to questions related to the uploaded PDFs.

---

## How It Works

MultiPDF Chat App - System Flow:

1. **PDF Loading**: The app reads and extracts text from multiple PDF files.
2. **Text Chunking**: The extracted text is divided into smaller, manageable chunks.
3. **Embedding Generation**: A language model generates vector representations (embeddings) of the text chunks.
4. **Similarity Matching**: Your question is compared to the embeddings to find the most relevant chunks.
5. **Response Generation**: The selected content is passed to the language model to generate a natural language answer.

---

## Dependencies and Installation

To install and run the MultiPDF Chat App, follow these steps:

1. **Clone the repository:**

```bash
git clone https://github.com/oussamalembarki/Multi-PDF-AI-Chatbot-with-LangChain-OpenAI-Streamlit-App.git
cd Multi-PDF-AI-Chatbot-with-LangChain-OpenAI-Streamlit-App
```
2. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set your OpenAI API key by creating a .env file in the root directory with:**

   ```bash
   OPENAI_API_KEY=your_secret_api_key
   ```bash

## Usage

1. Make sure you've installed dependencies and added your API key to the .env file.
2. Run the application using Streamlit.
3. The app will launch in your default web browser.
4. Upload multiple PDF documents.
5. Ask questions in natural language using the chat interface.
