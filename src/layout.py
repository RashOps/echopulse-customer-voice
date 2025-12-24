import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc
from data_loader import load_data

# Chargement des graphs
from graphs import make_topic_barchart, make_age_sentiment_chart, make_sunburst_chart
