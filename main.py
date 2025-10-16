import os
import requests
import pandas as pd
from dotenv import load_dotenv
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output

# Configuration
load_dotenv()
API_BASE_URL = "https://api.openaq.org/v3"
DEFAULT_STATION_ID = 2005

# Styles
CENTERED_STYLE = {'textAlign': 'center'}
CONTAINER_STYLE = {**CENTERED_STYLE, 'marginBottom': '20px'}

# Application
app = Dash(__name__)
app.title = "Stations OpenAQ"

def create_station_form():
    return html.Div([
        html.Label("Entrez l'ID de la station :"),
        dcc.Input(
            id='station-input',
            type='number',
            value=DEFAULT_STATION_ID,
            min=1,
            debounce=True  # Attend que l'utilisateur finisse de taper
        )
    ], style=CONTAINER_STYLE)

app.layout = html.Div([
    html.H1("Données des stations OpenAQ", style=CENTERED_STYLE),
    create_station_form(),
    html.Div(id='station-info'),
    html.H3("Paramètres mesurés"),
    dash_table.DataTable(id='parameters-table', columns=[], data=[])
])

def fetch_station_data(station_id):
    try:
        response = requests.get(
            f"{API_BASE_URL}/locations/{station_id}",
            headers={"X-API-Key": os.getenv("API_KEY")}
        )
        response.raise_for_status()
        return response.json().get("results", [{}])[0]
    except requests.exceptions.RequestException as e:
        return None

@app.callback(
    [Output('station-info', 'children'),
     Output('parameters-table', 'columns'),
     Output('parameters-table', 'data')],
    Input('station-input', 'value')
)
def update_station_info(station_id):
    if not station_id:
        return "Veuillez entrer un ID de station.", [], []

    location = fetch_station_data(station_id)
    if not location:
        return "Erreur: Impossible de récupérer les données de la station.", [], []

    info_children = html.Ul([
        html.Li(f"{key.capitalize()} : {location.get(key, 'N/A')}")
        for key in ['name', 'country', 'city', 'coordinates']
    ])

    df_parameters = pd.DataFrame(location.get("parameters", []))
    if df_parameters.empty:
        return info_children, [], []

    columns = [{"name": col, "id": col} for col in df_parameters.columns]
    return info_children, columns, df_parameters.to_dict('records')

# --- 4. Lancer l’app ---
if __name__ == "__main__":
    app.run(debug=True)
