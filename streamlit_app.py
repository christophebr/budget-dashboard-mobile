import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os

# Configuration de la page
st.set_page_config(
    page_title="💰 Budget Mobile",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS pour mobile
st.markdown("""
<style>
    .main > div { padding-top: 1rem; }
    .stMetric { background-color: #f0f2f6; padding: 1rem; border-radius: 0.5rem; margin: 0.5rem 0; }
    .stSelectbox > div > div { font-size: 16px; }
    .stDateInput > div > div { font-size: 16px; }
    .stTextInput > div > div > input { font-size: 16px; }
    .stButton > button { width: 100%; height: 3rem; font-size: 16px; }
    @media (max-width: 768px) { .stSidebar { display: none; } }
</style>
""", unsafe_allow_html=True)

# Titre
st.title("💰 Budget Personnel")
st.markdown("---")

# Créer des données d'exemple
def create_sample_data():
    """Crée des données d'exemple pour la démonstration"""
    sample_data = {
        'date': pd.date_range('2025-07-01', periods=30, freq='D'),
        'description': [
            'Virement salaire', 'Achat CB supermarché', 'Prélèvement assurance',
            'Virement remboursement', 'Achat CB restaurant', 'Prélèvement électricité',
            'Virement prime', 'Achat CB transport', 'Prélèvement téléphone',
            'Virement bonus', 'Achat CB pharmacie', 'Prélèvement internet',
            'Virement freelance', 'Achat CB vêtements', 'Prélèvement assurance auto',
            'Virement dividende', 'Achat CB essence', 'Prélèvement mutuelle',
            'Virement remboursement', 'Achat CB loisirs', 'Prélèvement crédit',
            'Virement prime', 'Achat CB alimentation', 'Prélèvement gaz',
            'Virement bonus', 'Achat CB culture', 'Prélèvement assurance habitation',
            'Virement freelance', 'Achat CB santé', 'Prélèvement épargne'
        ],
        'amount': [
            2500, -45.50, -89.90, 150, -23.80, -67.20, 300, -12.50, -35.40,
            500, -18.70, -42.10, 800, -156.30, -125.60, 75, -58.90, -78.20,
            200, -34.50, -89.10, 400, -67.80, -45.30, 600, -23.40, -56.70,
            900, -89.20, -34.60
        ],
        'source_file': ['exemple.pdf'] * 30
    }
    
    df = pd.DataFrame(sample_data)
    df['date'] = pd.to_datetime(df['date'])
    return df

# Charger les données
@st.cache_data
def load_data():
    """Charge les données depuis le fichier CSV ou crée des données d'exemple"""
    try:
        # Essayer de charger le fichier CSV
        df = pd.read_csv("transactions_complete.csv")
        df['date'] = pd.to_datetime(df['date'])
        return df
    except FileNotFoundError:
        # Créer des données d'exemple si le fichier n'existe pas
        st.warning("⚠️ Fichier de données non trouvé. Affichage de données d'exemple.")
        return create_sample_data()

# Charger les données
df = load_data()

if df is not None and not df.empty:
    # Filtres
    st.subheader("🔍 Filtres")
    
    col1, col2 = st.columns(2)
    
    with col1:
        min_date = df['date'].min().date()
        max_date = df['date'].max().date()
        date_range = st.date_input(
            "Période",
            value=(min_date, max_date),
            min_value=min_date,
            max_date=max_date
        )
    
    with col2:
        sources = ['Tous'] + list(df['source_file'].unique())
        selected_source = st.selectbox("Fichier source", sources)
    
    # Appliquer les filtres
    filtered_df = df.copy()
    
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df['date'].dt.date >= start_date) & 
            (filtered_df['date'].dt.date <= end_date)
        ]
    
    if selected_source != 'Tous':
        filtered_df = filtered_df[filtered_df['source_file'] == selected_source]
    
    # Métriques
    st.subheader("📊 Résumé")
    
    col1, col2 = st.columns(2)
    
    with col1:
        total_income = filtered_df[filtered_df['amount'] > 0]['amount'].sum()
        st.metric("💰 Revenus", f"{total_income:,.0f} €")
    
    with col2:
        total_expenses = filtered_df[filtered_df['amount'] < 0]['amount'].sum()
        st.metric("💸 Dépenses", f"{total_expenses:,.0f} €")
    
    net_balance = filtered_df['amount'].sum()
    st.metric("⚖️ Solde Net", f"{net_balance:,.0f} €")
    
    st.info("ℹ️ Les soldes de compte ne sont pas comptés comme des revenus ou dépenses.")
    
    st.markdown("---")
    
    # Graphique simple avec matplotlib au lieu de plotly
    st.subheader("📈 Évolution du Solde")
    
    filtered_df_sorted = filtered_df.sort_values('date')
    filtered_df_sorted['cumulative_balance'] = filtered_df_sorted['amount'].cumsum()
    
    # Utiliser st.line_chart au lieu de plotly
    chart_data = filtered_df_sorted.set_index('date')['cumulative_balance']
    st.line_chart(chart_data)
    
    # Répartition simple
    st.subheader("📊 Répartition des Montants")
    
    # Créer des catégories de montants
    filtered_df['amount_category'] = pd.cut(
        filtered_df['amount'], 
        bins=[-float('inf'), -100, -10, 0, 10, 100, float('inf')],
        labels=['< -100€', '-100€ à -10€', '-10€ à 0€', '0€ à 10€', '10€ à 100€', '> 100€']
    )
    
    category_counts = filtered_df['amount_category'].value_counts()
    
    # Utiliser st.bar_chart au lieu de plotly
    st.bar_chart(category_counts)
    
    # Transactions
    st.subheader("📋 Transactions Récentes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        show_income_only = st.checkbox("Revenus uniquement")
        show_expenses_only = st.checkbox("Dépenses uniquement")
    
    with col2:
        search_term = st.text_input("Rechercher", placeholder="Description...")
    
    # Appliquer les filtres
    display_df = filtered_df.copy()
    
    if show_income_only:
        display_df = display_df[display_df['amount'] > 0]
    
    if show_expenses_only:
        display_df = display_df[display_df['amount'] < 0]
    
    if search_term:
        display_df = display_df[display_df['description'].str.contains(search_term, case=False, na=False)]
    
    # Afficher les transactions
    if not display_df.empty:
        display_df_formatted = display_df.copy()
        display_df_formatted['date'] = display_df_formatted['date'].dt.strftime('%d/%m')
        display_df_formatted['amount'] = display_df_formatted['amount'].apply(lambda x: f"{x:+.0f} €")
        
        st.dataframe(
            display_df_formatted[['date', 'description', 'amount']].head(20),
            use_container_width=True,
            height=400
        )
        
        # Export
        csv = display_df.to_csv(index=False, encoding='utf-8')
        st.download_button(
            label="📥 Télécharger les données (CSV)",
            data=csv,
            file_name=f"transactions_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("Aucune transaction ne correspond aux critères sélectionnés.")
    
    # Statistiques
    with st.expander("📊 Statistiques Rapides"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Top 3 Dépenses:**")
            top_depenses = filtered_df[filtered_df['amount'] < 0].nsmallest(3, 'amount')
            for idx, row in top_depenses.iterrows():
                st.write(f"• {row['description'][:30]}... - {row['amount']:,.0f} €")
        
        with col2:
            st.write("**Top 3 Revenus:**")
            top_revenus = filtered_df[filtered_df['amount'] > 0].nlargest(3, 'amount')
            for idx, row in top_revenus.iterrows():
                st.write(f"• {row['description'][:30]}... + {row['amount']:,.0f} €")
    
    # Instructions
    if 'exemple.pdf' in df['source_file'].values:
        st.info("""
        **📁 Pour utiliser vos vraies données :**
        
        1. Placez vos relevés PDF dans le dossier `releve/`
        2. Exécutez : `python extract_all_transactions.py`
        3. Le fichier `transactions_complete.csv` sera créé
        4. Rechargez cette page pour voir vos données
        """)
    
else:
    st.error("Aucune donnée disponible.")

# Footer
st.markdown("---")
st.markdown("💡 *Dashboard Mobile - Optimisé pour iOS/Android*")