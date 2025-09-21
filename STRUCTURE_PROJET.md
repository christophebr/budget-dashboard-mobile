# 📁 Structure du Projet Budget - Version Finale

## 🎯 **Fichiers Essentiels**

### 🐍 **Scripts Python (4 fichiers)**
- **`extract_all_transactions.py`** - Script d'extraction principal
- **`dashboard.py`** - Interface dashboard Streamlit
- **`run_dashboard.py`** - Script de lancement automatique
- **`verify_data.py`** - Script de vérification des données

### 📊 **Données**
- **`transactions_complete.csv`** - Données extraites (262 transactions)
- **`releve/`** - Dossier contenant vos PDFs de relevés
  - `202508.pdf` - Relevé août 2025
  - `202509.pdf` - Relevé septembre 2025

### 📋 **Configuration**
- **`requirements.txt`** - Dépendances Python
- **`README.md`** - Guide d'installation
- **`GUIDE_UTILISATION.md`** - Guide d'utilisation détaillé

### 📈 **Fichiers CSV Anciens (à supprimer)**
- `transactions_banque_postale.csv` - Version intermédiaire
- `transactions_clean.csv` - Version intermédiaire
- `transactions_final.csv` - Version intermédiaire
- `transactions_real.csv` - Version intermédiaire
- `transactions.csv` - Version initiale

## 🚀 **Utilisation Simple**

### Lancement du Dashboard
```bash
python run_dashboard.py
```
Puis ouvrir http://localhost:8501

### Extraction Manuelle
```bash
python extract_all_transactions.py
```

### Vérification des Données
```bash
python verify_data.py
```

## 🧹 **Nettoyage Supplémentaire**

Vous pouvez également supprimer les anciens fichiers CSV :
- `transactions_banque_postale.csv`
- `transactions_clean.csv`
- `transactions_final.csv`
- `transactions_real.csv`
- `transactions.csv`

Il ne reste que **4 scripts Python essentiels** pour un projet propre et maintenable ! 🎉
