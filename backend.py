from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from pydantic import BaseModel
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing, allow all origins
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load pre-computed index and catalog
with open("catalog.pkl", "rb") as f:
    catalog = pickle.load(f)

index = faiss.read_index("catalog.index")
model = SentenceTransformer("all-MiniLM-L6-v2")

class Query(BaseModel):
    query: str

@app.post("/recommend")
async def recommend(data: Query):
    query_embedding = model.encode([data.query])
    D, I = index.search(np.array(query_embedding).astype("float32"), k=5)
    results = [catalog[i] for i in I[0]]
    return {"recommendations": results}