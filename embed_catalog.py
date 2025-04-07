import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Hardcoded catalog (since CSV was problematic)
catalog = [
    "SHL Verbal Reasoning Test",
    "SHL Logical Reasoning Test",
    "SHL Coding Assessment",
    "SHL Leadership Skills Test",
    "SHL Communication Skills Assessment"
]

# Load model and encode
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(catalog)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings).astype("float32"))

# Save index and catalog
faiss.write_index(index, "catalog.index")
with open("catalog.pkl", "wb") as f:
    pickle.dump(catalog, f)

print("✅ Catalog indexed and saved!")
