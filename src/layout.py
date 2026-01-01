from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
from data_loader import load_data

# Chargement des graphs
from graphs import make_topic_barchart, make_age_sentiment_chart, make_sunburst_chart, make_sentiment_distribution

# Chargement du dataset 
df = load_data()

# Params
division_list = list(df["Division Name"].unique())
topic_list = list(df["Topic Label"].unique())

# Création des figures
fig_topics = make_topic_barchart(df)
fig_sunburst = make_sunburst_chart(df)
fig_age = make_age_sentiment_chart(df)
fig_sentiment = make_sentiment_distribution(df)

# Graphs_text
topic_text = "Analyse Thématique (LDA) > Ce graphique identifie les 5 piliers de l'expérience client. Utilisez ces segments pour prioriser vos actions : un volume élevé sur le sujet 'Sizing' indique un besoin urgent de réviser les guides des tailles."
sunburst_text = "Cartographie de la Satisfaction > Visualisation hiérarchique : Division > Département > Classe. La couleur indique le sentiment. Identifiez en un coup d'œil les 'zones rouges' pour isoler les catégories de produits sous-performantes."
age_text = "Profilage Générationnel > Analyse de la corrélation entre l'âge et la satisfaction. Ce graphique permet de vérifier si votre produit résonne avec votre cœur de cible ou s'il existe un clivage générationnel dans la perception de la marque."
hist_text = "Santé de la Marque (Polarité) > Distribution brute des émotions. Une courbe centrée indique un consensus, tandis qu'une distribution bimodale (deux pics) révèle un produit clivant qui nécessite une analyse qualitative plus profonde."

# Mise en place du layout
def layout() : 
    return dbc.Container([

        # Titre 
        dbc.Row([
            dbc.Col(html.H1("🗣️ EchoPulse Dashboard", className="text-primary text-center mt-2"), width=12),
            dbc.Col(html.P("Analyse sémantique des avis clients (NLP)", className="text-center text-secondary"), width=12),
            html.Hr()
        ], className="g-4"),

        # Description de l'application
        dbc.Row([
            dbc.Col(html.P("EchoPulse transforme le feedback non structuré en insights stratégiques. Notre moteur NLP analyse la sémantique pour identifier les points de friction produits et les leviers de satisfaction.",
                className="text-center"), width=12)
        ], className="g-4"), 


        # Left sidebar
        dbc.Row([
            dbc.Col([
                dbc.Card(dbc.CardBody(
                        [
                            html.Label("Recherche par mot-clé :"),
                            dcc.Input(id="search-input", type="text", placeholder="Ex: silky, fit...", className="form-control shadow-sm"),
                            html.Br(),
                            html.Label("Choisir une catégorie"),
                            dcc.Dropdown(options=[{'label': i, 'value': i} for i in division_list], value=None, placeholder="Toutes les divisions", id="filter-dept", className="shadow-sm", multi=True, style={'color': '#212121'}),
                            html.Br(),
                            html.Label("Score de Sentiment Min/Max :"),
                            dcc.RangeSlider(min=-1, max=1, value=[-1,1], step=0.1, marks={-1: 'Neg (-1)', 0: 'Neutre', 1: 'Pos (1)'}, id="filter-sentiment"),
                            html.Br(),
                            html.Label("Choisir des topics"),
                            dcc.Checklist(options=[{'label': i, 'value': i} for i in topic_list], value=topic_list, id="filter-topic")
                        ]
                    ), className="shadow-sm rounded border-0"),
                ], style={"position": "sticky", "top": "2rem"}, width=3),

            # Body's application
            dbc.Col([
                # Les KPIs
            dbc.Row([
            dbc.Col([
                    dbc.Card(dbc.CardBody(
                        [
                            html.H4(f"{df.shape[0]}", className="text-primary", id="kpi-volume"),
                            html.P("Avis Totaux", className="text-secondary"),
                            dbc.Tooltip("Nombre total de commentaires clients après filtrage.", target="kpi-volume")
                        ]
                    ), className="rounded border-0 shadow-sm")
            ], width=4),

            dbc.Col([
                    dbc.Card(dbc.CardBody(
                        [
                            html.H4(f"{df['Sentiment Score'].mean():.2f}", className="text-primary", id="kpi-sentiment"),
                            html.P("Sentiment Moyen", className="text-secondary"),
                            dbc.Tooltip("Moyenne TextBlob : -1 (Très Négatif) à +1 (Très Positif).", target="kpi-sentiment")
                        ]
                    ), className="rounded border-0 shadow-sm")
            ], width=4),

            dbc.Col([
                    dbc.Card(dbc.CardBody(
                        [
                            html.H4(f"{df['Rating'].mean():.1f}/5", className="text-primary", id="kpi-rating"),
                            html.P("Note Moyenne", className="text-secondary"),
                            dbc.Tooltip("Note moyenne sur 5 étoiles attribuée par les clients.", target="kpi-rating")
                        ]
                    ), className="rounded border-0 shadow-sm")
            ], width=4)
        ], className="mb-4 p-3 g-4"),

        # Les graphes
        dbc.Row([
            dbc.Col([dcc.Loading(
                    id="loading-1",
                    type="circle",
                    children=dcc.Graph(id="topics", figure=fig_topics)),
                    dbc.Badge("Insight IA", color="info"),
                    dcc.Markdown(topic_text)], width=6),

            dbc.Col([dcc.Loading(
                    id="loading-2",
                    type="circle",
                    children=dcc.Graph(id="sunburst", figure=fig_sunburst)),
                    dbc.Badge("Insight IA", color="info"),
                    dcc.Markdown(sunburst_text)], width=6)
        ], className="mb-4 p-3 g-4"),

        dbc.Row([
            dbc.Col([dcc.Loading(
                    id="loading-3",
                    type="circle",
                    children=dcc.Graph(id="age", figure=fig_age)),
                    dbc.Badge("Insight IA", color="info"),
                    dcc.Markdown(age_text)], width=6),

            dbc.Col([dcc.Loading(
                    id="loading-4",
                    type="circle",
                    children=dcc.Graph(id="sentiment", figure=fig_sentiment)),
                    dbc.Badge("Insight IA", color="info"),
                    dcc.Markdown(hist_text)], width=6)
        ], className="mt-4 mb-5 g-4")], width=9),

        # Affichage du dataset
        dbc.Row([
            dbc.Col([
                html.Hr(),
                html.H3("Nos données analysées", className="text-primary text-center"),
                dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df[["Title", "Rating", "Topic Label", "Sentiment Score", "Sentiment Category"]]], page_size=10, id="dataframe",
                        filter_action="native", sort_action="native",
                        style_header={'backgroundColor': '#303030', 'color': 'white', 'fontWeight': 'bold', 'border': '1px solid #444'},
                        style_data={'backgroundColor': '#222222', 'color': 'white', 'border': '1px solid #444'},
                        style_table={'height': '400px', 'overflowY': 'auto', 'borderRadius': '10px', 'overflow': 'hidden'},
                        style_cell={'textAlign': 'left', 'minWidth': '150px', 'fontFamily': 'inherit'},
                        style_data_conditional=[
                            {'if': {'filter_query': '{Sentiment Score} > 0.4', 'column_id': 'Sentiment Score'}, 'backgroundColor': '#2ecc71', 'color': 'white'},
                            {'if': {'filter_query': '{Sentiment Score} < 0', 'column_id': 'Sentiment Score'}, 'backgroundColor': '#e74c3c', 'color': 'white'}] 
                        ),
                            dbc.Tooltip("Télécharger les données filtrées au format Excel/CSV", target="btn-csv"),
                            dbc.Button("📥 Exporter en CSV", id="btn-csv", color="primary", className="mt-3"),
                            dcc.Download(id="download-dataframe-csv")
                    ], width=12)
                ])
            ])
    ],className="px-5", fluid=True)