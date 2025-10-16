from dash import Dash, html
from src.components.navbar import create_navbar
from src.pages.simple_page import create_layout, update_station_info

# Initialisation de l'application
app = Dash(__name__)
app.title = "Stations OpenAQ"

# Layout principal
app.layout = html.Div([
    create_navbar(),
    create_layout()
])

# Enregistrement du callback
app.callback(update_station_info)

if __name__ == "__main__":
    app.run(debug=True)