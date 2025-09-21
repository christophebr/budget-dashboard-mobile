import pandas as pd
import pdfplumber
import os
import re
from datetime import datetime
import glob

class CompleteTransactionExtractor:
    def __init__(self, pdf_folder="releve"):
        self.pdf_folder = pdf_folder
        self.extracted_data = []
    
    def extract_text_from_pdf(self, pdf_path):
        """Extrait le texte de toutes les pages d'un PDF"""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                all_text = ""
                for page_num, page in enumerate(pdf.pages):
                    page_text = page.extract_text()
                    if page_text:
                        all_text += f"\n--- PAGE {page_num + 1} ---\n"
                        all_text += page_text + "\n"
                return all_text
        except Exception as e:
            print(f"Erreur lors de l'extraction du PDF {pdf_path}: {e}")
            return ""
    
    def clean_text(self, text):
        """Nettoie le texte extrait"""
        # Remplacer les caractères spéciaux
        text = text.replace('(cid:128)', '€')
        text = text.replace('(cid:224)', 'à')
        text = text.replace('Ø', 'é')
        text = text.replace('(cid:176)', '°')
        text = text.replace('ß', 'û')
        text = text.replace('(cid:231)', 'ç')
        text = text.replace('(cid:146)', "'")
        return text
    
    def extract_transactions_from_pdf(self, pdf_path):
        """Extrait toutes les transactions d'un PDF en traitant toutes les pages"""
        text = self.extract_text_from_pdf(pdf_path)
        if not text:
            return []
        
        text = self.clean_text(text)
        lines = text.split('\n')
        
        transactions = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Ignorer les lignes de séparation de pages
            if line.startswith('--- PAGE'):
                continue
            
            # 1. Chercher les lignes de solde (ne pas les compter comme des transactions)
            solde_match = re.search(r'Ancien solde au (\d{1,2}/\d{1,2}/\d{2,4})\s+([+-]?\d{1,3}(?:\s?\d{3})*(?:,\d{2})?)', line)
            if solde_match:
                # Les soldes ne sont pas des transactions, on les ignore
                continue
            
            # 2. Chercher les transactions qui commencent par une date DD/MM
            date_match = re.search(r'^(\d{1,2}/\d{1,2})\s+(.+)', line)
            if date_match:
                date_part = date_match.group(1)
                rest_of_line = date_match.group(2).strip()
                
                # Construire la date complète (ajouter l'année)
                # Pour les relevés 2025, on assume que c'est 2025
                full_date = f"{date_part}/2025"
                
                # Chercher le montant dans la ligne
                amount_matches = re.findall(r'([+-]?\d{1,3}(?:\s?\d{3})*(?:,\d{2})?)', rest_of_line)
                amount = None
                
                if amount_matches:
                    # Prendre le dernier montant trouvé qui ressemble à un montant de transaction
                    for amt in reversed(amount_matches):
                        amt_clean = amt.replace(' ', '').replace(',', '.')
                        try:
                            amt_float = float(amt_clean)
                            # Vérifier que c'est un montant raisonnable pour une transaction
                            if 0.01 <= abs(amt_float) <= 10000:
                                amount = amt_float
                                break
                        except:
                            continue
                
                if not amount:
                    continue
                
                # La description est le reste de la ligne sans le montant
                description = rest_of_line
                if amount_matches:
                    # Enlever le dernier montant de la description
                    last_amount = amount_matches[-1]
                    description = re.sub(rf'\s*{re.escape(last_amount)}\s*$', '', description)
                
                description = description.strip()
                
                # Filtrer les lignes qui ne sont pas des transactions
                if any(keyword in description.lower() for keyword in ['relevé', 'découvert', 'frais', 'récapitulatif', 'seuil', 'page']):
                    continue
                
                # Déterminer si c'est un crédit ou débit
                # Les paiements par carte sont généralement des débits
                if any(keyword in description.lower() for keyword in ['paiement', 'carte', 'prélèvement', 'virement sortant']):
                    amount = -abs(amount)
                elif any(keyword in description.lower() for keyword in ['virement', 'crédit', 'remboursement']):
                    amount = abs(amount)
                else:
                    # Par défaut, considérer comme un débit si le montant est positif
                    amount = -abs(amount)
                
                transactions.append({
                    'date': full_date,
                    'description': description,
                    'amount': amount
                })
                continue
            
            # 3. Chercher les paiements par carte bancaire spécifiques
            cb_match = re.search(r'Paiement Carte Bancaire de (\d+,\d+) € du (\d{1,2}/\d{1,2})', line)
            if cb_match:
                amount_str = cb_match.group(1).replace(',', '.')
                date_part = cb_match.group(2)
                full_date = f"{date_part}/2025"
                try:
                    amount = -float(amount_str)  # Dépense
                    transactions.append({
                        'date': full_date,
                        'description': f'Paiement Carte Bancaire {cb_match.group(1)} €',
                        'amount': amount
                    })
                except:
                    pass
                continue
        
        return transactions
    
    def process_all_pdfs(self):
        """Traite tous les PDFs dans le dossier"""
        pdf_files = glob.glob(os.path.join(self.pdf_folder, "*.pdf"))
        
        for pdf_file in pdf_files:
            print(f"Traitement de {pdf_file}...")
            
            transactions = self.extract_transactions_from_pdf(pdf_file)
            
            # Ajouter le nom du fichier source
            for transaction in transactions:
                transaction['source_file'] = os.path.basename(pdf_file)
            
            self.extracted_data.extend(transactions)
            print(f"Extrait {len(transactions)} transactions de {pdf_file}")
    
    def save_to_csv(self, output_file="transactions_complete.csv"):
        """Sauvegarde les données extraites en CSV"""
        if not self.extracted_data:
            print("Aucune donnée à sauvegarder")
            return
        
        df = pd.DataFrame(self.extracted_data)
        
        # Nettoyer et formater les données
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        
        # Convertir les dates
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y', errors='coerce')
        
        # Supprimer les lignes avec des dates invalides
        df = df.dropna(subset=['date'])
        
        # Trier par date
        df = df.sort_values('date')
        
        # Sauvegarder
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Données sauvegardées dans {output_file}")
        print(f"Total: {len(df)} transactions")
        
        return df

def main():
    # Créer l'extracteur
    extractor = CompleteTransactionExtractor()
    
    # Traiter tous les PDFs
    extractor.process_all_pdfs()
    
    # Sauvegarder en CSV
    df = extractor.save_to_csv()
    
    if df is not None and not df.empty:
        print("\nAperçu des données extraites:")
        print(df.head(15))
        print(f"\nColonnes: {list(df.columns)}")
        print(f"Types de données:\n{df.dtypes}")
        
        # Statistiques de base
        print(f"\nStatistiques:")
        print(f"Période: {df['date'].min().strftime('%d/%m/%Y')} - {df['date'].max().strftime('%d/%m/%Y')}")
        print(f"Total des dépenses: {df[df['amount'] < 0]['amount'].sum():.2f} €")
        print(f"Total des revenus: {df[df['amount'] > 0]['amount'].sum():.2f} €")
        print(f"Solde net: {df['amount'].sum():.2f} €")
        
        # Afficher les transactions par fichier source
        print(f"\nTransactions par fichier:")
        for source in df['source_file'].unique():
            count = len(df[df['source_file'] == source])
            print(f"  {source}: {count} transactions")
    else:
        print("Aucune transaction extraite. Vérifiez le format de vos PDFs.")

if __name__ == "__main__":
    main()
