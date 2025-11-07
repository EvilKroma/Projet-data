#Page dédiée à l'affichage de l'histogramme
# Importation de plotly
import plotly.express as px
import pandas as pd

# Récupération des données
def get_data_by_city_id(city_id):
    data = [
        {"polluant": "NO2", "valeur": 45, "date": "2023-01-01"},
        {"polluant": "PM10", "valeur": 30, "date": "2023-01-01"},
        {"polluant": "C03", "valeur": 10, "date": "2023-01-01"},
        {"polluant": "NO2", "valeur": 50, "date": "2023-02-01"},
        {"polluant": "PM10", "valeur": 35, "date": "2023-02-01"},
        {"polluant": "C03", "valeur": 12, "date": "2023-02-01"},
        {"polluant": "NO2", "valeur": 40, "date": "2023-03-01"},
        {"polluant": "PM10", "valeur": 28, "date": "2023-03-01"},
        {"polluant": "C03", "valeur": 9, "date": "2023-03-01"}
    ]
    return data

# JSON vers DataFrame
def data_to_dataframe(json_data): 
    df = pd.DataFrame(json_data)
    df["date"] = pd.to_datetime(df["date"])
    df["mois"] = df["date"].dt.strftime("%B")  # Mois en toutes lettres
    return df

# Histogrammes séparés par polluant
def afficher_histogrammes_par_polluant(city_id):
    json_data = get_data_by_city_id(city_id)
    df = data_to_dataframe(json_data)
    
    polluants = df["polluant"].unique()
    
    for polluant in polluants:
        df_polluant = df[df["polluant"] == polluant]
        fig = px.histogram(
            df_polluant,
            x="mois",
            y="valeur",
            title=f"Évolution mensuelle de {polluant} - Ville ID {city_id}",
            color_discrete_sequence=["#636EFA"]  # Couleur personnalisée
        )
        fig.update_layout(xaxis_title="Mois", yaxis_title="Valeur")
        fig.show()
