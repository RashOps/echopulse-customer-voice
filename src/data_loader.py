import pandas as pd
import os

def load_data():
    """
    Charge les données traitées depuis le dossier data/processed.
    Renvoie un DataFrame Pandas.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'reviews_with_sentiment_and_topics.csv')
    
    try:
        df = pd.read_csv(data_path)
        print(f"✅ Données chargées : {df.shape[0]} lignes")
        return df
    except FileNotFoundError:
        print(f"❌ ERREUR CRITIQUE : Fichier introuvable ici : {data_path}")
        return pd.DataFrame()