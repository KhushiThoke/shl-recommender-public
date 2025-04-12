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


Testing Your API 
1. Base Endpoint Check
 Endpoint: GET /
 URL: http://127.0.0.1:8000/
 Expected Response:{ "message": "SHL Recommender API is live!"}
2. Search Endpoint Check
Endpoint: GET /search?query=logical thinking

URL Example: http://127.0.0.1:8000/search?query=logical thinking


[{ "product_name": "Product A",
    "url": "https://example.com/product-a",
    "adaptive_support": "Yes",
    "description": "Detailed info about Product A",
    "duration": 45,
    "remote_support": "No",
    "test_type": ["Cognitive", "Behavioral"]
  },
  ...]

  
Public URL
https://shl-recommender-public-1.onrender.com

