import dash
import dash_bootstrap_components as dbc
from layout import layout
import callbacks

# Initialisation de l'application
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.DARKLY],
                suppress_callback_exceptions=True)
server = app.server  

# Construction de l'application
app.layout = layout

# Debugging
if __name__ == '__main__':
    app.run(debug=True)