#!/usr/bin/env python3
"""
Script pour déployer sur Streamlit Cloud
"""

import webbrowser

def main():
    print("🚀 Déploiement sur Streamlit Cloud")
    print("=" * 50)
    
    print("✅ Code poussé vers GitHub avec succès !")
    print("📁 Repository : https://github.com/christophebr/budget-dashboard-mobile")
    
    print("\n🌐 Ouverture de Streamlit Cloud...")
    webbrowser.open("https://share.streamlit.io")
    
    print("\n📋 Instructions pour déployer :")
    print("1. Se connecter avec votre compte GitHub")
    print("2. Cliquer sur 'New app'")
    print("3. Remplir le formulaire :")
    print("   - Repository : christophebr/budget-dashboard-mobile")
    print("   - Branch : main")
    print("   - Main file path : dashboard_mobile.py")
    print("   - App URL : budget-dashboard-mobile")
    print("4. Cliquer sur 'Deploy!'")
    
    print("\n⏳ Le déploiement prendra 2-3 minutes...")
    
    print("\n📱 Une fois déployé, votre app sera accessible à :")
    print("https://budget-dashboard-mobile.streamlit.app")
    
    print("\n📱 Pour l'ajouter à l'écran d'accueil iOS :")
    print("1. Ouvrir Safari sur votre iPhone")
    print("2. Aller à l'URL de l'app")
    print("3. Appuyer sur le bouton 'Partager' (carré avec flèche)")
    print("4. Sélectionner 'Ajouter à l'écran d'accueil'")
    print("5. Personnaliser le nom : 'Budget'")
    print("6. Appuyer sur 'Ajouter'")
    
    print("\n🎉 Votre dashboard budget sera alors une vraie app mobile !")
    
    print("\n📊 Fonctionnalités disponibles :")
    print("✅ Interface mobile optimisée")
    print("✅ 262 transactions extraites")
    print("✅ Graphiques interactifs")
    print("✅ Filtres et recherche")
    print("✅ Export des données")
    print("✅ Accès depuis n'importe où")

if __name__ == "__main__":
    main()
