import plotly.express as px
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output
from src.utils.get_data import load_station_json, fetch_measurements

# Récupération des données via id_station entré par le uer
def get_data_by_station_id(station_id):
    station_data = load_station_json(station_id)
    if not station_data:
        return []
    
    measurements = fetch_measurements(station_id)
    if not measurements:
        return []
    
    data = []
    for measure in measurements:
        parameter = measure.get('parameter', {})
        param_name = parameter.get('displayName') or parameter.get('name', 'Unknown') if isinstance(parameter, dict) else str(parameter)
        
        date_obj = measure.get('date', {})
        date = date_obj.get('utc') or date_obj.get('local', '') if isinstance(date_obj, dict) else str(date_obj)
        
        value = measure.get('value')
        if param_name != 'Unknown' and date and value is not None:
            try:
                data.append({"polluant": param_name, "valeur": float(value), "date": date})
            except (ValueError, TypeError):
                continue
    
    return data

#je transforme le Json en dataframe pour traiter les données
def data_to_dataframe(json_data):
    if not json_data:
        return pd.DataFrame()
    
    df = pd.DataFrame(json_data)
    if 'date' in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors='coerce')
        df = df.dropna(subset=['date'])
        df["mois"] = df["date"].dt.strftime("%B")
        df = df.sort_values('date')
    
    return df

# Layout
def layout():
    return html.Div(
        children=[
            html.H1("Page Histogramme"),
            html.Div(
                children=[
                    html.Label("Id Station :"),
                    dcc.Input(
                        id='station-id-input', type='number', placeholder="Ex: 2005",
                        min=1, value=2005, debounce=True
                    )
                ]
            ),
            html.Div(id='histogram-container')
        ]
    )

# Création des histogrammes
def create_histogram_figures(station_id):
    json_data = get_data_by_station_id(station_id)
    if not json_data:
        return []
    
    df = data_to_dataframe(json_data)
    if df.empty:
        return []
    
    figures = []
    has_multiple_dates = len(df["date"].unique()) > 1
    
    for polluant in df["polluant"].unique():
        df_polluant = df[df["polluant"] == polluant]
        if df_polluant.empty:
            continue
        
        if has_multiple_dates:
            fig = px.histogram(df_polluant, x="mois", y="valeur", 
                             title=f"Évolution mensuelle de {polluant} - Station {station_id}",
                             color_discrete_sequence=["#636EFA"])
        else:
            fig = px.bar(df_polluant, x="polluant", y="valeur", 
                        title=f"Dernière mesure de {polluant} - Station {station_id}",
                        color_discrete_sequence=["#0112FF"], text="valeur")    #Couleur des barres histogramme
            fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')
        
        fig.update_layout(
            xaxis_title="Mois" if has_multiple_dates else "Polluant",
            yaxis_title="Valeur",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False
        )
        figures.append(fig)
    
    return figures

# Callbacks
def register_callbacks(app):
    @app.callback(
        Output('histogram-container', 'children'),
        Input('station-id-input', 'value')
    )
    def update_histograms(station_id):
        if not station_id:
            return html.Div("Veuillez entrer un ID de station.")
        
        figures = create_histogram_figures(station_id)
        
        if not figures:
            return html.Div([
                html.Div(f"Impossible de récupérer les mesures pour la station {station_id}.")
            ])
        
        return html.Div([dcc.Graph(figure=fig, style={'marginBottom': '30px'}) for fig in figures])