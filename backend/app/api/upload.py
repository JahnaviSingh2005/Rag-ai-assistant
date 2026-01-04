from fastapi import APIRouter, UploadFile, File

from app.services.document_loader import load_document
from app.services.chunker import chunk_text
from app.services.embeddings import embed_chunks
from app.services.vector_store import add_to_vector_store, reset_vector_store

router = APIRouter()

# @router.post("/")
# async def upload_file(file: UploadFile = File(...)):
#     # 🔁 IMPORTANT: clear old embeddings before re-upload
#     reset_vector_store()

#     # 📄 Load document (pdfplumber-based extraction)
#     raw_chunks = load_document(file)

#     if not raw_chunks:
#         return {"message": "No readable text found in document."}

#     # ✂️ Chunk text
#     chunks = []
#     for rc in raw_chunks:
#         chunks.extend(
#             chunk_text(
#                 rc["text"],
#                 rc["metadata"]
#             )
#         )

#     if not chunks:
#         return {"message": "Document text could not be chunked."}

#     # 🧠 Generate embeddings
#     embeddings = embed_chunks(chunks)

#     # 📦 Store in vector DB
#     add_to_vector_store(chunks, embeddings)

#     return {
#         "message": "Document uploaded and indexed successfully",
#         "chunks_indexed": len(chunks)
#     }
@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    print("UPLOAD ENDPOINT HIT")

    reset_vector_store()

    raw_chunks = load_document(file)
    print("RAW CHUNKS:", len(raw_chunks))

    chunks = []
    for rc in raw_chunks:
        split_chunks = chunk_text(rc["text"], rc["metadata"])
        chunks.extend(split_chunks)

    print("FINAL CHUNKS:", len(chunks))

    embeddings = embed_chunks(chunks)
    print("EMBEDDINGS COUNT:", len(embeddings))

    add_to_vector_store(chunks, embeddings)
    print("UPLOAD COMPLETE")

    return {
        "message": "Document uploaded and indexed",
        "chunks": len(chunks)
    }
