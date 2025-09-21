# 💰 Dashboard Budget Personnel

Un système complet pour extraire et visualiser les données de vos relevés de compte bancaires PDF.

## 🚀 Fonctionnalités

- **Extraction automatique** des données depuis les PDFs de relevés bancaires
- **Conversion en CSV** pour un traitement facile des données
- **Dashboard interactif** avec visualisations et filtres
- **Statistiques détaillées** sur vos revenus et dépenses
- **Export des données** filtrées

## 📁 Structure du Projet

```
Budget/
├── releve/                    # Dossier contenant vos PDFs de relevés
│   ├── 202508.pdf
│   └── 202509.pdf
├── extract_pdf_simple.py     # Script d'extraction des données PDF
├── dashboard.py              # Interface dashboard Streamlit
├── run_dashboard.py          # Script de lancement automatique
├── requirements.txt          # Dépendances Python
├── transactions_clean.csv    # Données extraites (généré automatiquement)
└── README.md                 # Ce fichier
```

## 🛠️ Installation

1. **Installer les dépendances Python :**
   ```bash
   pip install -r requirements.txt
   ```

2. **Placer vos PDFs de relevés** dans le dossier `releve/`

## 🎯 Utilisation

### Méthode 1 : Lancement automatique (Recommandé)
```bash
python run_dashboard.py
```

### Méthode 2 : Lancement manuel

1. **Extraire les données des PDFs :**
   ```bash
   python extract_pdf_simple.py
   ```

2. **Lancer le dashboard :**
   ```bash
   streamlit run dashboard.py
   ```

3. **Ouvrir votre navigateur** à l'adresse : http://localhost:8501

## 📊 Fonctionnalités du Dashboard

### Métriques Principales
- Nombre total de transactions
- Total des revenus
- Total des dépenses
- Solde net

### Visualisations
- **Évolution du solde** au fil du temps
- **Répartition des montants** par catégorie
- **Transactions par mois** (graphique en barres)

### Filtres et Recherche
- Filtrage par période (date de début/fin)
- Filtrage par fichier source
- Recherche dans les descriptions
- Affichage des revenus ou dépenses uniquement

### Export des Données
- Téléchargement des données filtrées en CSV
- Statistiques avancées (top transactions)

## 🔧 Personnalisation

### Ajouter de nouveaux PDFs
1. Placez vos nouveaux PDFs dans le dossier `releve/`
2. Relancez l'extraction : `python extract_pdf_simple.py`
3. Rechargez le dashboard

### Modifier les patterns d'extraction
Le fichier `extract_pdf_simple.py` contient les patterns d'extraction. Vous pouvez les modifier selon le format de vos relevés bancaires.

## 📝 Notes Importantes

- Le script d'extraction fonctionne mieux avec des PDFs de relevés bancaires français
- Les dates doivent être au format DD/MM/YYYY
- Les montants peuvent utiliser la virgule ou le point comme séparateur décimal
- Le dashboard se met à jour automatiquement quand vous ajoutez de nouveaux PDFs

## 🐛 Dépannage

### Problème d'extraction
- Vérifiez que vos PDFs ne sont pas protégés par mot de passe
- Assurez-vous que le texte est sélectionnable dans vos PDFs
- Vérifiez le format des dates dans vos relevés

### Problème d'affichage
- Vérifiez que le fichier `transactions_clean.csv` a été généré
- Relancez l'extraction si nécessaire

## 📞 Support

Pour toute question ou problème, vérifiez d'abord :
1. Que toutes les dépendances sont installées
2. Que vos PDFs sont dans le bon dossier
3. Que le fichier CSV a été généré correctement

---

*Dashboard créé avec ❤️ en Python et Streamlit*
