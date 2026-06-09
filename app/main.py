"""Main application entry point for Profielentool API"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API for Profielentool",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Profielentool API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.api_route("/health", methods=["GET", "POST"]) # Health check endpoint that accepts both GET and POST requests
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.api_route("/dwarsprofiel", methods=["GET", "POST"])
async def get_dwarsprofiel():
    """Geeft een standaard GeoJSON-dwarsprofiel terug."""
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "name": "Standaard dwarsprofiel",
                    "description": "Voorbeeld GeoJSON voor een dwarsprofiel"
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [4.895167, 52.370216],
                        [4.895300, 52.370500],
                        [4.895450, 52.370800]
                    ]
                }
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
    )
