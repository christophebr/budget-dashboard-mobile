# 📱 Guide Mobile - Dashboard Budget

## 🎯 **Déploiement Mobile avec Streamlit**

### **Option A : Accès Local (Recommandé pour débuter)**

#### 1. **Lancer le Dashboard Mobile**
```bash
python run_mobile.py
```

#### 2. **Accéder depuis votre iPhone/iPad**
- **Sur le même réseau WiFi** : `http://192.168.1.155:8501`
- **Remplacer 192.168.1.155** par l'IP de votre ordinateur
- **Trouver votre IP** : `ipconfig` (Windows) ou `ifconfig` (Mac/Linux)

#### 3. **Ajouter à l'écran d'accueil iOS**
1. Ouvrir Safari sur votre iPhone
2. Aller à l'URL du dashboard
3. Appuyer sur le bouton "Partager" (carré avec flèche)
4. Sélectionner "Ajouter à l'écran d'accueil"
5. Personnaliser le nom : "Budget"
6. Appuyer sur "Ajouter"

### **Option B : Déploiement Cloud (Accès depuis n'importe où)**

#### 1. **Créer un Repository GitHub**
```bash
# Initialiser Git
git init
git add .
git commit -m "Dashboard Budget Mobile"

# Créer un repository sur GitHub
# Pousser le code
git remote add origin https://github.com/votre-username/budget-mobile.git
git push -u origin main
```

#### 2. **Déployer sur Streamlit Cloud**
1. Aller sur [share.streamlit.io](https://share.streamlit.io)
2. Se connecter avec GitHub
3. Sélectionner votre repository
4. Configurer :
   - **Main file path** : `dashboard_mobile.py`
   - **App URL** : `votre-app.streamlit.app`
5. Déployer

#### 3. **Accéder depuis Mobile**
- URL publique : `https://votre-app.streamlit.app`
- Ajouter à l'écran d'accueil iOS (même procédure)

## 📱 **Optimisations Mobile Incluses**

### **Interface Adaptée**
- ✅ **Sidebar fermée** par défaut
- ✅ **Boutons plus grands** pour le tactile
- ✅ **Police 16px** (évite le zoom iOS)
- ✅ **Graphiques optimisés** pour mobile
- ✅ **Tableaux simplifiés**

### **Fonctionnalités Mobile**
- ✅ **Filtres en haut** de page
- ✅ **Métriques principales** bien visibles
- ✅ **Transactions récentes** (20 dernières)
- ✅ **Recherche simplifiée**
- ✅ **Téléchargement CSV** facile

### **Navigation Touch-Friendly**
- ✅ **Éléments espacés** pour éviter les erreurs
- ✅ **Scroll fluide** sur mobile
- ✅ **Graphiques responsives**
- ✅ **Texte lisible** sur petit écran

## 🔧 **Configuration Avancée**

### **Variables d'Environnement (Streamlit Cloud)**
```toml
# .streamlit/secrets.toml
[general]
app_name = "Budget Mobile"
```

### **Configuration Streamlit**
```toml
# .streamlit/config.toml
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
```

## 📊 **Fonctionnalités du Dashboard Mobile**

### **Vue d'Ensemble**
- Revenus, Dépenses, Solde Net
- Graphique d'évolution du solde
- Répartition des montants

### **Filtres**
- Période (date de début/fin)
- Fichier source
- Type de transaction
- Recherche textuelle

### **Données**
- 20 dernières transactions
- Export CSV
- Statistiques rapides

## 🚀 **Prochaines Étapes**

1. **Tester localement** : `python run_mobile.py`
2. **Accéder depuis mobile** via l'IP locale
3. **Ajouter à l'écran d'accueil** iOS
4. **Déployer sur Streamlit Cloud** pour un accès permanent
5. **Partager l'URL** avec d'autres utilisateurs

## 📞 **Support**

### **Problèmes Courants**
- **"Site non accessible"** : Vérifier l'IP et le port
- **"Interface déformée"** : Vider le cache du navigateur
- **"Données manquantes"** : Relancer l'extraction

### **Optimisations Supplémentaires**
- Ajouter des notifications push
- Intégrer avec des APIs bancaires
- Créer des alertes de budget
- Synchronisation automatique

---

*Dashboard Mobile optimisé pour iOS et Android* 📱
