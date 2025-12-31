from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from data_loader import load_data

# Chargement des graphs
from graphs import make_topic_barchart, make_age_sentiment_chart, make_sunburst_chart, make_sentiment_distribution

# Chargement du dataset 
df = load_data()

# Params
division_list = list(df["Division Name"].unique())

# Création des figures
fig_topics = make_topic_barchart(df)
fig_sunburst = make_sunburst_chart(df)
fig_age = make_age_sentiment_chart(df)
fig_sentiment = make_sentiment_distribution(df)

# Mise en place du layout
def layout() : 
    return dbc.Container([

        # Titre 
        dbc.Row([
            dbc.Col(html.H1("🗣️ EchoPulse Dashboard", className="text-primary text-center"), width=12),
            dbc.Col(html.P("Analyse sémantique des avis clients (NLP)", className="text-center text-secondary"), width=12),
            html.Hr()
        ]),

        # Description de l'application
        dbc.Row([
            dbc.Col(html.P("EchoPulse transforme le feedback non structuré en insights stratégiques. Notre moteur NLP analyse la sémantique pour identifier les points de friction produits et les leviers de satisfaction.",
                className="text-center"), width=12)
        ]), 


        # Left sidebar
        dbc.Row([
            dbc.Col([
                dbc.Card(dbc.CardBody(
                        [
                            html.Label("Choisir une catégorie"),
                            dcc.Dropdown(options=[{'label': i, 'value': i} for i in division_list], value=None, placeholder="Toutes les divisions", id="filter-dept", className="shadow-sm", multi=True),
                            html.Br(),
                            html.Label("Score de Sentiment Min/Max :"),
                            dcc.RangeSlider(min=-1, max=1, value=[-1,1], step=0.1, marks={-1: 'Neg (-1)', 0: 'Neutre', 1: 'Pos (1)'}, id="filter-sentiment")
                        ]
                    ), className="shadow-sm rounded border-0"),
                ], width=3),

            # Body's application
            dbc.Col([
                # Les KPIs
            dbc.Row([
            dbc.Col([
                    dbc.Card(dbc.CardBody(
                        [
                            html.H4(f"{df.shape[0]}", className="shadow-sm p-3"),
                            html.P("Avis Totaux"),
                        ]
                    ), id="kpi-volume", className="rounded border-0 text-primary")
            ], width=4),

            dbc.Col([
                    dbc.Card(dbc.CardBody(
                        [
                            html.H4(f"{df['Sentiment Score'].mean():.2f}", className="shadow-sm p-3"),
                            html.P("Sentiment Moyen"),
                        ]
                    ), id="kpi-sentiment", className="rounded border-0 text-primary")
            ], width=4),

            dbc.Col([
                    dbc.Card(dbc.CardBody(
                        [
                            html.H4(f"{df['Rating'].mean():.1f}/5", className="shadow-sm p-3"),
                            html.P("Note Moyenne"),
                        ]
                    ), id="kpi-rating", className="rounded border-0 text-primary")
            ], width=4)
        ], className="mb-4 p-3 rounded border-0 shadow-sm"),

        # Les graphes
        dbc.Row([
            dbc.Col([dcc.Graph(id="topics", figure=fig_topics),
                    dcc.Markdown("""""")], width=6),

            dbc.Col([dcc.Graph(id="sunburst", figure=fig_sunburst),
                    dcc.Markdown("""""")], width=6)
        ], className="mb-4 p-3"),

        dbc.Row([
            dbc.Col([dcc.Graph(id="age", figure=fig_age),
                    dcc.Markdown("""""")], width=6),

            dbc.Col([dcc.Graph(id="sentiment", figure=fig_sentiment),
                    dcc.Markdown("""""")], width=6)
        ], className="mt-4 mb-5")], width=9),

        # Affichage du dataset filtré
        dbc.Row([
            dbc.Col([
                html.Hr(),
                html.H3("Nos données analysées", className="text-primary text-center"),
                dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], page_size=10, style_cell={'textAlign': 'left', 'minWidth': '150px'}, style_table={'height': '400px', 'overflowY': 'auto'})
                ], width=12)
            ])
        ])
    ])

