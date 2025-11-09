#Page d'accueil pour afficher le Json via API
from dash import html, dcc
import json
from src.utils.get_data import fetch_and_save_station_data

#Recherche station par ID
def create_station_form():
    return html.Div([
        html.Label("Entrez l'ID de la station :"),
        dcc.Input(
            id='station-input',
            type='number',
            placeholder="Ex: 2005",
            min=1,
            debounce=True,
        )
    ], style={'textAlign': 'center', 'marginBottom': '20px'})

# Affichage du JSON
def create_json_display():
    return html.Div([
        html.Div(id='json-display')
    ])

#Layout pour la mise en page
def create_layout():
    return html.Div([
        create_station_form(),
        create_json_display()
    ])

# Utilisation API Open pour récupérer les données en JSON
def update_station_info(station_id):
    if not station_id:
        return html.Div("Veuillez entrer un ID de station.", style={'textAlign': 'center', 'margin': '20px'})

    data, filepath = fetch_and_save_station_data(station_id)
    
    if not data:
        return html.Div("Erreur: Impossible de récupérer les données de la station.", style={'textAlign': 'center', 'margin': '20px', 'color': 'red'})
    
    # Affichage des données JSON
    json_content = json.dumps(data, indent=2, ensure_ascii=False)
    
    return html.Div([
        html.H3(f"Données de la station {station_id}", style={'textAlign': 'center'}),
        html.P(f"Fichier sauvegardé dans ./data/raw/ ", style={'textAlign': 'center', 'fontStyle': 'italic'}),  # Je sauvegarde les données pour les utiliser dans l'histogramme
        html.Pre(json_content, style={
            'backgroundColor': '#f5f5f5',
            'padding': '20px',
            'border': '1px solid #ddd',
            'borderRadius': '5px',
            'overflow': 'auto',
            'maxHeight': '500px'
        })
    ])