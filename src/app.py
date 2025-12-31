import pandas as pd
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from layout import layout

# Initialisation de l'application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  

# Construction de l'application
app.layout = layout

# Debugging
if __name__ == '__main__':
    app.run(debug=True)