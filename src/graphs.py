import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# 1. Graphique des Topics (Bar Chart Horizontal)
def make_topic_barchart(df):
    if df.empty:
        fig = go.Figure(),
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'),
        fig.add_annotation(text="Aucune donnée ne correspond à ces filtres", showarrow=False, font=dict(size=20))
        return fig

    topic_counts = df["Topic Label"].value_counts().reset_index()
    topic_counts.columns = ["Topic", "Count"]
    
    fig = px.bar(
        topic_counts, 
        x="Count", 
        y="Topic", 
        orientation="h",
        title="Volume d'avis par Sujet",
        text="Count",
        color="Count",
        color_continuous_scale="Bluyl"
    )
    fig.update_layout(yaxis={"categoryorder":"total ascending"})

    fig.update_layout(
        template="plotly_dark", 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode="x unified",         
        margin=dict(l=20, r=20, t=40, b=20),   
        font=dict(color="#ffffff"))
    return fig

# 2. Graphique Hiérarchique (Sunburst)
def make_sunburst_chart(df):
    if df.empty:
        fig = go.Figure(),
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'),
        fig.add_annotation(text="Aucune donnée ne correspond à ces filtres", showarrow=False, font=dict(size=20))
        return fig

    fig = px.sunburst(
        df, 
        path=["Division Name", "Department Name", "Class Name"], 
        values="Rating", 
        color="Sentiment Score", 
        color_continuous_scale="RdBu",
        color_continuous_midpoint=0,
        title="Exploration par Catégorie Produit"
    )

    fig.update_traces(hoverinfo="label+percent entry")

    fig.update_layout(
        template="plotly_dark", 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',         
        margin=dict(l=20, r=20, t=40, b=20),   
        font=dict(color="#ffffff"))
    return fig

# 3. Graphique Démographique (Distribution Sentiment par Age)
def make_age_sentiment_chart(df):
    if df.empty:
        fig = go.Figure(),
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'),
        fig.add_annotation(text="Aucune donnée ne correspond à ces filtres", showarrow=False, font=dict(size=20))
        return fig
    
    df_temp = df.copy()
    df_temp["Age_Group"] = pd.cut(df_temp["Age"], bins=[18, 25, 35, 45, 55, 65, 99], labels=['18-25', '26-35', '36-45', '46-55', '56-65', '65+'])
    
    age_stats = df_temp.groupby("Age_Group", observed=True)["Sentiment Score"].mean().reset_index()
    
    fig = px.line(
        age_stats,
        x="Age_Group",
        y="Sentiment Score",
        markers=True,
        title="Sentiment Moyen par Tranche d'Âge",
        line_shape="spline"
    )

    fig.update_layout(
        template="plotly_dark", 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode="x unified",         
        margin=dict(l=20, r=20, t=40, b=20),   
        font=dict(color="#ffffff"))
    return fig

# 4. Graphique distribution de la polarité
def make_sentiment_distribution(df):
    if df.empty:
        fig = go.Figure(),
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'),
        fig.add_annotation(text="Aucune donnée ne correspond à ces filtres", showarrow=False, font=dict(size=20))
        return fig
    
    fig = px.histogram(
        df,
        x="Sentiment Score",
        color="Sentiment Category",
        nbins=50,
        template="plotly_dark",
        title="Distribution de la Polarité des Avis",
        color_discrete_map={"Positif": '#2ecc71', 'Neutre': '#95a5a6', 'Négatif': '#e74c3c'},
        labels={"Sentiment Score": "Score de Sentiment", "count": "Nombre d'avis"}
    )
    
    # Ajout d'une ligne verticale pour la moyenne globale
    fig.add_vline(x=df["Sentiment Score"].mean(), line_dash="dash", line_color="#ecf0f1", 
        annotation_text="Moyenne", annotation_position="top left")
    
    fig.update_layout(showlegend=True, bargap=0.1)

    fig.update_layout(
        template="plotly_dark", 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode="x unified", 
        margin=dict(l=20, r=20, t=40, b=20),  
        font=dict(color="#ffffff"),
        hoverlabel=dict(
            bgcolor="#222", 
            font_size=13, 
            font_family="Inter, sans-serif",
            bordercolor="#444"
        ))
    return fig