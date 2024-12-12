# Chat Applications using GROQ and OpenAI

This repository contains two Streamlit-based web applications that demonstrate the use of Retrieval-Augmented Generation (RAG) and OpenAI's GPT models to build intelligent chatbots. These applications showcase how to process documents and generate responses based on user queries.

## Applications

### 1. Simple RAG Chat Application using GROQ

This application uses GROQ AI for language generation and OpenAI embeddings for creating a context-aware chatbot that can answer questions based on the content of uploaded PDF documents.

#### Features
- **Document Upload**: Allows users to upload PDF documents for context.
- **Query Input**: Responds to user queries based on the uploaded document.
- **Vector Store Creation**: Uses FAISS to create efficient document retrieval embeddings.
- **Language Model**: Utilizes GROQ AI's Gemma2-9B-IT model for accurate responses.

#### Prerequisites
- Python 3.8+
- Libraries: `streamlit`, `langchain`, `langchain-community`, `langchain-openai`, `langchain-groq`, `python-dotenv`, `faiss-cpu`
- API keys for OpenAI (`OPENAI_API_KEY`) and GROQ AI (`GROQ_API_KEY`)
- Environment variables: `LANGCHAIN_API_KEY`, `LANGCHAIN_PROJECT`, `LANGCHAIN_TRACING_V2`

#### Installation
```bash
git clone https://github.com/yourusername/rag-chat-app.git
cd rag-chat-app
pip install -r requirements.txt
```

#### Usage
1. Set up `.env` file with API keys.
2. Run the app:
   ```bash
   streamlit run app.py
   ```
3. Interact via the web interface.

---

### 2. Simple Chat Application using OpenAI

This application uses OpenAI's GPT models to create a chatbot with customizable parameters like temperature, model selection, and token limits.

#### Features
- **Customizable Inputs**: Adjust model, temperature, and token limits via a sidebar.
- **Query Input**: Responds to user questions using OpenAI's GPT models.

#### Prerequisites
- Python 3.8+
- Libraries: `streamlit`, `langchain`, `python-dotenv`
- API key for OpenAI (`OPENAI_API_KEY`)

#### Installation
```bash
git clone https://github.com/yourusername/openai-chat-app.git
cd openai-chat-app
pip install -r requirements.txt
```

#### Usage
1. Set up `.env` file with the OpenAI API key.
2. Run the app:
   ```bash
   streamlit run openai_chat_app.py
   ```
3. Use the sidebar to set parameters and input queries.

## File Structure
```
├── rag-chat-app
│   ├── app.py                  # RAG Chat App code
│   ├── requirements.txt        # Dependencies
│   ├── .env                    # Environment variables
│   └── README.md               # Documentation
├── openai-chat-app
│   ├── openai_chat_app.py      # OpenAI Chat App code
│   ├── requirements.txt        # Dependencies
│   ├── .env                    # Environment variables
│   └── README.md               # Documentation
```

## Acknowledgments
- [LangChain](https://www.langchain.com/) for foundational components.
- [GROQ AI](https://groq.com/) and [OpenAI](https://openai.com/) for the language models.
- [Streamlit](https://streamlit.io/) for the frontend framework.
