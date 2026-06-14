# AI Research Agent

An Agentic AI application built with Python, Streamlit, Groq LLM, ChromaDB, and Retrieval-Augmented Generation (RAG).

The system allows users to upload PDF documents, ask questions about them, search the web for current information, and perform combined document + web research using multiple AI agents.

## Features

### Document Analysis
- Upload PDF documents
- Automatic text extraction
- Document chunking
- Semantic indexing using ChromaDB
- Retrieval-Augmented Generation (RAG)

### Web Search
- Search the internet for recent information
- Retrieve external knowledge beyond uploaded documents
- Generate context-aware responses

### Multi-Agent Architecture
The application uses specialized agents:

#### Router Agent
Determines which agent should handle a user request.

#### Chat Agent
Answers questions using document context retrieved from the vector database.

#### Search Agent
Handles web-based information retrieval and current-event queries.

#### Research Agent
Combines document knowledge and web search results to generate deeper insights and comparisons.

#### Planner Agent (In Progress)
Will determine which tools and data sources are required before executing a task.

## Architecture

User Query
→ Router Agent
→ Chat Agent / Search Agent / Research Agent
→ Response

For document-based queries:

PDF Upload
→ Text Extraction
→ Chunking
→ ChromaDB Vector Store
→ Semantic Retrieval
→ LLM Response

For research queries:

User Query
→ Document Retrieval
→ Web Search
→ Context Aggregation
→ LLM Response

## Tech Stack

- Python
- Streamlit
- Groq API
- ChromaDB
- Sentence Transformers
- Retrieval-Augmented Generation (RAG)

## Current Capabilities

- PDF document understanding
- Semantic search over uploaded documents
- Web search integration
- Multi-agent orchestration
- Research workflows combining internal and external knowledge

## Future Enhancements

- Planner Agent
- LangGraph Integration
- Multi-step Agent Workflows
- Memory Management
- Multi-document Knowledge Base
- Tool Calling Framework
- Autonomous Research Pipelines

## Project Goal

This project is being built to explore real-world Agentic AI systems by combining:

- LLMs
- RAG
- Vector Databases
- Multi-Agent Architectures
- Planning and Reasoning Workflows

The focus is on understanding how modern AI agents retrieve information, reason over multiple sources, and coordinate specialized tools to solve complex tasks.
