# Profielentool API

A FastAPI-based REST API service for the Profielentool application, designed to be deployed on Render.

## Overview

This project provides backend services for the Profielentool application using FastAPI, a modern, fast web framework for building APIs with Python.

## Project Structure

```
Profielentool_API/
├── app/                          # Application package
│   ├── __init__.py
│   ├── main.py                   # Application entry point
│   ├── config.py                 # Configuration settings
│   ├── models/                   # Pydantic models
│   │   ├── __init__.py
|   |   ├── default.py
|   |   ├── schema.py
│   │   └── validation.py
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api.py
│   └── test_arcgis_post.py
└── venv-profielentool-api        # virtual environment that contains the libraries under requirements
├── requirements.in               # Python dependencies (source)
├── requirements.txt              # Python dependencies (pinned)
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## Prerequisites

- Python 3.10.12
- pip and venv

## Installation

1. **Create and activate virtual environment:**

   ```bash
   python3 -m venv venv-profielentool-api
   source venv-profielentool-api/bin/activate  # On Windows: venv-profielentool-api\Scripts\activate
   ```


2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Development

### Running the Application Locally

```bash
python3 -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

- API docs: `http://localhost:8000/docs`

### Running Tests

```bash
pytest tests/
```

### Managing Dependencies

This project uses `pip-compile` for dependency management.

Update dependencies:

```bash
pip install pip-tools
pip-compile requirements.in
```

Then install updated requirements:

```bash
pip install -r requirements.txt
```

## Deployment on Render

### Prerequisites

- Render account (https://dashboard.render.com/)
- GitHub repository with this code

### Deployment Steps

1. **Make a project** on Render
2. **Create a new Web Service** on Render
3. **Connect to your repository** (i.e.GitHub) with this repository and select branch (settings on Render)
4. **Configure the service:**
   - Environment: Python 3.10
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. **Add environment variables** in Render dashboard
6. **Deploy**

### Environment Variables

Set these in your Render dashboard or `.env` file:

- Currently None

### Which Endpoints?

Configurated in app/main.py

## Deploy new version of the API

1. Create a local branch
2. Commit changes
3. Merge branch into main
4. Render polls for a new commit on main and deploys a new version

