from dash import dcc, html

about_layout = html.Div([
    dcc.Markdown("""

## ️ℹ️ Informations générales

**Auteurs :** `Allemann Alexis`, `Corpataux Sam`, `Koch Gaël`

## 🏃 Installation de l'environnement de développement

**Prérequis :** 

- au minimum `Python v3.8`

**Cloner le repository GitHub :** 

```bash
git clone git@github.com:gakoo35/VI-WTSW.git
```

**Installation des dépendances :**

```bash
pip install -r requirements.txt
```

## 🚀 Exécuter le projet

```bash
python main.py
```

**Accéder à** http://127.0.0.1:8989/

    """)
])
