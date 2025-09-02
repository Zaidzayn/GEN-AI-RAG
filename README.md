LangChain RAG Chatbot with Groq LPU
A comprehensive LangChain application featuring Retrieval-Augmented Generation (RAG), conversational memory, vector databases, and FastAPI integration using Groq's Language Processing Units (LPU) for high-performance inference.
🚀 Features

Conversational AI Chatbot with memory persistence
RAG (Retrieval-Augmented Generation) for context-aware responses
Vector Database Integration using ChromaDB
Document Loading & Processing capabilities
Structured Outputs and prompt templates
FastAPI REST API with LangServe
Multi-language Translation support
Groq LPU Integration for fast inference
HuggingFace Embeddings for semantic search
Session Management for conversation history

🛠️ Tech Stack

LangChain - LLM application framework
Groq - High-performance LLM inference
ChromaDB - Vector database for embeddings
FastAPI - Web framework for API endpoints
HuggingFace - Sentence transformers for embeddings
LangServe - Deployment framework for LangChain apps

📦 Installation

Clone the repository

bashgit clone <your-repo-url>
cd langchain-rag-chatbot

Install dependencies

bashpip install -r requirements.txt

Set up environment variables
Create a .env file in the root directory:

envGROQ_API_KEY=your_groq_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here

🔧 Key Components
1. Models and Chains

ChatGroq: Primary LLM for chat completions
LCEL (LangChain Expression Language): For chaining components
Prompt Templates: Structured prompts with variables
Output Parsers: String parsing for clean responses

2. Memory Management

ChatMessageHistory: Stores conversation history
RunnableWithMessageHistory: Adds memory to chains
Session Management: Multiple conversation sessions
Message Trimming: Manage token limits

3. Vector Database & RAG

ChromaDB: Vector storage for document embeddings
HuggingFace Embeddings: Sentence transformers for semantic similarity
Document Retrieval: Similarity search for relevant context
RAG Pipeline: Retrieve → Generate pattern

4. API Integration

LangServe: Deploy chains as REST APIs
FastAPI: Web framework with automatic docs
Async Support: Non-blocking operations
Batch Processing: Multiple requests at once

🎯 Use Cases

Customer Support Chatbot - With knowledge base integration
Educational AI Tutor - Personalized learning with memory
Document Q&A System - Query large document collections
Multi-language Translation - Real-time language conversion
Content Generation - Context-aware content creation

📊 Performance Features

Groq LPU: Ultra-fast inference speeds
Async Operations: Non-blocking I/O
Batch Processing: Handle multiple requests efficiently
Memory Management: Token limit handling
Caching: Vector store caching for repeated queries
