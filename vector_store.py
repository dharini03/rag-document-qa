import faiss
import numpy as np
from sentence_transformers.SentenceTransformer import SentenceTransformer
from typing import List


class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.texts: List[str] = []

    def add_texts(self, texts: List[str]) -> None:
        if not texts:
            return
        embeddings: np.ndarray = np.array(self.model.encode(texts), dtype=np.float32)
        self.index.add(x=embeddings)  # type: ignore
        self.texts.extend(texts)

    def search(self, query: str, top_k: int = 3) -> List[str]:
        if not self.texts:
            return []
        query_vec: np.ndarray = np.array(self.model.encode([query]), dtype=np.float32)
        distances, indices = self.index.search(x=query_vec, k=top_k)   # type: ignore
        return [self.texts[i] for i in indices[0]]


VECTOR_DB = VectorStore()
