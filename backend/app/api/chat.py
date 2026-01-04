from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embeddings import embed_query
from app.services.vector_store import similarity_search
from app.services.llm import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/")
def chat(request: QueryRequest):
    query = request.query

    # 1️⃣ Embed query
    query_embedding = embed_query(query)

    # 2️⃣ Retrieve chunks
    results = similarity_search(query_embedding, top_k=4)

    if not results:
        return {
            "answer": "No relevant information found in the document.",
            "sources": []
        }

    context = "\n\n".join([r["text"] for r in results])

    # 3️⃣ Gemini answer
    answer = generate_answer(query, context)

    return {
        "answer": answer,
        "sources": [
            {
                "source": r["metadata"].get("source", "document"),
                "page": r["metadata"].get("page")
            }
            for r in results
        ]
    }
