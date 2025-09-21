#!/usr/bin/env python3
"""
Script pour créer des données d'exemple pour le déploiement Streamlit Cloud
"""

import pandas as pd
from datetime import datetime, timedelta

def create_sample_data():
    """Crée des données d'exemple pour le dashboard"""
    
    # Créer des données d'exemple réalistes
    descriptions = [
        'Virement salaire OLAQIN', 'Achat CB FRANPRIX', 'Prélèvement NEONESS',
        'Virement remboursement DGFIP', 'Achat CB restaurant', 'Prélèvement électricité',
        'Virement prime', 'Achat CB transport', 'Prélèvement téléphone',
        'Virement bonus', 'Achat CB pharmacie', 'Prélèvement internet',
        'Virement freelance', 'Achat CB vêtements', 'Prélèvement assurance auto',
        'Virement dividende', 'Achat CB essence', 'Prélèvement mutuelle',
        'Virement remboursement', 'Achat CB loisirs', 'Prélèvement crédit',
        'Virement prime', 'Achat CB alimentation', 'Prélèvement gaz',
        'Virement bonus', 'Achat CB culture', 'Prélèvement assurance habitation',
        'Virement freelance', 'Achat CB santé', 'Prélèvement épargne',
        'Virement salaire', 'Achat CB supermarché', 'Prélèvement assurance',
        'Virement remboursement', 'Achat CB restaurant', 'Prélèvement électricité',
        'Virement prime', 'Achat CB transport', 'Prélèvement téléphone',
        'Virement bonus', 'Achat CB pharmacie', 'Prélèvement internet',
        'Virement freelance', 'Achat CB vêtements', 'Prélèvement assurance auto',
        'Virement dividende', 'Achat CB essence', 'Prélèvement mutuelle'
    ]
    
    amounts = [
        2500, -45.50, -89.90, 150, -23.80, -67.20, 300, -12.50, -35.40,
        500, -18.70, -42.10, 800, -156.30, -125.60, 75, -58.90, -78.20,
        200, -34.50, -89.10, 400, -67.80, -45.30, 600, -23.40, -56.70,
        900, -89.20, -34.60, 2500, -45.50, -89.90, 150, -23.80, -67.20,
        300, -12.50, -35.40, 500, -18.70, -42.10, 800, -156.30, -125.60,
        75, -58.90, -78.20, 200, -34.50
    ]
    
    # Répéter les listes pour avoir 50 éléments
    descriptions = descriptions * 2
    amounts = amounts * 2
    
    sample_data = {
        'date': pd.date_range('2025-07-01', periods=50, freq='D'),
        'description': descriptions[:50],
        'amount': amounts[:50],
        'source_file': ['exemple.pdf'] * 50
    }
    
    df = pd.DataFrame(sample_data)
    
    # Sauvegarder
    df.to_csv('transactions_complete.csv', index=False, encoding='utf-8')
    print("✅ Données d'exemple créées dans transactions_complete.csv")
    print(f"📊 {len(df)} transactions créées")
    print(f"💰 Revenus : {df[df['amount'] > 0]['amount'].sum():,.2f} €")
    print(f"💸 Dépenses : {df[df['amount'] < 0]['amount'].sum():,.2f} €")
    print(f"⚖️ Solde net : {df['amount'].sum():,.2f} €")

if __name__ == "__main__":
    create_sample_data()
