import dash_bootstrap_components as dbc
from dash import html

def create_navbar():
    navbar = dbc.Navbar(
        dbc.Container([
            # Brand
            dbc.NavbarBrand("OpenAQ Stations", href="/", className="ms-2 fw-bold"),
            
            # Navigation links
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("Accueil", href="/", id="nav-home")),
                dbc.NavItem(dbc.NavLink("Histogrammes", href="/histogramme", id="nav-histogram")),
            ], className="ms-auto", navbar=True),
        ], fluid=True),
        color="primary",
        dark=True,
        sticky="top",
        className="shadow-sm"
    )
    return navbar