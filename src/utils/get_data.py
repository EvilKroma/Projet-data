import json
import os
import requests
from datetime import datetime
from config import API_BASE_URL, API_KEY, RAW_DATA_DIR

# Récupération des données de station via l'API
def fetch_station_data(station_id):
    try:
        response = requests.get(
            f"{API_BASE_URL}/locations/{station_id}",
            headers={"X-API-Key": API_KEY}
        )
        response.raise_for_status()
        return response.json().get("results", [{}])[0]
    except requests.exceptions.RequestException as e:
        print(f"Erreur API station: {e}")
        return None

# Sauvegarde des données en JSON
def save_data_to_json(data, filename=None):
    if not data:
        return False, None
    
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"station_data_{timestamp}.json"

    filepath = os.path.join(RAW_DATA_DIR, filename)
    
    try:
        os.makedirs(RAW_DATA_DIR, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2, ensure_ascii=False)
        return True, filepath
    except Exception as e:
        print(f"Erreur sauvegarde: {e}")
        return False, None

# Récupération et sauvegarde combinées
def fetch_and_save_station_data(station_id):
    data = fetch_station_data(station_id)
    if data:
        success, filepath = save_data_to_json(data)
        return data, filepath if success else None
    return None, None

# Chargement des données depuis JSON
def load_station_json(station_id):
    filename = f"{station_id}.json"
    filepath = os.path.join(RAW_DATA_DIR, filename)
    
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as jsonfile:
                return json.load(jsonfile)
        except Exception as e:
            print(f"Erreur lecture {filepath}: {e}")
    
    # Recherche dans tous les fichiers JSON
    try:
        files = [f for f in os.listdir(RAW_DATA_DIR) if f.endswith('.json')]
        for filename in files:
            filepath = os.path.join(RAW_DATA_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as jsonfile:
                    data = json.load(jsonfile)
                    if data.get('id') == station_id:
                        return data
            except Exception:
                continue
    except Exception as e:
        print(f"Erreur recherche JSON: {e}")
    
    return None

# Récupération des mesures de pollution
def fetch_measurements(station_id, limit=1000, date_from=None):
    if not date_from:
        date_from = "2023-01-01T00:00:00Z"
    
    params = {"limit": limit, "date_from": date_from}
    
    # Requetes GET 
    endpoints = [
        (params, f"{API_BASE_URL}/locations/{station_id}/measurements")
    ]
    
    for endpoint_params, url in endpoints:
        try:
            full_params = params.copy()
            full_params.update(endpoint_params)
            response = requests.get(url, params=full_params, headers={"X-API-Key": API_KEY})
            response.raise_for_status()
            results = response.json().get("results", [])
            if results:
                return results
        except requests.exceptions.RequestException:
            continue
    
    # Fallback pour une mesure récente meme si mon code échoue
    try:
        response = requests.get(
            f"{API_BASE_URL}/locations/{station_id}/latest",
            headers={"X-API-Key": API_KEY}
        )
        response.raise_for_status()
        results = response.json().get("results", [])
        
        if results:
            measurements = []
            for result in results:
                measurements.append({
                    "parameter": {"name": "unknown", "displayName": "Inconnu"},
                    "value": result.get("value"),
                    "date": result.get("datetime", {})
                })
            return measurements
    except requests.exceptions.RequestException:
        pass
    
    print(f"Aucune mesure trouvée pour la station {station_id}")
    return []