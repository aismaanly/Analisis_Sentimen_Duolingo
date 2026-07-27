import os
import re
import pandas as pd
import streamlit as st

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "processed_review.csv")
RAW_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "duolingo_review.csv")

@st.cache_data
def load_data():
    """
    Memuat dataset processed_review.csv dengan caching Streamlit untuk performa cepat.
    Menambahkan kolom sentiment berdasarkan nilai score rating.
    """
    if not os.path.exists(DATA_PATH):
        st.error(f"File data tidak ditemukan di path: {DATA_PATH}")
        return pd.DataFrame()
    
    df = pd.read_csv(DATA_PATH)
    
    # Mapping sentimen berdasarkan score rating jika belum ada kolom sentiment
    if 'sentiment' not in df.columns:
        def get_sentiment(score):
            if score >= 4:
                return 'Positif'
            elif score == 3:
                return 'Netral'
            else:
                return 'Negatif'
        
        df['sentiment'] = df['score'].apply(get_sentiment)
        
    return df

@st.cache_data
def load_raw_data():
    """
    Memuat data mentah ulasan jika tersedia.
    """
    if os.path.exists(RAW_DATA_PATH):
        return pd.read_csv(RAW_DATA_PATH)
    return pd.DataFrame()

def render_metric_card(title, value, subtitle="", value_color="#58CC02"):
    """
    Renders custom HTML metric card dengan efek Glassmorphism.
    """
    html = f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value" style="color: {value_color};">{value}</div>
        <div class="metric-subtitle">{subtitle}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_sidebar(title="🦉 Analisis Sentimen Duolingo"):
    """
    Renders single clean custom sidebar navigation.
    """
    with st.sidebar:
        st.markdown(f"## {title}")
        st.markdown("<div style='margin-bottom: 1.2rem;'></div>", unsafe_allow_html=True)
        pages = [
            ("🏠 Main Dashboard", "main.py"),
            ("📊 Overview & KPI", "pages/overview.py"),
            ("📈 EDA & Distribusi", "pages/eda.py"),
            ("🔤 Text Insights", "pages/text_insights.py"),
            ("🤖 Evaluasi Model", "pages/model_evaluation.py"),
            ("🧪 Live Prediction", "pages/live_prediction.py"),
            ("📑 Data Explorer", "pages/data_explorer.py"),
        ]
        
        for page_name, page_file in pages:
            st.page_link(page_file, label=page_name)

def preprocess_text(text):
    """
    Fungsi sederhana untuk cleaning teks ulasan baru pada live prediction.
    """
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.strip()
    return text
