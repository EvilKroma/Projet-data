from dash import Dash, html
from dash.dependencies import Input, Output
# from src.components.navbar import create_navbar
from src.pages.simple_page import create_layout, update_station_info

# Initialisation de l'application
app = Dash(__name__)
app.title = "Stations OpenAQ"

# Layout principal
app.layout = html.Div([
    # create_navbar(),
    create_layout()
])

# Enregistrement du callback pour mettre à jour l'affichage JSON
@app.callback(
    Output('json-display', 'children'),
    Input('station-input', 'value')
)
def update_callback(value):
    return update_station_info(value)

if __name__ == "__main__":
    app.run(debug=True)