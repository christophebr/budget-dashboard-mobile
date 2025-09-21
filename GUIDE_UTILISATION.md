# 📋 Guide d'Utilisation - Dashboard Budget Personnel

## 🎯 Vue d'ensemble

Ce système vous permet d'extraire automatiquement les données de vos relevés de compte bancaires PDF et de les visualiser dans un dashboard interactif.

## 📊 Données Extraites

Le système extrait actuellement **9 transactions** de vos relevés :

### Types de transactions détectées :
- **Ancien solde** : Solde initial du relevé
- **Paiements par carte bancaire** : Avec montant exact extrait
- **Prélèvements** : Comme ALAN INSURANCE
- **Frais bancaires** : Frais et cotisations

### Période couverte :
- **Du 07/07/2025 au 07/08/2025**
- **Total des dépenses** : -389,17 €
- **Total des revenus** : 1 807,01 €
- **Solde net** : 1 417,84 €

## 🚀 Utilisation

### Lancement rapide :
```bash
python run_dashboard.py
```

### Lancement manuel :
1. **Extraire les données** :
   ```bash
   python extract_real_transactions.py
   ```

2. **Lancer le dashboard** :
   ```bash
   streamlit run dashboard.py
   ```

3. **Ouvrir votre navigateur** : http://localhost:8501

## 📈 Fonctionnalités du Dashboard

### Métriques Principales
- **Total Transactions** : Nombre de transactions extraites
- **Total Revenus** : Somme des montants positifs
- **Total Dépenses** : Somme des montants négatifs
- **Solde Net** : Différence entre revenus et dépenses

### Visualisations
1. **Évolution du Solde** : Graphique linéaire montrant l'évolution du solde
2. **Répartition des Montants** : Graphique en secteurs par catégorie
3. **Transactions par Mois** : Graphique en barres des montants mensuels

### Filtres et Recherche
- **Filtre par période** : Sélection de dates de début et fin
- **Filtre par source** : Choix du fichier PDF source
- **Recherche** : Recherche dans les descriptions
- **Filtres de type** : Revenus uniquement / Dépenses uniquement

### Export des Données
- **Téléchargement CSV** : Export des données filtrées
- **Statistiques avancées** : Top 5 des plus grosses/petites transactions

## 🔧 Personnalisation

### Ajouter de nouveaux PDFs
1. Placez vos nouveaux PDFs dans le dossier `releve/`
2. Relancez l'extraction : `python extract_real_transactions.py`
3. Rechargez le dashboard

### Modifier les patterns d'extraction
Le fichier `extract_real_transactions.py` contient les patterns pour :
- Paiements par carte bancaire
- Prélèvements automatiques
- Virements
- Frais bancaires

Vous pouvez les adapter selon le format de vos relevés.

## 📝 Notes Importantes

### Format des PDFs supportés
- **La Banque Postale** (format actuel)
- PDFs avec texte sélectionnable
- Dates au format DD/MM/YYYY
- Montants avec virgule comme séparateur décimal

### Limitations actuelles
- Certains montants sont estimés (prélèvements ALAN)
- Les descriptions peuvent être tronquées
- Seules les transactions principales sont extraites

## 🐛 Dépannage

### Problèmes courants

1. **"Aucune donnée à sauvegarder"**
   - Vérifiez que vos PDFs sont dans le dossier `releve/`
   - Assurez-vous que le texte est sélectionnable dans vos PDFs

2. **Montants incorrects**
   - Vérifiez le format des montants dans vos PDFs
   - Ajustez les patterns dans `extract_real_transactions.py`

3. **Dashboard ne se lance pas**
   - Vérifiez que Streamlit est installé : `pip install streamlit`
   - Vérifiez que le fichier `transactions_real.csv` existe

### Logs de débogage
Pour voir les détails de l'extraction, exécutez :
```bash
python extract_real_transactions.py
```

## 📞 Support

### Fichiers importants
- `extract_real_transactions.py` : Script d'extraction principal
- `dashboard.py` : Interface dashboard
- `run_dashboard.py` : Script de lancement automatique
- `transactions_real.csv` : Données extraites (généré automatiquement)

### Structure des données CSV
```csv
date,description,amount,source_file
2025-07-07,Ancien solde,631.6,202508.pdf
2025-07-28,Paiement Carte Bancaire 17,09 €,-17.09,202508.pdf
```

---

*Dashboard créé avec ❤️ en Python et Streamlit*
