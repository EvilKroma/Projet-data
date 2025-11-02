import json
import os
import requests
from datetime import datetime
from config import API_BASE_URL, API_KEY, RAW_DATA_DIR

# Récupération des données via l'API OpenAQ
def fetch_station_data(station_id):
    try:
        print(f"Fetching data for station ID: {station_id}")
        response = requests.get(
            f"{API_BASE_URL}/locations/{station_id}",
            headers={"X-API-Key": API_KEY}
        )
        response.raise_for_status()
        return response.json().get("results", [{}])[0]
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des données : {e}")
        return None
    
# Sauvegarde les données dans un fichier JSON
def save_data_to_json(data, filename=None):
    if not data:
        return False, None
    
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"station_data_{timestamp}.json"

    filepath = os.path.join(RAW_DATA_DIR, filename)
    
    try:
        # Créer le dossier s'il n'existe pas
        os.makedirs(RAW_DATA_DIR, exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2, ensure_ascii=False)
        print(f"Données sauvegardées dans : {filepath}")
        return True, filepath
    except Exception as e:
        print(f"Erreur lors de la sauvegarde JSON : {e}")
        return False, None

# Fonction principale pour récupérer et sauvegarder
def fetch_and_save_station_data(station_id):
    """Récupère les données de l'API et les sauvegarde en JSON"""
    data = fetch_station_data(station_id)
    if data:
        success, filepath = save_data_to_json(data)
        return data, filepath if success else None
    return None, None