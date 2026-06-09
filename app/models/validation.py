# from pydantic_geojson import LineString
# from pyproj import Transformer
# import math

def validate_is_linestring(geometry: dict) -> bool:
    """Controleer of de geometry een LineString is."""
    return geometry.get("type") == "LineString"

# def calculate_length(coordinates: List[List[float]], srid: int = 28992) -> float:
#     """
#     Bereken de lengte van een LineString in meters (RD New = EPSG:28992).
#     Gebruikt PyProj voor nauwkeurige afstandsberekening.
#     """
#     if srid != 28992:
#         raise ValueError("Alleen SRID 28992 (RD New) wordt ondersteund")

#     transformer = Transformer.from_crs("EPSG:28992", "EPSG:28992", always_xy=True)
#     total_length = 0.0
#     for i in range(len(coordinates) - 1):
#         x1, y1 = coordinates[i]
#         x2, y2 = coordinates[i + 1]
#         # Bereken Euclidean afstand (voor RD New is dit voldoende voor korte afstanden)
#         distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#         total_length += distance
#     return total_length

# def validate_line_length(coordinates: List[List[float]], max_length: float = 1000.0) -> bool:
#     """Controleer of de lijn korter is dan `max_length` meters."""
#     length = calculate_length(coordinates)
#     if length > max_length:
#         raise ValueError(f"Lijn is te lang: {length:.2f}m (max: {max_length}m)")
#     return True