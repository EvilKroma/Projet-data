# Importation des dépendances
from dash import html
from src.pages.simple_page import create_layout, update_station_info
from dash.dependencies import Input, Output

# Layout page accueil
def layout():
    return html.Div(
        children=[
            html.H1("🌍 Stations OpenAQ"),
            html.Div(
                children=[
                    create_layout()
                ]
            )
        ]
    )

# Fonction pour enregister le json en fonction de l'id
def register_callbacks(app):
    @app.callback(
        Output('json-display', 'children'),
        Input('station-input', 'value')
    )
    def update_callback(value):
        return update_station_info(value)