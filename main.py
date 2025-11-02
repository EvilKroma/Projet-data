from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from src.components.navbar import create_navbar
from src.pages.simple_page import create_layout, update_station_info
import dash_bootstrap_components as dbc

# Initialisation de l'application avec un thème Bootstrap
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],  # Essaie aussi LUX, FLATLY, YETI, etc.
    suppress_callback_exceptions=True
)
app.title = "Stations OpenAQ"

# Style global
CONTENT_STYLE = {
    "margin": "2rem",
    "padding": "2rem",
    "backgroundColor": "rgba(255,255,255,0.05)",
    "borderRadius": "15px",
    "boxShadow": "0 4px 12px rgba(0,0,0,0.3)"
}

# Layout principal
app.layout = html.Div([
    create_navbar(),  # Barre de navigation (supposée bien faite)
    html.Div([
        html.H2("Tableau de bord des stations OpenAQ 🌍",
                className="text-center text-info mb-4"),
        create_layout()  # Contenu principal de la page
    ], style=CONTENT_STYLE)
])


# Enregistrement du callback pour mettre à jour le tableau
@app.callback(
    [Output('station-info', 'children'),
     Output('parameters-table', 'columns'),
     Output('parameters-table', 'data')],
    Input('station-input', 'value')
)
def update_callback(value):
    return update_station_info(value)


if __name__ == "__main__":
    app.run(debug=True)
