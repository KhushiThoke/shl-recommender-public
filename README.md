# SHL Recommender 🔍

A web-based Retrieval-Augmented Generation (RAG) tool using the SHL product catalog. It returns smart job/product recommendations based on user queries.

## Features
- FastAPI backend with recommendation endpoint
- Streamlit frontend UI
- Sentence-Transformers for semantic search

## Usage

1. Clone the repo  
2. Install dependencies: `pip install -r requirements.txt`  
3. Run backend: `python backend.py`  
4. Run frontend: `streamlit run frontend.py`

## API Endpoint

`POST /recommend`  
Input:  
```json
{ "query": "coding assessment" }
