import os
import requests
import pandas as pd
from dotenv import load_dotenv
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output

load_dotenv()
app = Dash(__name__)
app.title = "Stations OpenAQ"

# Layout principal
app.layout = html.Div([
    html.H1("Données des stations OpenAQ", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Entrez l'ID de la station :"),
        dcc.Input(
            id='station-input',
            type='number',
            value=2005,
            min=1,
            debounce=True
        )
    ], style={'textAlign': 'center', 'marginBottom': '20px'}),
    html.Div(id='station-info'),
    dash_table.DataTable(
        id='parameters-table',
        columns=[],
        data=[],
        style_cell={'textAlign': 'left', 'whiteSpace': 'normal'},
        style_header={'fontWeight': 'bold'},
        page_size=10
    )
])

def fetch_station_data(station_id):
    try:
        response = requests.get(
            f"https://api.openaq.org/v3/locations/{station_id}",
            headers={"X-API-Key": os.getenv("API_KEY")}
        )
        response.raise_for_status()
        return response.json().get("results", [{}])[0]
    except requests.exceptions.RequestException:
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

    def format_value(key, value):
        if key == 'sensors' and isinstance(value, list):
            return "\n".join(
                " | ".join(f"{k}: {v}" for k, v in sensor.items() 
                if k in ['id', 'name', 'parameter', 'manufacturer', 'modelName'])
                for sensor in value
            )
        elif isinstance(value, (dict, list)):
            return str(value)
        return str(value)

    # Données de la station
    selected_fields = ['id', 'name', 'locality', 'country', 'sensors', 'coordinates', 
                      'datetimeFirst', 'datetimeLast']
    station_info = {
        key: format_value(key, location.get(key, 'N/A'))
        for key in selected_fields
        if key in location
    }
    
    # Création du tableau d'information
    info_df = pd.DataFrame([station_info]).transpose()
    info_df.columns = ['Valeur']
    info_df.index.name = 'Propriété'
    info_table = dash_table.DataTable(
        data=info_df.reset_index().to_dict('records'),
        columns=[
            {"name": "Propriété", "id": "Propriété"},
            {"name": "Valeur", "id": "Valeur", "presentation": "markdown"}
        ],
        style_cell={'textAlign': 'left', 'whiteSpace': 'normal'},
        style_header={'fontWeight': 'bold'},
        page_size=20
    )

    # Préparation du tableau des paramètres
    df_parameters = pd.DataFrame(location.get("parameters", []))
    if df_parameters.empty:
        return info_table, [], []

    param_columns = [{"name": col.capitalize(), "id": col} for col in df_parameters.columns]
    return info_table, param_columns, df_parameters.to_dict('records')

# --- 4. Lancer l’app ---
if __name__ == "__main__":
    app.run(debug=True)
