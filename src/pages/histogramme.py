#Page dédiée à l'affichage de l'histogramme

import plotly.express as px
import pandas as pd

# Récupération des données
def get_data_by_city_id(city_id):
    data = [
        {"polluant": "NO2", "valeur": 45, "date": "2023-01-01"},
       {"polluant": "PM10", "valeur": 30, "date": "2023-01-01"},
        {"polluant": "C03", "valeur": 10, "date": "2023-01-01"}
    ]
    return data

# JSON vers DataFrame
def data_to_dataframe(json_data): 
    return pd.DataFrame(json_data)

# Histogramme interactif
def afficher_histogramme(city_id):
    json_data = get_data_by_city_id(city_id)
    df = data_to_dataframe(json_data)
    
    fig = px.histogram(df, x="polluant", y="valeur", color="polluant", barmode="group")
    fig.update_layout(title=f"Pollution pour la ville ID {city_id}")
    fig.show()

# Point d'entrée du script
if __name__ == "__main__":
    afficher_histogramme(city_id=1)
