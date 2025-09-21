#!/usr/bin/env python3
"""
Script de lancement du dashboard mobile
"""

import subprocess
import sys
import os

def main():
    print("📱 Lancement du Dashboard Budget Mobile")
    print("=" * 50)
    
    # Vérifier si le fichier CSV existe
    if not os.path.exists("transactions_complete.csv"):
        print("📄 Fichier CSV non trouvé. Extraction des données depuis les PDFs...")
        try:
            subprocess.run([sys.executable, "extract_all_transactions.py"], check=True)
            print("✅ Extraction terminée!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'extraction: {e}")
            return
        except FileNotFoundError:
            print("❌ Script d'extraction non trouvé.")
            return
    else:
        print("✅ Fichier CSV trouvé!")
    
    # Lancer le dashboard mobile
    print("\n📱 Lancement du dashboard mobile...")
    print("Le dashboard sera accessible à l'adresse: http://localhost:8501")
    print("Pour mobile: http://192.168.1.155:8501 (remplacez par votre IP)")
    print("Appuyez sur Ctrl+C pour arrêter le serveur")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "dashboard_mobile.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Dashboard mobile arrêté par l'utilisateur")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du lancement du dashboard: {e}")
    except FileNotFoundError:
        print("❌ Streamlit non trouvé. Veuillez installer les dépendances avec: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
