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

## 🛠 Stack Technique (Objectif d'apprentissage)

Ce projet marque une montée en compétence vers des outils "Production-Ready".

* **Frontend / Dashboarding :** [Dash](https://dash.plotly.com/) (Python framework pour applis Web analytiques).
* **UI Components :** Dash Bootstrap Components (DBC).
* **Data Visualization :** Plotly Graph Objects.
* **NLP & IA :**
    * Cleaning (NLTK/Spacy)
    * Sentiment Analysis (VADER ou Transformers)
    * Topic Modeling (Scikit-learn LDA ou BERTopic)
* **Backend Data :** Pandas.

## 📂 Structure du Projet

```text
echopulse-customer-voice/
├── data/               # Données brutes et traitées
├── notebooks/          # Experimentation NLP (Jupyter)
├── src/                # Code source de l'application Dash
│   ├── app.py          # Serveur principal
│   ├── layout.py       # Structure visuelle (HTML/Divs)
│   └── callbacks.py    # Logique interactive
└── assets/             # CSS et images
