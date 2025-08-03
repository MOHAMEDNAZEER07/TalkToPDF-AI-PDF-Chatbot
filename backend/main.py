from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from rag_engine import query_rag, ingest_pdf

import shutil
import os
import uuid
from pydantic import BaseModel

app = FastAPI()

# CORS middleware if using frontend like Streamlit/React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change this in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs("data", exist_ok=True)
    filename = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join("data", filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_pdf(file_path)

    return {"message": f"File {filename} uploaded and ingested."}

@app.post("/ask/")
def ask_post(payload: QueryRequest):
    answer = query_rag(payload.query)
    return {"response": answer}
