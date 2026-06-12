
default_geoJSON = {
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
        "druk_bar": None,
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



default_geoJSON_2 = {
  "type": "FeatureCollection",
  "spatialReference": { "wkid": 28992 },
  "layers": [
    {
      "id": "bodemtype",
      "label": "Bodemtypen",
      "geometryType": "polygon",
      "fields": [
        { "name": "grondsoort",        "alias": "Grondsoort",             "type": "string"  },
        { "name": "nen_klasse",        "alias": "NEN-klasse",             "type": "string"  },
        { "name": "diepte_mv_m",       "alias": "Diepte (m-mv)",          "type": "double"  },
        { "name": "dikte_m",           "alias": "Dikte (m)",              "type": "double"  },
        { "name": "kleur",             "alias": "Kleur",                  "type": "string"  },
        { "name": "organisch_stof_pct","alias": "Organisch stof (%)",     "type": "double"  }
      ],
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
      "fields": [
        { "name": "type",         "alias": "Type",             "type": "string"  },
        { "name": "beheerder",    "alias": "Beheerder",        "type": "string"  },
        { "name": "diameter_mm",  "alias": "Diameter (mm)",    "type": "integer" },
        { "name": "materiaal",    "alias": "Materiaal",        "type": "string"  },
        { "name": "aanlegjaar",   "alias": "Aanlegjaar",       "type": "integer" },
        { "name": "druk_bar",     "alias": "Druk (bar)",       "type": "double"  },
        { "name": "diepte_mv_m",  "alias": "Diepte (m-mv)",   "type": "double"  }
      ],
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
      "fields": [
        { "name": "code",                 "alias": "Code",                   "type": "string" },
        { "name": "omschrijving",         "alias": "Omschrijving",           "type": "string" },
        { "name": "filterdiepte_m",       "alias": "Filterdiepte (m)",       "type": "double" },
        { "name": "grondwaterstand_m_mv", "alias": "Grondwaterstand (m-mv)", "type": "double" },
        { "name": "meetdatum",            "alias": "Meetdatum",              "type": "date"   },
        { "name": "kwaliteit",            "alias": "Kwaliteit",              "type": "string" }
      ],
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
        "druk_bar": None,
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
