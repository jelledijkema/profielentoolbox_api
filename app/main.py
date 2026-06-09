"""Main application entry point for Profielentool API"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.models.validation import validate_is_linestring

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
  "spatialReference": { "wkid": 28992 },
  "layers": [
    {
      "id": "bodemtype",
      "label": "Bodemtypen",
      "geometryType": "polygon",
      "style": {
        "color": "#8B4513",
        "fillOpacity": 0.35,
        "outlineWidth": 1.0
      },
      "labelField": "grondsoort"
    },
    {
      "id": "leiding",
      "label": "Kabels en leidingen",
      "geometryType": "line",
      "style": {
        "color": "#ff9900",
        "width": 3,
        "opacity": 1.0
      },
      "labelField": "type"
    },
    {
      "id": "peilbuis",
      "label": "Peilbuizen",
      "geometryType": "point",
      "style": {
        "color": "#00a8e0",
        "size": 10,
        "outlineColor": "#ffffff",
        "outlineWidth": 1.5
      },
      "labelField": "code"
    }
  ],
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [135800, 455800],
            [135980, 455800],
            [135980, 455700],
            [135800, 455700],
            [135800, 455800]
          ]
        ]
      },
      "properties": {
        "layer": "bodemtype",
        "grondsoort": "Fijn zand",
        "nen_klasse": "Zs1",
        "diepte_mv_m": 0.5,
        "dikte_m": 3.2,
        "kleur": "Grijsgeel",
        "organisch_stof_pct": 0.4
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [135980, 455800],
            [136150, 455800],
            [136150, 455700],
            [135980, 455700],
            [135980, 455800]
          ]
        ]
      },
      "properties": {
        "layer": "bodemtype",
        "grondsoort": "Klei",
        "nen_klasse": "K",
        "diepte_mv_m": 0.3,
        "dikte_m": 1.8,
        "kleur": "Donkergrijs",
        "organisch_stof_pct": 3.1
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [135800, 455700],
            [136150, 455700],
            [136150, 455620],
            [135800, 455620],
            [135800, 455700]
          ]
        ]
      },
      "properties": {
        "layer": "bodemtype",
        "grondsoort": "Veen",
        "nen_klasse": "V",
        "diepte_mv_m": 2.1,
        "dikte_m": 4.5,
        "kleur": "Zwartbruin",
        "organisch_stof_pct": 28.7
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [135820, 455780],
          [135900, 455760],
          [136050, 455750],
          [136130, 455740]
        ]
      },
      "properties": {
        "layer": "leiding",
        "type": "Waterleiding",
        "beheerder": "Vitens",
        "diameter_mm": 150,
        "materiaal": "PVC",
        "aanlegjaar": 1987,
        "druk_bar": 6.5,
        "diepte_mv_m": 1.2
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "LineString",
        "coordinates": [
          [135830, 455730],
          [135950, 455720],
          [136080, 455710]
        ]
      },
      "properties": {
        "layer": "leiding",
        "type": "Riool (vrijverval)",
        "beheerder": "Gemeente",
        "diameter_mm": 400,
        "materiaal": "Beton",
        "aanlegjaar": 1972,
        "druk_bar": null,
        "diepte_mv_m": 2.4
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [135870, 455760]
      },
      "properties": {
        "layer": "peilbuis",
        "code": "PB-01",
        "omschrijving": "Peilbuis westelijk deel",
        "filterdiepte_m": 4.5,
        "grondwaterstand_m_mv": 1.35,
        "meetdatum": "2026-05-28",
        "kwaliteit": "Goed"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [136020, 455740]
      },
      "properties": {
        "layer": "peilbuis",
        "code": "PB-02",
        "omschrijving": "Peilbuis centrale zone",
        "filterdiepte_m": 6.0,
        "grondwaterstand_m_mv": 0.98,
        "meetdatum": "2026-05-28",
        "kwaliteit": "Matig"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [136110, 455750]
      },
      "properties": {
        "layer": "peilbuis",
        "code": "PB-03",
        "omschrijving": "Peilbuis oostelijk deel",
        "filterdiepte_m": 3.8,
        "grondwaterstand_m_mv": 1.62,
        "meetdatum": "2026-05-28",
        "kwaliteit": "Goed"
      }
    }
  ]
}

@app.api_route("/dwarsprofiel/validate", methods=["GET", "POST"])
async def validate_dwarsprofiel(request: Request):
    data = await request.json()

    # Valideer of 'geometry' bestaat
    if "geometry" not in data:
        raise HTTPException(status_code=400, detail="Ontbrekend veld: geometry")

    if validate_is_linestring(data["geometry"]) == False:
        raise HTTPException(status_code=400, detail="Ongeldige geometry: moet een LineString zijn")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
    )
