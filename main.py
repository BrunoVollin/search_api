import os
from openai_gpt.gpt import Bot
import uvicorn
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
from fastapi.responses import FileResponse

import pytesseract

from search.searcher import Searcher
from search.utils import clean_data

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'F:\T\tesseract.exe'

app = FastAPI()

API_KEY = os.environ.get("OPENAI_API_KEY")
bot = Bot(API_KEY)


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


@app.post("/uploadpdf")
async def upload_pdf(file: UploadFile = File(...)):
    upload_dir = "uploads"
    data_dir = "data"

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    file_location = os.path.join(upload_dir, file.filename)
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())

    # Save the filename before opening the file
    filename = file.filename

    # Perform OCR on the PDF file and save the extracted text to a .txt file in the data directory
    with open(file_location, "rb") as file:
        pdf_reader = PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            # You may need to use an additional library or approach to extract images
            # from the PDF pages for OCR.
            # Alternatively, you can extract text directly without OCR if the PDF contains text.
            text += page.extract_text()

        txt_filename = os.path.splitext(filename)[0] + ".txt"
        txt_file_location = os.path.join(data_dir, txt_filename)
        with open(txt_file_location, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)

    return {"filename": filename}


def isGraphicResponse(question: str):
    return True


@app.post("/search")
async def search_document(pdf_name: str, question: str):
    data_dir = "data"
    txt_filename = os.path.splitext(pdf_name)[0] + ".txt"
    txt_file_location = os.path.join(data_dir, txt_filename)

    if not os.path.exists(txt_file_location):
        raise HTTPException(status_code=404, detail="Text file not found")

    searcher = Searcher()
    with open(txt_file_location, "r", encoding="utf-8") as file:
        document = file.read()
    relevant_paragraphs = searcher.advanced_search(question, document)
    cleaned_paragraphs = clean_data(relevant_paragraphs)
    print(cleaned_paragraphs)

    response = bot.generate_chart(question, " ".join(cleaned_paragraphs)) if isGraphicResponse(
        question) else bot.generate(question, " ".join(cleaned_paragraphs))

    return response


    ...


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
