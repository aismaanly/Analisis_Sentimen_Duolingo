import streamlit as st
import pandas as pd
from src.themes import load_css
from src.utils import load_data, render_sidebar

st.set_page_config(page_title="Data Explorer - Duolingo Sentiment", page_icon="📑", layout="wide")
load_css()
render_sidebar("🦉 Analisis Sentimen Duolingo")

st.title("📑 Data Explorer & Export")
st.markdown("Penjelajah dataset ulasan Duolingo dengan fitur pencarian teks, filter multi-kolom, dan unduh data.")

df = load_data()

if not df.empty:
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown("### 🔍 Filter Data Explorer")
    
    # Filter Sentimen
    sentiments = st.sidebar.multiselect(
        "Filter Sentimen:",
        options=['Positif', 'Netral', 'Negatif'],
        default=['Positif', 'Netral', 'Negatif']
    )
    
    # Filter Score Rating
    scores = st.sidebar.multiselect(
        "Filter Rating Bintang (1-5):",
        options=[1, 2, 3, 4, 5],
        default=[1, 2, 3, 4, 5]
    )
    
    # Keyword Search
    search_term = st.sidebar.text_input("🔍 Cari Kata Kunci di Ulasan:", "")
    
    # Apply Filters
    filtered = df[df['sentiment'].isin(sentiments) & df['score'].isin(scores)]
    
    if search_term.strip():
        filtered = filtered[filtered['content'].astype(str).str.contains(search_term, case=False, na=False)]
        
    st.markdown(f"**Menampilkan `{len(filtered):,}` dari `{len(df):,}` total ulasan**")
    
    # Select columns to display
    display_cols = ['content', 'score', 'sentiment']
    if 'final_clean_text' in df.columns:
        display_cols.append('final_clean_text')
        
    st.dataframe(
        filtered[display_cols],
        use_container_width=True,
        height=500
    )
    
    # Download Button
    csv_data = filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Unduh Data Hasil Filter (CSV)",
        data=csv_data,
        file_name="duolingo_filtered_reviews.csv",
        mime="text/csv",
        use_container_width=True
    )
