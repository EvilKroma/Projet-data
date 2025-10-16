"""
Navigation component
"""
from dash import html

def create_navbar():
    return html.Nav([
        html.Div([
            html.H1("Données des stations OpenAQ", className='nav-title')
        ], className='navbar')
    ])