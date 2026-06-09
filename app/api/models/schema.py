from pydantic import BaseModel
from pydantic_geojson import LineStringModel

class Dwarsprofiel(BaseModel):
    linestring: LineStringModel  # Valideert een complete LineString (type + coordinates)