# 🗣️ EchoPulse : Customer Sentiment & Insight Engine

> **Projet Data Science & Business Intelligence**

**EchoPulse** est un dashboard analytique conçu pour aider les chefs de produit à écouter la "voix du client" à grande échelle. Il utilise le **Traitement du Langage Naturel (NLP)** pour transformer des milliers d'avis textuels en indicateurs stratégiques actionnables.

![Status](https://img.shields.io/badge/Status-In%20Development-yellow) [![Dash](https://img.shields.io/badge/Dash-App-blue?logo=plotly)](https://dash.plotly.com/)

---

## 🎯 Objectifs Business
Lire 23 000 avis un par un est impossible. Ce projet vise à :
1.  **Monitorer la santé de la marque** via l'analyse de sentiment (Positif/Négatif/Neutre).
2.  **Détecter les sujets de friction** automatiquement (Topic Modeling) : Problèmes de taille, qualité du tissu, logistique...
3.  **Segmenter les retours** par catégorie de produit (Robes, Hauts, etc.) et par âge des clients.

## 🚀 Fonctionnalités Clés
- **Analyse de Sentiment Dynamique :** Visualisation de la polarité des avis (Positif/Négatif/Neutre) via TextBlob.
- **Topic Modeling (IA) :** Segmentation automatique des retours par thématiques (Sizing, Quality, Service).
- **Filtrage Multidimensionnel :** Exploration par catégorie, tranche d'âge, score de sentiment et recherche textuelle sécurisée (Regex protection).
- **Export Business :** Extraction des données filtrées au format CSV pour des rapports externes.
- **UI/UX Premium :** Interface optimisée avec le thème Darkly, tooltips interactifs et chargement asynchrone (Spinners).

## 🛠 Stack Technique
- **Framework :** Plotly Dash (Python)
- **UI :** Dash Bootstrap Components (Thème Darkly)
- **Data & NLP :** Pandas, TextBlob, Scikit-Learn
- **Déploiement :** Gunicorn (Production Server), Render

## 📂 Structure du Projet

```text
echopulse-customer-voice/
├── data/               # Données brutes et traitées
├── notebooks/          # Experimentation NLP (Jupyter)
├── src/                # Code source de l'application Dash
│   ├── app.py          # Serveur principal
│   ├── layout.py       # Structure visuelle (HTML/Divs)
│   └── callbacks.py    # Logique interactive
└── assets/             # CSS

## ⚙️ Installation & Lancement
1. Installer les dépendances : `pip install -r requirements.txt`
2. Lancer le serveur local : `python src/app.py`
3. Accéder à l'app : `http://127.0.0.1:8050`