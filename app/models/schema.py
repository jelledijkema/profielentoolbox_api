from pydantic import BaseModel
from pydantic_geojson import LineStringModel

class Dwarsprofiel(BaseModel):
    linestring: LineStringModel  # Valideert een complete LineString (type + coordinates)
    sr: int = 28992  # Spatial Reference ID (SRID) zoals 28992