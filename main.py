from dash import Dash, html, dcc
from dash.dependencies import Input, Output
# from src.components.navbar import create_navbar
from src.pages.simple_page import create_layout, update_station_info
import dash_bootstrap_components as dbc

# Initialisation de l'application avec un thème Bootstrap
app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.CYBORG,
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap"
    ],
    suppress_callback_exceptions=True
)
app.title = "Stations OpenAQ"

# Styles globaux améliorés
CONTENT_STYLE = {
    "margin": "0",
    "padding": "0",
    "minHeight": "100vh",
    "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
    "fontFamily": "'Inter', sans-serif"
}

CARD_STYLE = {
    "margin": "2rem auto",
    "padding": "2.5rem",
    "maxWidth": "1200px",
    "backgroundColor": "rgba(255, 255, 255, 0.95)",
    "borderRadius": "20px",
    "boxShadow": "0 20px 60px rgba(0, 0, 0, 0.3)",
    "backdropFilter": "blur(10px)",
    "border": "1px solid rgba(255, 255, 255, 0.2)"
}

HEADER_STYLE = {
    "textAlign": "center",
    "marginBottom": "2rem",
    "color": "#667eea",
    "fontWeight": "700",
    "fontSize": "2.5rem",
    "textShadow": "2px 2px 4px rgba(0,0,0,0.1)"
}

INPUT_CONTAINER_STYLE = {
    "marginBottom": "2rem",
    "padding": "1.5rem",
    "backgroundColor": "rgba(102, 126, 234, 0.05)",
    "borderRadius": "15px",
    "border": "2px solid rgba(102, 126, 234, 0.2)"
}

RESULT_CONTAINER_STYLE = {
    "marginTop": "2rem",
    "padding": "2rem",
    "backgroundColor": "#f8f9fa",
    "borderRadius": "15px",
    "border": "1px solid #e9ecef",
    "minHeight": "300px",
    "maxHeight": "600px",
    "overflowY": "auto",
    "boxShadow": "inset 0 2px 8px rgba(0,0,0,0.05)"
}

# Layout principal amélioré
app.layout = html.Div(
    style=CONTENT_STYLE,
    children=[
        html.Div(
            style=CARD_STYLE,
            children=[
                html.H1(
                    "🌍 Stations OpenAQ",
                    style=HEADER_STYLE
                ),
                html.Div(
                    style=INPUT_CONTAINER_STYLE,
                    children=[
                        html.Label(
                            "Rechercher une station",
                            style={
                                "fontSize": "1.1rem",
                                "fontWeight": "600",
                                "color": "#495057",
                                "marginBottom": "0.5rem",
                                "display": "block"
                            }
                        ),
                        create_layout()
                    ]
                )
            ]
        )
    ]
)

# Enregistrement du callback pour mettre à jour l'affichage JSON
@app.callback(
    Output('json-display', 'children'),
    Input('station-input', 'value')
)
def update_callback(value):
    return update_station_info(value)


if __name__ == "__main__":
    app.run(debug=True)