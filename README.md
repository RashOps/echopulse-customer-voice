# 🗣️ EchoPulse : Customer Sentiment & Insight Engine

> **Projet Data Science & Business Intelligence**

**EchoPulse** est un dashboard analytique "SaaS-Ready" conçu pour transformer le feedback client non structuré en insights stratégiques. Grâce à un moteur **NLP (Natural Language Processing)**, l'outil identifie automatiquement les frictions produits et les leviers de satisfaction.

### 🌐 [Accéder à l'application en direct (Render)](https://echopulse-customer-voice.onrender.com/)

![Status](https://img.shields.io/badge/Status-Deployed-success)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-v3.3.0-008ED5?logo=plotly&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 Objectifs Business
Lire 23 000 avis un par un est impossible. Ce projet vise à :
1. **Monitorer la santé de la marque** via l'analyse de sentiment (Positif/Négatif/Neutre).
2. **Détecter les sujets de friction** automatiquement (Topic Modeling) : Problèmes de taille, qualité du tissu, logistique...
3. **Segmenter les retours** par catégorie de produit (Robes, Hauts, etc.) et par profil démographique.

## 🚀 Fonctionnalités Clés
- **Analyse de Sentiment Dynamique :** Visualisation de la polarité via TextBlob.
- **Topic Modeling (IA) :** Segmentation automatique par thématiques stratégiques.
- **Filtrage Multidimensionnel :** Exploration par catégorie, âge, sentiment et recherche textuelle sécurisée (Regex protection).
- **Export Business :** Extraction des données filtrées au format CSV.
- **UI/UX Premium :** Interface optimisée avec le thème **Darkly**, tooltips interactifs et chargement asynchrone (Spinners).

## 🛠 Stack Technique

### **Data & Intelligence**
![Pandas](https://img.shields.io/badge/Pandas-v2.3.3-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-v2.3.5-013243?logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.7.2-F7931E?logo=scikit-learn&logoColor=white)
![TextBlob](https://img.shields.io/badge/NLP-TextBlob-FF69B4?logo=python&logoColor=white)

### **Visualisation & Interface**
![Plotly](https://img.shields.io/badge/Plotly-v6.5.0-3F4F75?logo=plotly&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-v2.0.4-7952B3?logo=bootstrap&logoColor=white)

### **Infrastructure & Déploiement**
![Gunicorn](https://img.shields.io/badge/Gunicorn-Production%20Server-499848?logo=gunicorn&logoColor=white)
![Git](https://img.shields.io/badge/Git-Source%20Control-F05032?logo=git&logoColor=white)
![Render](https://img.shields.io/badge/Render-Cloud%20Hosting-46E3B7?logo=render&logoColor=white)

---

## 📂 Structure du Projet

```text
echopulse/
├── data/               # Données sources (CSV)
├── src/                # Code source de l'application
│   ├── app.py          # Point d'entrée & Serveur Flask
│   ├── layout.py       # Définition de l'UI (DBC)
│   ├── callbacks.py    # Logique réactive & Interactivité
│   ├── graphs.py       # Moteur de rendu Plotly
│   └── data_loader.py  # Gestion de l'ingestion de données
├── assets/             # CSS personnalisé (Dark Mode fixes)
├── Procfile            # Configuration Gunicorn pour Render
└── requirements.txt    # Dépendances de production 
```

## ⚙️ Installation & Lancement
1. Installer les dépendances : `pip install -r requirements.txt`
2. Lancer le serveur local : `python src/app.py`
3. Accéder à l'app : `http://127.0.0.1:8050`