"""
Fonctions de récupération des données de l'API OpenAQ
"""

import requests
from config import API_BASE_URL, API_KEY

def fetch_station_data(station_id):
    """Récupère les données d'une station spécifique"""
    try:
        response = requests.get(
            f"{API_BASE_URL}/locations/{station_id}",
            headers={"X-API-Key": API_KEY}
        )
        response.raise_for_status()
        return response.json().get("results", [{}])[0]
    except requests.exceptions.RequestException:
        return None