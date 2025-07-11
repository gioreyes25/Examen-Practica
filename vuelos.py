vuelos_programados = {
    "LA245": {
        "origen": "Santiago",
        "destino": "Lima",
        "hora_salida": "14:30",
        "hora_llegada_estimada": "17:00",
        "aerolinea": "LATAM",
        "puerta_asignada": "A1",
        "estado": "A Tiempo"
    },
    "AV789": {
        "origen": "Bogota",
        "destino": "Mexico CDMX",
        "hora_salida": "10:00",
        "hora_llegada_estimada": "15:00",
        "aerolinea": "Avianca",
        "puerta_asignada": "B3",
        "estado": "Retrasado"
    },
    "IB901": {
        "origen": "Madrid",
        "destino": "Buenos Aires",
        "hora_salida": "22:00",
        "hora_llegada_estimada": "08:00",
        "aerolinea": "Iberia",
        "puerta_asignada": "C2",
        "estado": "Embarcando"
    },
    "AA123": {
        "origen": "New York",
        "destino": "Miami",
        "hora_salida": "09:00",
        "hora_llegada_estimada": "11:30",
        "aerolinea": "American Airlines",
        "puerta_asignada": "A1", # A1 esta ocupada por LA245, esto es un conflicto a resolver
        "estado": "A Tiempo"
    }
}

puertas_disponibilidad = {
    "A1": {"ocupada_por_vuelo": "LA245", "esta_disponible": False},
    "B3": {"ocupada_por_vuelo": "AV789", "esta_disponible": False},
    "C2": {"ocupada_por_vuelo": "IB901", "esta_disponible": False},
    "D4": {"ocupada_por_vuelo": None, "esta_disponible": True},
    "E5": {"ocupada_por_vuelo": None, "esta_disponible": True}
}

pasajeros_por_vuelo = {
    "LA245": ["PAX001", "PAX002"],
    "AV789": ["PAX003"],
    "IB901": ["PAX004", "PAX005", "PAX006"],
    "AA123": [] # Aun no tiene pasajeros asignados en esta estructura
}

info_pasajeros = {
    "PAX001": ["Juan", "Perez", "12A", "LA245"],
    "PAX002": ["Maria", "Lopez", "12B", "LA245"],
    "PAX003": ["Carlos", "Gomez", "23F", "AV789"],
    "PAX004": ["Ana", "Diaz", "05C", "IB901"],
    "PAX005": ["Luis", "Silva", "06D", "IB901"],
    "PAX006": ["Elena", "Ruiz", "07E", "IB901"]
}
                    