import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os

# Configuration de la page
st.set_page_config(
    page_title="Dashboard Budget Personnel",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre principal
st.title("💰 Dashboard Budget Personnel")
st.markdown("---")

# Charger les données
@st.cache_data
def load_data():
    """Charge les données depuis le fichier CSV"""
    try:
        df = pd.read_csv("transactions_complete.csv")
        df['date'] = pd.to_datetime(df['date'])
        return df
    except FileNotFoundError:
        st.error("Fichier transactions_complete.csv non trouvé. Veuillez d'abord exécuter le script d'extraction.")
        return None

# Charger les données
df = load_data()

if df is not None and not df.empty:
    # Sidebar pour les filtres
    st.sidebar.header("🔍 Filtres")
    
    # Filtre par période
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    
    date_range = st.sidebar.date_input(
        "Période",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Filtre par source
    sources = ['Tous'] + list(df['source_file'].unique())
    selected_source = st.sidebar.selectbox("Fichier source", sources)
    
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
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_transactions = len(filtered_df)
        st.metric("Total Transactions", total_transactions)
    
    with col2:
        total_income = filtered_df[filtered_df['amount'] > 0]['amount'].sum()
        st.metric("Total Revenus", f"{total_income:,.2f} €")
    
    with col3:
        total_expenses = filtered_df[filtered_df['amount'] < 0]['amount'].sum()
        st.metric("Total Dépenses", f"{total_expenses:,.2f} €")
    
    with col4:
        net_balance = filtered_df['amount'].sum()
        st.metric("Solde Net", f"{net_balance:,.2f} €")
    
    # Note sur les soldes
    st.info("ℹ️ **Note** : Les soldes de compte ne sont pas comptés comme des revenus ou dépenses. Ils représentent l'état du compte à une date donnée.")
    
    st.markdown("---")
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Évolution du Solde")
        
        # Calculer le solde cumulé
        filtered_df_sorted = filtered_df.sort_values('date')
        filtered_df_sorted['cumulative_balance'] = filtered_df_sorted['amount'].cumsum()
        
        fig_balance = px.line(
            filtered_df_sorted, 
            x='date', 
            y='cumulative_balance',
            title="Évolution du solde au fil du temps",
            labels={'cumulative_balance': 'Solde (€)', 'date': 'Date'}
        )
        fig_balance.update_layout(height=400)
        st.plotly_chart(fig_balance, use_container_width=True)
    
    with col2:
        st.subheader("📈 Répartition des Montants")
        
        # Créer des catégories de montants
        filtered_df['amount_category'] = pd.cut(
            filtered_df['amount'], 
            bins=[-float('inf'), -100, -10, 0, 10, 100, float('inf')],
            labels=['< -100€', '-100€ à -10€', '-10€ à 0€', '0€ à 10€', '10€ à 100€', '> 100€']
        )
        
        category_counts = filtered_df['amount_category'].value_counts()
        
        fig_pie = px.pie(
            values=category_counts.values,
            names=category_counts.index,
            title="Répartition par catégorie de montant"
        )
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Graphique des transactions par mois
    st.subheader("📅 Transactions par Mois")
    
    # Grouper par mois
    monthly_data = filtered_df.copy()
    monthly_data['month'] = monthly_data['date'].dt.to_period('M')
    monthly_summary = monthly_data.groupby('month').agg({
        'amount': ['sum', 'count'],
        'date': ['min', 'max']
    }).round(2)
    
    monthly_summary.columns = ['Montant Total', 'Nombre Transactions', 'Date Min', 'Date Max']
    monthly_summary = monthly_summary.reset_index()
    monthly_summary['month_str'] = monthly_summary['month'].astype(str)
    
    fig_monthly = px.bar(
        monthly_summary,
        x='month_str',
        y='Montant Total',
        title="Montant total par mois",
        labels={'month_str': 'Mois', 'Montant Total': 'Montant (€)'}
    )
    fig_monthly.update_layout(height=400)
    st.plotly_chart(fig_monthly, use_container_width=True)
    
    # Tableau des transactions
    st.subheader("📋 Détail des Transactions")
    
    # Options d'affichage
    col1, col2 = st.columns([1, 3])
    
    with col1:
        show_income_only = st.checkbox("Revenus uniquement")
        show_expenses_only = st.checkbox("Dépenses uniquement")
    
    with col2:
        search_term = st.text_input("Rechercher dans les descriptions", "")
    
    # Appliquer les filtres supplémentaires
    display_df = filtered_df.copy()
    
    if show_income_only:
        display_df = display_df[display_df['amount'] > 0]
    
    if show_expenses_only:
        display_df = display_df[display_df['amount'] < 0]
    
    if search_term:
        display_df = display_df[display_df['description'].str.contains(search_term, case=False, na=False)]
    
    # Afficher le tableau
    if not display_df.empty:
        # Formater les colonnes pour l'affichage
        display_df_formatted = display_df.copy()
        display_df_formatted['date'] = display_df_formatted['date'].dt.strftime('%d/%m/%Y')
        display_df_formatted['amount'] = display_df_formatted['amount'].apply(lambda x: f"{x:,.2f} €")
        
        st.dataframe(
            display_df_formatted[['date', 'description', 'amount', 'source_file']],
            use_container_width=True,
            height=400
        )
        
        # Bouton de téléchargement
        csv = display_df.to_csv(index=False, encoding='utf-8')
        st.download_button(
            label="📥 Télécharger les données filtrées (CSV)",
            data=csv,
            file_name=f"transactions_filtrees_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
    else:
        st.info("Aucune transaction ne correspond aux critères sélectionnés.")
    
    # Statistiques avancées
    with st.expander("📊 Statistiques Avancées"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Top 5 des plus grosses transactions:**")
            top_transactions = filtered_df.nlargest(5, 'amount')[['date', 'description', 'amount']]
            for idx, row in top_transactions.iterrows():
                st.write(f"• {row['date'].strftime('%d/%m/%Y')}: {row['description'][:50]}... - {row['amount']:,.2f} €")
        
        with col2:
            st.write("**Top 5 des plus petites transactions:**")
            bottom_transactions = filtered_df.nsmallest(5, 'amount')[['date', 'description', 'amount']]
            for idx, row in bottom_transactions.iterrows():
                st.write(f"• {row['date'].strftime('%d/%m/%Y')}: {row['description'][:50]}... - {row['amount']:,.2f} €")
    
else:
    st.error("Aucune donnée disponible. Veuillez d'abord exécuter le script d'extraction des PDFs.")
    
    st.info("""
    **Instructions pour utiliser le dashboard:**
    
    1. Placez vos relevés de compte PDF dans le dossier `releve/`
    2. Exécutez le script d'extraction: `python extract_pdf_simple.py`
    3. Rechargez cette page pour voir vos données
    """)

# Footer
st.markdown("---")
st.markdown("💡 *Dashboard créé avec Streamlit - Données extraites automatiquement depuis vos relevés PDF*")
