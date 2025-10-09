import os
import requests
import pandas as pd
from dotenv import load_dotenv
from dash import Dash, html, dcc, dash_table

# Charger les variables d'environnement
load_dotenv()

# --- 1. Appel API ---
station_id = 2005
url = f"https://api.openaq.org/v3/locations/{station_id}"
headers = {"X-API-Key": os.getenv("API_KEY")}

response = requests.get(url, headers=headers)
data = response.json()

# --- 2. Préparer les données ---
location = data.get("results", [{}])[0]  
df_parameters = pd.DataFrame(location.get("parameters", []))  

# --- 3. Créer l’app Dash ---
app = Dash(__name__)
app.title = f"Station OpenAQ #{station_id}"

app.layout = html.Div([
    html.H1(f"Données de la station #{station_id}", style={'textAlign': 'center'}),
    
    html.H3("Informations générales"),
    html.Ul([
        html.Li(f"Nom : {location.get('name', 'N/A')}"),
        html.Li(f"Pays : {location.get('country', 'N/A')}"),
        html.Li(f"Ville : {location.get('city', 'N/A')}"),
        html.Li(f"Coordonnées : {location.get('coordinates', {})}")
    ]),

])

# --- 4. Lancer l’app ---
if __name__ == "__main__":
    app.run(debug=True)
