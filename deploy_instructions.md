# 🚀 Instructions de Déploiement Streamlit Cloud

## 📋 **Étapes de Déploiement**

### **1. Créer un Repository GitHub**

1. **Aller sur GitHub.com** et créer un nouveau repository
2. **Nom suggéré** : `budget-dashboard-mobile`
3. **Description** : "Dashboard Budget Personnel Mobile"
4. **Visibilité** : Public (gratuit) ou Privé
5. **Cocher** : "Add a README file"

### **2. Cloner et Préparer le Repository**

```bash
# Cloner votre repository (remplacez par votre URL)
git clone https://github.com/votre-username/budget-dashboard-mobile.git
cd budget-dashboard-mobile

# Copier vos fichiers dans le repository
# (Copier tous les fichiers .py, .md, requirements.txt, etc.)
```

### **3. Pousser le Code sur GitHub**

```bash
# Ajouter tous les fichiers
git add .

# Commit initial
git commit -m "Initial commit: Dashboard Budget Mobile"

# Pousser sur GitHub
git push origin main
```

### **4. Déployer sur Streamlit Cloud**

1. **Aller sur** [share.streamlit.io](https://share.streamlit.io)
2. **Se connecter** avec votre compte GitHub
3. **Cliquer** sur "New app"
4. **Remplir le formulaire** :
   - **Repository** : `votre-username/budget-dashboard-mobile`
   - **Branch** : `main`
   - **Main file path** : `dashboard_mobile.py`
   - **App URL** : `budget-dashboard-mobile` (ou votre choix)
5. **Cliquer** sur "Deploy!"

### **5. Accéder à Votre App Mobile**

- **URL publique** : `https://budget-dashboard-mobile.streamlit.app`
- **Ajouter à l'écran d'accueil iOS** :
  1. Ouvrir Safari
  2. Aller à l'URL
  3. Partager → "Ajouter à l'écran d'accueil"
  4. Nommer "Budget"

## 📱 **Optimisations Mobile Incluses**

- ✅ Interface responsive
- ✅ Boutons tactiles optimisés
- ✅ Graphiques adaptés mobile
- ✅ Navigation simplifiée
- ✅ Filtres en haut de page

## 🔧 **Configuration Avancée**

### **Variables d'Environnement (si nécessaire)**
```toml
# .streamlit/secrets.toml
[general]
app_name = "Budget Mobile"
```

### **Mise à Jour de l'App**
```bash
# Modifier vos fichiers
git add .
git commit -m "Update dashboard"
git push origin main
# L'app se met à jour automatiquement
```

## 📊 **Fonctionnalités Disponibles**

- **Vue d'ensemble** : Revenus, dépenses, solde
- **Graphiques** : Évolution du solde, répartition
- **Filtres** : Période, source, type
- **Recherche** : Dans les descriptions
- **Export** : Téléchargement CSV

## 🆘 **Dépannage**

### **Problèmes Courants**
- **"App not found"** : Vérifier l'URL et le repository
- **"Import error"** : Vérifier requirements.txt
- **"Data not loading"** : Vérifier les fichiers CSV

### **Logs de Debug**
- Aller dans l'interface Streamlit Cloud
- Cliquer sur "Manage app"
- Voir les logs en temps réel

## 🎉 **Résultat Final**

Vous aurez une application mobile accessible depuis n'importe où :
- **URL publique** permanente
- **Interface mobile** optimisée
- **Mise à jour automatique** du code
- **Accès depuis iPhone/iPad** via l'écran d'accueil

---

*Votre dashboard budget est maintenant une vraie application mobile !* 📱
