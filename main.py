import streamlit as st
from src.themes import load_css
from src.utils import load_data, render_metric_card, render_sidebar

# 1. Page Configuration
st.set_page_config(
    page_title="Duolingo Sentiment Analytics",
    page_icon="🦉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Load Custom Theme (Glassmorphism + Vibrant Duolingo Palette)
load_css()

# 3. Render Custom Sidebar Menu
render_sidebar("🦉 Analisis Sentimen Duolingo")

# 4. Main Hero Header Box
st.markdown("""
<div class="hero-box">
    <h1>🦉 Duolingo Sentiment Analytics</h1>
    <p class="hero-subtitle">
        Dashboard Analisis Sentimen Ulasan Play Store & Perbandingan Model Machine Learning (MLP, SimpleRNN, LSTM)
    </p>
</div>
""", unsafe_allow_html=True)

# Load Dataset
df = load_data()

if not df.empty:
    total_reviews = len(df)
    pos_count = (df['sentiment'] == 'Positif').sum()
    neu_count = (df['sentiment'] == 'Netral').sum()
    neg_count = (df['sentiment'] == 'Negatif').sum()

    # Metric Cards Top Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_metric_card("Total Ulasan", f"{total_reviews:,}", "Data Scraping Play Store", "#38bdf8")
    with col2:
        render_metric_card("Sentimen Positif", f"{(pos_count/total_reviews)*100:.1f}%", f"{pos_count:,} ulasan", "#58CC02")
    with col3:
        render_metric_card("Sentimen Netral", f"{(neu_count/total_reviews)*100:.1f}%", f"{neu_count:,} ulasan", "#FFC800")
    with col4:
        render_metric_card("Sentimen Negatif", f"{(neg_count/total_reviews)*100:.1f}%", f"{neg_count:,} ulasan", "#FF4B4B")

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🎯 Fitur & Navigasi Menu Dashboard")

# Navigation Showcase Grid (Clickable Cards)
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("""
    <a href="/overview" target="_self" style="text-decoration: none; color: inherit; display: block; height: 100%;">
        <div style="background: rgba(30, 41, 59, 0.6); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(88, 204, 2, 0.2); height: 100%; cursor: pointer;">
            <h3>📊 Overview & KPI</h3>
            <p>Ringkasan statistik ulasan, distribusi rating bintang, dan rasio kepuasan pengguna Duolingo.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <a href="/eda" target="_self" style="text-decoration: none; color: inherit; display: block; height: 100%;">
        <div style="background: rgba(30, 41, 59, 0.6); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(34, 211, 238, 0.2); height: 100%; cursor: pointer;">
            <h3>📈 Analisis EDA</h3>
            <p>Exploratory Data Analysis mendalam: Donut Chart, Korelasi Rating vs Sentimen, dan Tren Waktu.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_c:
    st.markdown("""
    <a href="/text_insights" target="_self" style="text-decoration: none; color: inherit; display: block; height: 100%;">
        <div style="background: rgba(30, 41, 59, 0.6); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(168, 85, 247, 0.2); height: 100%; cursor: pointer;">
            <h3>🔤 Text Insights</h3>
            <p>Visualisasi WordCloud interaktif per kategori sentimen dan analisis N-Gram kata kunci ulasan.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_d, col_e, col_f = st.columns(3)

with col_d:
    st.markdown("""
    <a href="/model_evaluation" target="_self" style="text-decoration: none; color: inherit; display: block; height: 100%;">
        <div style="background: rgba(30, 41, 59, 0.6); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(88, 204, 2, 0.2); height: 100%; cursor: pointer;">
            <h3>🤖 Perbandingan Model</h3>
            <p>Evaluasi & perbandingan metrik akurasi, F1-Score, dan Confusion Matrix model MLP, SimpleRNN, dan LSTM.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_e:
    st.markdown("""
    <a href="/live_prediction" target="_self" style="text-decoration: none; color: inherit; display: block; height: 100%;">
        <div style="background: rgba(30, 41, 59, 0.6); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(34, 211, 238, 0.2); height: 100%; cursor: pointer;">
            <h3>🧪 Live Prediction</h3>
            <p>Uji coba masukan teks ulasan baru secara real-time untuk melihat hasil klasifikasi sentimen.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_f:
    st.markdown("""
    <a href="/data_explorer" target="_self" style="text-decoration: none; color: inherit; display: block; height: 100%;">
        <div style="background: rgba(30, 41, 59, 0.6); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(168, 85, 247, 0.2); height: 100%; cursor: pointer;">
            <h3>📑 Data Explorer</h3>
            <p>Jelajahi data ulasan mentah dan hasil preprocessing dengan fitur filter serta tombol export CSV.</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("🦉 Duolingo Sentiment Analysis Dashboard • Built with Streamlit & Plotly")
