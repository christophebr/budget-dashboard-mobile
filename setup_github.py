#!/usr/bin/env python3
"""
Script pour configurer GitHub et déployer sur Streamlit Cloud
"""

import subprocess
import sys
import webbrowser

def check_git_status():
    """Vérifie le statut Git"""
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Repository Git prêt")
            return True
        else:
            print("❌ Problème avec Git")
            return False
    except Exception as e:
        print(f"❌ Erreur Git: {e}")
        return False

def create_github_repo():
    """Ouvre GitHub pour créer un repository"""
    print("\n🌐 Ouverture de GitHub...")
    webbrowser.open("https://github.com/new")
    
    print("\n📋 Instructions pour créer le repository :")
    print("1. Nom du repository : budget-dashboard-mobile")
    print("2. Description : Dashboard Budget Personnel Mobile")
    print("3. Visibilité : Public (gratuit)")
    print("4. NE PAS cocher 'Add a README file' (on en a déjà un)")
    print("5. Cliquer sur 'Create repository'")
    print("\n⏳ Attendez que la page se charge...")

def get_github_url():
    """Demande l'URL du repository GitHub"""
    print("\n📝 Une fois le repository créé, copiez l'URL HTTPS")
    print("Exemple : https://github.com/votre-username/budget-dashboard-mobile.git")
    
    github_url = input("\n🔗 Collez l'URL de votre repository GitHub : ").strip()
    
    if not github_url.startswith("https://github.com/") or not github_url.endswith(".git"):
        print("❌ URL invalide. Format attendu : https://github.com/username/repo.git")
        return None
    
    return github_url

def setup_remote_and_push(github_url):
    """Configure le remote et pousse le code"""
    try:
        # Ajouter le remote
        print(f"\n🔗 Ajout du remote GitHub...")
        subprocess.run(["git", "remote", "add", "origin", github_url], check=True)
        print("✅ Remote ajouté")
        
        # Pousser le code
        print(f"\n📤 Poussée du code vers GitHub...")
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("✅ Code poussé vers GitHub")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la poussée : {e}")
        return False

def deploy_streamlit():
    """Ouvre Streamlit Cloud pour le déploiement"""
    print("\n🚀 Ouverture de Streamlit Cloud...")
    webbrowser.open("https://share.streamlit.io")
    
    print("\n📋 Instructions pour déployer :")
    print("1. Se connecter avec GitHub")
    print("2. Cliquer sur 'New app'")
    print("3. Remplir :")
    print("   - Repository : votre-username/budget-dashboard-mobile")
    print("   - Branch : main")
    print("   - Main file path : dashboard_mobile.py")
    print("   - App URL : budget-dashboard-mobile")
    print("4. Cliquer sur 'Deploy!'")

def main():
    print("🚀 Configuration GitHub et Déploiement Streamlit")
    print("=" * 60)
    
    # Vérifier Git
    if not check_git_status():
        return
    
    print("✅ Tous les fichiers sont prêts pour GitHub")
    
    # Créer le repository GitHub
    create_github_repo()
    
    input("\n⏸️ Appuyez sur Entrée quand vous avez créé le repository...")
    
    # Demander l'URL GitHub
    github_url = get_github_url()
    if not github_url:
        return
    
    # Configurer et pousser
    if setup_remote_and_push(github_url):
        print("\n🎉 Code poussé vers GitHub avec succès !")
        
        # Déployer sur Streamlit
        deploy_streamlit()
        
        print("\n📱 Une fois déployé, votre app sera accessible à :")
        print("https://budget-dashboard-mobile.streamlit.app")
        
        print("\n📱 Pour l'ajouter à l'écran d'accueil iOS :")
        print("1. Ouvrir Safari")
        print("2. Aller à l'URL de l'app")
        print("3. Partager → 'Ajouter à l'écran d'accueil'")
        print("4. Nommer 'Budget'")
    else:
        print("\n❌ Erreur lors de la configuration GitHub")

if __name__ == "__main__":
    main()
