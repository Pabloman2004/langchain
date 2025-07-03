import requests
from datetime import datetime
import locale

# Configurar idioma si es posible
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, 'C')  # inglés si falla

def obtener_coordenadas(ciudad: str):
    url = f"https://nominatim.openstreetmap.org/search?q={ciudad}&format=json"
    response = requests.get(url, headers={"User-Agent": "TuAgente/1.0"})
    data = response.json()

    if not data:
        return None, None

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon

def obtener_tiempo_actual(ciudad: str):
    lat, lon = obtener_coordenadas(ciudad)
    if lat is None:
        return f"No pude encontrar la ciudad '{ciudad}'."

    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "current_weather" not in data:
        return f"No pude obtener el tiempo en {ciudad}."

    weather = data["current_weather"]
    temp = weather["temperature"]
    wind = weather["windspeed"]

    # Parsear la hora que da la API
    hora_api = datetime.strptime(weather["time"], "%Y-%m-%dT%H:%M")
    fecha_formateada = hora_api.strftime("%A, %d de %B de %Y, %H:%M").capitalize()

    return (
        f"En {ciudad.title()} hay {temp}°C y viento de {wind} km/h.\n"
        f"Datos obtenidos el {fecha_formateada} UTC."
    )


