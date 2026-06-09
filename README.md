<<<<<<< HEAD
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
│   ├── api/                      # API routes
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── endpoints/        # API endpoints
│   ├── models/                   # Pydantic models
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── database/                 # Database related
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models.py
│   └── core/                     # Core utilities
│       ├── __init__.py
│       └── middleware.py
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api.py
├── requirements.in               # Python dependencies (source)
├── requirements.txt              # Python dependencies (pinned)
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── Makefile                      # Development commands
└── README.md                     # This file
```

## Prerequisites

- Python 3.9+ (3.10.12)
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
uvicorn app.main:app --reload
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

- Render account
- GitHub repository with this code

### Deployment Steps

1. **Connect your repository** to Render
2. **Create a new Web Service** on Render
3. **Configure the service:**
   - Environment: Python 3.11
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. **Add environment variables** in Render dashboard
5. **Deploy**

### Environment Variables

Set these in your Render dashboard or `.env` file:

- `DATABASE_URL`: PostgreSQL connection string
- `ENVIRONMENT`: `production` or `development`
- `DEBUG`: `False` for production

## API Documentation

API endpoints follow RESTful conventions. Documentation is auto-generated and available at `/docs` when running the application.

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests
4. Submit a pull request

## License

[Add your license information]

## Support

For issues and questions, please open an issue in the repository.
=======
# profielentoolbox_api
>>>>>>> origin/main
