import os
import requests
import pandas as pd
from dotenv import load_dotenv
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output

# Charger les variables d'environnement
load_dotenv()

# --- 1. Créer l'app Dash ---
app = Dash(__name__)
app.title = "Stations OpenAQ"

# --- 2. Layout de l'app ---
app.layout = html.Div([
    html.H1("Données des stations OpenAQ", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("Entrez l'ID de la station :"),
        dcc.Input(id='station-input', type='number', value=2005, min=1),
        html.Button('Valider', id='submit-btn', n_clicks=0)
    ], style={'textAlign': 'center', 'marginBottom': '20px'}),
    
    html.Div(id='station-info'),
    html.H3("Paramètres mesurés"),
    dash_table.DataTable(id='parameters-table', columns=[], data=[])
])

# --- 3. Callback pour mettre à jour les données ---
@app.callback(
    [Output('station-info', 'children'),
     Output('parameters-table', 'columns'),
     Output('parameters-table', 'data')],
    Input('submit-btn', 'n_clicks'),
    Input('station-input', 'value')
)
def update_station_info(n_clicks, station_id):
    if not station_id:
        return "Aucune station sélectionnée.", [], []
    
    url = f"https://api.openaq.org/v3/locations/{station_id}"
    headers = {"X-API-Key": os.getenv("API_KEY")}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return f"Erreur API : {response.status_code}", [], []
    
    data = response.json()
    location = data.get("results", [{}])[0]
    
    # Infos générales
    info_children = html.Ul([
        html.Li(f"Nom : {location.get('name', 'N/A')}"),
        html.Li(f"Pays : {location.get('country', 'N/A')}"),
        html.Li(f"Ville : {location.get('city', 'N/A')}"),
        html.Li(f"Coordonnées : {location.get('coordinates', {})}")
    ])
    
    # Paramètres
    df_parameters = pd.DataFrame(location.get("parameters", []))
    if df_parameters.empty:
        return info_children, [], []
    
    columns = [{"name": col, "id": col} for col in df_parameters.columns]
    data_table = df_parameters.to_dict('records')
    
    return info_children, columns, data_table

# --- 4. Lancer l’app ---
if __name__ == "__main__":
    app.run(debug=True)
