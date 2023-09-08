from search.searcher import Searcher
from search.utils import clean_data
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/search")
async def search_document(question: str):
    searcher = Searcher()

    with open('data/aa.txt', 'r', encoding='utf-8') as file:
        document = file.read()

    relevant_paragraphs = searcher.advanced_search(question, document)
    cleaned_paragraphs = clean_data(relevant_paragraphs)

    return {"results": cleaned_paragraphs}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
