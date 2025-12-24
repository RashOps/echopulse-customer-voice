import pandas as pd
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import os
from data_loader import load_data

# Initialisation de l'application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  

# Construction de l'application
app.layout = dbc.Container([

    # Titre 
    dbc.Row([
        dbc.Col(html.H1("🗣️ EchoPulse Dashboard", className="text-center text-primary mb-4"), width=12)
    ])
])

# Debugging
if __name__ == '__main__':
    # debug=True permet de voir les erreurs en direct dans le navigateur
    app.run(debug=True)