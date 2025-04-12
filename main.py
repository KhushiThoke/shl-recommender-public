from fastapi import FastAPI, Query
import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util

app = FastAPI()

# Load catalog safely whether or not header is present
try:
    catalog = pd.read_csv("shl_catalog.csv")
    if "title" in catalog.columns:
        titles = catalog["title"].tolist()
    else:
        titles = catalog.iloc[:, 0].tolist()
except:
    catalog = pd.read_csv("shl_catalog.csv", header=None)
    titles = catalog.iloc[:, 0].tolist()

# Load SentenceTransformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load or generate embeddings
try:
    catalog_embeddings = torch.load("catalog.pkl", map_location=torch.device("cpu"))
except:
    catalog_embeddings = model.encode(titles, convert_to_tensor=True)
    torch.save(catalog_embeddings, "catalog.pkl")

@app.get("/")
def home():
    return {"message": "SHL Recommender API is live!"}

@app.get("/search")
def recommend(query: str = Query(..., description="Enter job title or keyword")):
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(query_embedding, catalog_embeddings)[0]
    top_idx = torch.argmax(similarities).item()
    return {
        "query": query,
        "recommended_assessment": titles[top_idx],
        "score": float(similarities[top_idx])
    }



