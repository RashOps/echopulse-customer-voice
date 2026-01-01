import pandas as pd
from dash import Input, Output, State, callback, dcc
from graphs import make_topic_barchart, make_age_sentiment_chart, make_sunburst_chart, make_sentiment_distribution
from data_loader import load_data

# Chargement du dataset 
df = load_data()

@callback(
Output(component_id="kpi-volume", component_property="children"),
Output(component_id="kpi-sentiment", component_property="children"),
Output(component_id="kpi-rating", component_property="children"),
Output(component_id="topics", component_property="figure"),
Output(component_id="sunburst", component_property="figure"),
Output(component_id="age", component_property="figure"),
Output(component_id="sentiment", component_property="figure"),
Output(component_id="dataframe", component_property="data"),
Input(component_id="filter-dept", component_property="value"),
Input(component_id="filter-sentiment", component_property="value"),
Input(component_id="filter-topic", component_property="value"),
Input(component_id="search-input", component_property="value")
)

def update_dashboard(selected_depts, sentiment_range, selected_topic, search_text):
    dff = df.copy()
    
    low, high = sentiment_range
    dff = dff[dff["Sentiment Score"].between(low, high)]
    
    if selected_depts:
        dff = dff[dff["Division Name"].isin(selected_depts)]
    
    if selected_topic:
        dff = dff[dff["Topic Label"].isin(selected_topic)]
    
    if search_text:
        dff = dff[dff["Full Review"].str.contains(search_text, case=False, na=False)]
    
    # KPI
    if not dff.empty:
        vol = len(dff)
        sent = f"{dff['Sentiment Score'].mean():.2f}"
        rat = f"{dff['Rating'].mean():.1f}/5"
    else:
        vol, sent, rat = 0, "0.00", "0/5"

    # Graphs
    fig_topics = make_topic_barchart(dff)
    fig_sunburst = make_sunburst_chart(dff)
    fig_age = make_age_sentiment_chart(dff)
    fig_sentiment = make_sentiment_distribution(dff)

    return (vol, 
            sent, 
            rat, 
            fig_topics, 
            fig_sunburst, 
            fig_age, 
            fig_sentiment, 
            dff.to_dict('records'))

@callback(
    Output("download-dataframe-csv", "data"),
    Input("btn-csv", "n_clicks"),
    State("dataframe", "data"),
    prevent_initial_call=True,
)
def export_csv(n_clicks, table_data):
    dff = pd.DataFrame(table_data)
    return dcc.send_data_frame(dff.to_csv, "echopulse_export.csv", index=False)