from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from rag_engine import query_rag, ingest_pdf

import shutil
import os
import uuid
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS: read allowed origins from env (comma-separated).
# Defaults to localhost Streamlit port only.
_raw_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:8501")
allowed_origins = [o.strip() for o in _raw_origins.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

    os.makedirs("data", exist_ok=True)
    filename = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join("data", filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        ingest_pdf(file_path, original_name=file.filename)
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    return {"message": "File uploaded and ingested successfully."}

@app.post("/ask/")
def ask_post(payload: QueryRequest):
    answer = query_rag(payload.query)
    return {"response": answer}

