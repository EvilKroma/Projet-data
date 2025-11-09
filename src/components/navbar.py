#Page de la mise en page de a navbar 

from dash import html, dcc

def create_navbar():
    return html.Nav([
        html.Div([
            html.H1(
                "Données des stations OpenAQ",   #Titre principal de la page 
                className='nav-title',
                style={
                    'color': 'white',
                    'margin': '10px 0',
                    'fontSize': '2rem',
                    'textShadow': '2px 2px 4px rgba(0,0,0,0.3)'
                }
            ),
            html.Div([
                dcc.Link(
                    "Accueil",  #Lien vers la page d'accueil
                    href="/", 
                    style={
                        'margin': '0 15px',
                        'color': 'white',
                        'textDecoration': 'none',
                        'padding': '10px 20px',
                        'borderRadius': '8px',
                        'backgroundColor': '#007bff',
                        'fontWeight': '600',
                        'transition': 'all 0.3s ease',
                        'boxShadow': '0 2px 5px rgba(0,0,0,0.2)'
                    }
                ),
                dcc.Link(
                "Histogramme",  #Lien vers la page d'histogramme
                    href="/histogramme", 
                    style={
                        'margin': '0 15px',
                        'color': 'white',
                        'textDecoration': 'none',
                        'padding': '10px 20px',
                        'borderRadius': '8px',
                        'backgroundColor': '#28a745',
                        'fontWeight': '600',
                        'transition': 'all 0.3s ease',
                        'boxShadow': '0 2px 5px rgba(0,0,0,0.2)'
                    }
                )
            ], style={
                'marginTop': '10px',
                'display': 'flex',
                'flexWrap': 'wrap',
                'justifyContent': 'center'
            })
        ], className='navbar', style={
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center',
            'padding': '20px',
            'backgroundColor': 'rgba(0, 0, 0, 0.2)',
            'backdropFilter': 'blur(10px)',
            'borderBottom': '1px solid rgba(255, 255, 255, 0.1)'
        })
    ])