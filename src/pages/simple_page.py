"""
Page d'accueil simple affichant les informations d'une station
"""
from dash import html, dcc, dash_table
import pandas as pd
from src.utils.get_data import fetch_station_data
from config import DEFAULT_STATION_ID

def create_station_form():
    return html.Div([
        html.Label("Entrez l'ID de la station :"),
        dcc.Input(
            id='station-input',
            type='number',
            value=DEFAULT_STATION_ID,
            min=1,
            debounce=True
        )
    ], style={'textAlign': 'center', 'marginBottom': '20px'})

def create_data_tables():
    return html.Div([
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

def create_layout():
    return html.Div([
        create_station_form(),
        create_data_tables()
    ])

# Les outputs et inputs seront définis dans le callback principal
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