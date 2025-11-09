#Importztion des dépendances / pages 
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from src.components.navbar import create_navbar
from src.pages import home, histogramme
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.CYBORG,
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap"
    ],
    suppress_callback_exceptions=True
)
app.title = "Stations OpenAQ"

#Style css de base 


#Layout de la page
app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        create_navbar(),
        html.Div(id='page-content', style={'padding': '20px'})
    ]
)

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/histogramme':
        return histogramme.layout()
    else:
        return home.layout()

home.register_callbacks(app)
histogramme.register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
