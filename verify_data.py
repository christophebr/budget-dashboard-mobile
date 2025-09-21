import pandas as pd

def verify_transactions():
    """Vérifie que les données extraites sont correctes"""
    try:
        df = pd.read_csv("transactions_complete.csv")
        df['date'] = pd.to_datetime(df['date'])
        
        print("🔍 Vérification des données extraites")
        print("=" * 50)
        
        # Vérifier qu'il n'y a pas de soldes dans les transactions
        solde_transactions = df[df['description'].str.contains('solde', case=False, na=False)]
        if len(solde_transactions) > 0:
            print("❌ PROBLÈME : Des soldes sont encore présents dans les transactions :")
            print(solde_transactions[['date', 'description', 'amount']])
        else:
            print("✅ Aucun solde trouvé dans les transactions (correct)")
        
        # Statistiques
        print(f"\n📊 Statistiques :")
        print(f"Total transactions : {len(df)}")
        print(f"Période : {df['date'].min().strftime('%d/%m/%Y')} - {df['date'].max().strftime('%d/%m/%Y')}")
        
        # Revenus et dépenses
        revenus = df[df['amount'] > 0]['amount'].sum()
        depenses = df[df['amount'] < 0]['amount'].sum()
        solde_net = df['amount'].sum()
        
        print(f"Total revenus : {revenus:,.2f} €")
        print(f"Total dépenses : {depenses:,.2f} €")
        print(f"Solde net : {solde_net:,.2f} €")
        
        # Vérifier les types de transactions
        print(f"\n🏷️ Types de transactions :")
        types = df['description'].str.extract(r'^([A-Z\s]+)')[0].value_counts()
        print(types.head(10))
        
        # Vérifier les montants négatifs (dépenses)
        print(f"\n💸 Top 10 des dépenses :")
        top_depenses = df[df['amount'] < 0].nlargest(10, 'amount')
        for idx, row in top_depenses.iterrows():
            print(f"  {row['date'].strftime('%d/%m/%Y')} : {row['description'][:50]}... - {row['amount']:,.2f} €")
        
        # Vérifier les montants positifs (revenus)
        print(f"\n💰 Top 10 des revenus :")
        top_revenus = df[df['amount'] > 0].nlargest(10, 'amount')
        for idx, row in top_revenus.iterrows():
            print(f"  {row['date'].strftime('%d/%m/%Y')} : {row['description'][:50]}... + {row['amount']:,.2f} €")
        
        print(f"\n✅ Vérification terminée !")
        
    except FileNotFoundError:
        print("❌ Fichier transactions_complete.csv non trouvé")
    except Exception as e:
        print(f"❌ Erreur lors de la vérification : {e}")

if __name__ == "__main__":
    verify_transactions()
