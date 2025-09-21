import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os

# Configuration de la page pour mobile
st.set_page_config(
    page_title="💰 Budget Mobile",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"  # Sidebar fermée par défaut sur mobile
)

# CSS pour optimiser l'affichage mobile
st.markdown("""
<style>
    .main > div {
        padding-top: 1rem;
    }
    
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    
    .stSelectbox > div > div {
        font-size: 16px; /* Évite le zoom sur iOS */
    }
    
    .stDateInput > div > div {
        font-size: 16px;
    }
    
    .stTextInput > div > div > input {
        font-size: 16px;
    }
    
    /* Optimiser les graphiques pour mobile */
    .js-plotly-plot {
        width: 100% !important;
    }
    
    /* Boutons plus grands pour le tactile */
    .stButton > button {
        width: 100%;
        height: 3rem;
        font-size: 16px;
    }
    
    /* Masquer les éléments non essentiels sur mobile */
    @media (max-width: 768px) {
        .stSidebar {
            display: none;
        }
    }
</style>
""", unsafe_allow_html=True)

# Titre principal
st.title("💰 Budget Personnel")
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
    # Filtres mobiles (en haut de page)
    st.subheader("🔍 Filtres")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Filtre par période
        min_date = df['date'].min().date()
        max_date = df['date'].max().date()
        
        date_range = st.date_input(
            "Période",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            key="mobile_date_filter"
        )
    
    with col2:
        # Filtre par source
        sources = ['Tous'] + list(df['source_file'].unique())
        selected_source = st.selectbox("Fichier source", sources, key="mobile_source_filter")
    
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
    
    # Métriques principales (optimisées pour mobile)
    st.subheader("📊 Résumé")
    
    col1, col2 = st.columns(2)
    
    with col1:
        total_income = filtered_df[filtered_df['amount'] > 0]['amount'].sum()
        st.metric("💰 Revenus", f"{total_income:,.0f} €")
    
    with col2:
        total_expenses = filtered_df[filtered_df['amount'] < 0]['amount'].sum()
        st.metric("💸 Dépenses", f"{total_expenses:,.0f} €")
    
    # Solde net (pleine largeur)
    net_balance = filtered_df['amount'].sum()
    st.metric("⚖️ Solde Net", f"{net_balance:,.0f} €")
    
    # Note sur les soldes
    st.info("ℹ️ Les soldes de compte ne sont pas comptés comme des revenus ou dépenses.")
    
    st.markdown("---")
    
    # Graphiques optimisés pour mobile
    st.subheader("📈 Évolution du Solde")
    
    # Calculer le solde cumulé
    filtered_df_sorted = filtered_df.sort_values('date')
    filtered_df_sorted['cumulative_balance'] = filtered_df_sorted['amount'].cumsum()
    
    fig_balance = px.line(
        filtered_df_sorted, 
        x='date', 
        y='cumulative_balance',
        title="Évolution du solde",
        labels={'cumulative_balance': 'Solde (€)', 'date': 'Date'},
        height=300  # Hauteur réduite pour mobile
    )
    fig_balance.update_layout(
        font_size=12,
        title_font_size=16,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_balance, use_container_width=True)
    
    # Répartition des montants
    st.subheader("📊 Répartition des Montants")
    
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
        title="Répartition par catégorie",
        height=300
    )
    fig_pie.update_layout(
        font_size=12,
        title_font_size=16,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Transactions récentes (tableau simplifié)
    st.subheader("📋 Transactions Récentes")
    
    # Options d'affichage
    col1, col2 = st.columns(2)
    
    with col1:
        show_income_only = st.checkbox("Revenus uniquement", key="mobile_income_filter")
        show_expenses_only = st.checkbox("Dépenses uniquement", key="mobile_expenses_filter")
    
    with col2:
        search_term = st.text_input("Rechercher", key="mobile_search", placeholder="Description...")
    
    # Appliquer les filtres supplémentaires
    display_df = filtered_df.copy()
    
    if show_income_only:
        display_df = display_df[display_df['amount'] > 0]
    
    if show_expenses_only:
        display_df = display_df[display_df['amount'] < 0]
    
    if search_term:
        display_df = display_df[display_df['description'].str.contains(search_term, case=False, na=False)]
    
    # Afficher les 20 dernières transactions
    if not display_df.empty:
        display_df_formatted = display_df.copy()
        display_df_formatted['date'] = display_df_formatted['date'].dt.strftime('%d/%m')
        display_df_formatted['amount'] = display_df_formatted['amount'].apply(lambda x: f"{x:+.0f} €")
        
        # Afficher seulement les colonnes essentielles
        st.dataframe(
            display_df_formatted[['date', 'description', 'amount']].head(20),
            use_container_width=True,
            height=400
        )
        
        # Bouton de téléchargement
        csv = display_df.to_csv(index=False, encoding='utf-8')
        st.download_button(
            label="📥 Télécharger les données (CSV)",
            data=csv,
            file_name=f"transactions_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("Aucune transaction ne correspond aux critères sélectionnés.")
    
    # Statistiques rapides
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
    
else:
    st.error("Aucune donnée disponible. Veuillez d'abord exécuter le script d'extraction des PDFs.")
    
    st.info("""
    **Instructions pour utiliser le dashboard mobile:**
    
    1. Placez vos relevés de compte PDF dans le dossier `releve/`
    2. Exécutez le script d'extraction: `python extract_all_transactions.py`
    3. Rechargez cette page pour voir vos données
    """)

# Footer
st.markdown("---")
st.markdown("💡 *Dashboard Mobile - Optimisé pour iOS/Android*")
