# Document Search API

This project provides an API that allows users to submit questions about a document. In response, the API returns relevant paragraphs from the document using semantic similarity powered by spaCy.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository:**

    \```bash
    git clone https://github.com/your_username/document_search_api.git
    cd document_search_api
    \```

    Replace `your_username` with your actual GitHub username and `document_search_api` with your repository name if different.

2. **Set Up a Virtual Environment (Recommended):**

    \```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    \```

3. **Install the Required Packages:**

    \```bash
    pip install fastapi[all] uvicorn spacy
    \```

4. **Download the spaCy Language Model:**

    For Portuguese:

    \```bash
    python -m spacy download pt_core_news_lg
    \```

## Usage

1. **Start the API Server:**

    \```bash
    python main.py
    \```

2. **Access the API:**

    The API will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000). You can use tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to make requests to the API.

    Example POST request to the `/search` endpoint with a question:

    \```bash
    curl -X POST "http://127.0.0.1:8000/search" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "question=Consequencia aquecimento global?"
    \```

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.
