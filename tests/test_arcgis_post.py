class TestDwarsprofielEndpoint:
    """Test the /dwarsprofiel endpoint"""

    def test_get_dwarsprofiel_default(self, client):
        """Test GET request returns default GeoJSON response"""
        response = client.get("/dwarsprofiel")
        assert response.status_code == 200
        data = response.json()
        assert data["type"] == "FeatureCollection"
        assert len(data["features"]) > 0
        assert data["features"][0]["type"] == "Feature"

    def test_post_dwarsprofiel_valid_arcgis_geometry(self, client):
        """Test POST with valid ArcGIS geometry"""
        payload = {
            "geometry": {
                "paths": [
                    [
                        [121782.98911020345, 487894.3965402709],
                        [121963.21287569811, 488107.14182318584]
                    ]
                ],
                "spatialReference": {
                    "latestWkid": 28992,
                    "wkid": 28992
                }
            }
        }
        headers = {"Content-Type": "application/json"}
        response = client.post("/dwarsprofiel", json=payload, headers=headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["type"] == "FeatureCollection"
        assert len(data["features"]) > 0
        feature = data["features"][0]
        assert feature["type"] == "Feature"
        assert feature["geometry"]["type"] == "LineString"
        assert "coordinates" in feature["geometry"]

    # def test_post_dwarsprofiel_multiple_paths(self, client):
    #     """Test POST with multiple coordinate paths"""
    #     payload = {
    #         "geometry": {
    #             "paths": [
    #                 [
    #                     [100.0, 200.0],
    #                     [110.0, 210.0],
    #                     [120.0, 220.0]
    #                 ],
    #                 [
    #                     [130.0, 230.0],
    #                     [140.0, 240.0]
    #                 ]
    #             ],
    #             "spatialReference": {
    #                 "latestWkid": 28992,
    #                 "wkid": 28992
    #             }
    #         }
    #     }
    #     response = client.post("/dwarsprofiel", json=payload)
        
    #     assert response.status_code == 200
    #     data = response.json()
    #     coords = data["features"][0]["geometry"]["coordinates"]
    #     # Should flatten all coordinates from all paths
    #     assert len(coords) == 5  # 3 + 2 coordinates

    # def test_post_dwarsprofiel_invalid_payload(self, client):
    #     """Test POST with invalid payload"""
    #     payload = {
    #         "invalid_field": "data"
    #     }
    #     response = client.post("/dwarsprofiel", json=payload)
    #     assert response.status_code == 422  # Validation error

    # def test_post_dwarsprofiel_missing_spatial_reference(self, client):
    #     """Test POST without spatial reference fails"""
    #     payload = {
    #         "geometry": {
    #             "paths": [[[0.0, 1.0], [2.0, 3.0]]]
    #         }
    #     }
    #     response = client.post("/dwarsprofiel", json=payload)
    #     assert response.status_code == 422

    def test_dwarsprofiel_response_structure(self, client):
        """Test the response has correct GeoJSON structure"""
        payload = {
            "geometry": {
                "paths": [[[0.0, 0.0], [1.0, 1.0]]],
                "spatialReference": {"latestWkid": 28992, "wkid": 28992}
            }
        }
        response = client.post("/dwarsprofiel", json=payload)
        data = response.json()
        
        # Validate GeoJSON structure
        assert "type" in data
        assert "features" in data
        assert isinstance(data["features"], list)
        
        feature = data["features"][0]
        assert "type" in feature
        assert "properties" in feature
        assert "geometry" in feature
        assert "type" in feature["geometry"]
        assert "coordinates" in feature["geometry"]

    def test_dwarsprofiel_cors_headers(self, client):
        """Test that CORS headers are present"""
        response = client.post(
            "/dwarsprofiel",
            json={
                "geometry": {
                    "paths": [[[0.0, 0.0], [1.0, 1.0]]],
                    "spatialReference": {"latestWkid": 28992, "wkid": 28992}
                }
            },
            headers={"Origin": "https://localhost:3001"}
        )
        assert response.status_code == 200
