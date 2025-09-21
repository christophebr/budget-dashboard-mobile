#!/usr/bin/env python3
"""
Script de déploiement automatique pour Streamlit Cloud
"""

import subprocess
import sys
import os

def check_git():
    """Vérifie si Git est installé et configuré"""
    try:
        subprocess.run(["git", "--version"], check=True, capture_output=True)
        print("✅ Git installé")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git non installé. Veuillez installer Git d'abord.")
        return False

def init_git_repo():
    """Initialise un repository Git"""
    if os.path.exists(".git"):
        print("✅ Repository Git déjà initialisé")
        return True
    
    try:
        subprocess.run(["git", "init"], check=True)
        print("✅ Repository Git initialisé")
        return True
    except subprocess.CalledProcessError:
        print("❌ Erreur lors de l'initialisation Git")
        return False

def create_github_repo():
    """Guide pour créer un repository GitHub"""
    print("\n📋 Étapes pour créer le repository GitHub :")
    print("1. Aller sur https://github.com")
    print("2. Cliquer sur 'New repository'")
    print("3. Nom : 'budget-dashboard-mobile'")
    print("4. Description : 'Dashboard Budget Personnel Mobile'")
    print("5. Cocher 'Add a README file'")
    print("6. Cliquer sur 'Create repository'")
    print("\n📋 Ensuite, exécutez ces commandes :")
    print("git remote add origin https://github.com/VOTRE-USERNAME/budget-dashboard-mobile.git")
    print("git add .")
    print("git commit -m 'Initial commit: Dashboard Budget Mobile'")
    print("git push -u origin main")

def deploy_streamlit():
    """Guide pour déployer sur Streamlit Cloud"""
    print("\n🚀 Étapes pour déployer sur Streamlit Cloud :")
    print("1. Aller sur https://share.streamlit.io")
    print("2. Se connecter avec GitHub")
    print("3. Cliquer sur 'New app'")
    print("4. Remplir :")
    print("   - Repository : votre-username/budget-dashboard-mobile")
    print("   - Branch : main")
    print("   - Main file path : dashboard_mobile.py")
    print("   - App URL : budget-dashboard-mobile")
    print("5. Cliquer sur 'Deploy!'")

def main():
    print("🚀 Assistant de Déploiement Streamlit Cloud")
    print("=" * 50)
    
    # Vérifier Git
    if not check_git():
        return
    
    # Initialiser Git
    if not init_git_repo():
        return
    
    # Créer .gitignore si nécessaire
    if not os.path.exists(".gitignore"):
        print("✅ Fichier .gitignore créé")
    
    # Créer config Streamlit si nécessaire
    if not os.path.exists(".streamlit/config.toml"):
        print("✅ Configuration Streamlit créée")
    
    print("\n📁 Fichiers prêts pour le déploiement :")
    print("✅ dashboard_mobile.py")
    print("✅ extract_all_transactions.py")
    print("✅ requirements.txt")
    print("✅ .gitignore")
    print("✅ .streamlit/config.toml")
    print("✅ README_STREAMLIT.md")
    
    # Guide GitHub
    create_github_repo()
    
    # Guide Streamlit
    deploy_streamlit()
    
    print("\n🎉 Votre dashboard sera accessible à :")
    print("https://budget-dashboard-mobile.streamlit.app")
    
    print("\n📱 Pour l'ajouter à l'écran d'accueil iOS :")
    print("1. Ouvrir Safari")
    print("2. Aller à l'URL de l'app")
    print("3. Partager → 'Ajouter à l'écran d'accueil'")
    print("4. Nommer 'Budget'")

if __name__ == "__main__":
    main()
