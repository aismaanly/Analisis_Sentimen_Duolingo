import streamlit as st
import plotly.express as px
from src.themes import load_css
from src.utils import load_data, render_metric_card, render_sidebar

st.set_page_config(page_title="Overview - Duolingo Sentiment", page_icon="📊", layout="wide")
load_css()
render_sidebar("🦉 Analisis Sentimen Duolingo")

st.title("📊 Overview & Ringkasan KPI")
st.markdown("Ringkasan statistik ulasan pengguna aplikasi Duolingo di Google Play Store.")

df = load_data()

if df.empty:
    st.warning("Data tidak tersedia. Pastikan dataset telah diproses.")
else:
    total_reviews = len(df)
    pos_count = (df['sentiment'] == 'Positif').sum()
    neu_count = (df['sentiment'] == 'Netral').sum()
    neg_count = (df['sentiment'] == 'Negatif').sum()
    avg_rating = df['score'].mean()

    # Metric Cards Top Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_metric_card("Total Ulasan", f"{total_reviews:,}", "Dataset Scraping", "#38bdf8")
    with col2:
        render_metric_card("Rata-Rata Rating", f"{avg_rating:.2f} / 5.0", "Skala 1 - 5 Bintang", "#58CC02")
    with col3:
        render_metric_card("Ulasan Positif", f"{pos_count:,}", f"{(pos_count/total_reviews)*100:.1f}% dari total", "#58CC02")
    with col4:
        render_metric_card("Ulasan Negatif", f"{neg_count:,}", f"{(neg_count/total_reviews)*100:.1f}% dari total", "#FF4B4B")

    st.markdown("<br>", unsafe_allow_html=True)

    col_chart1, col_chart2 = st.columns([1, 1])

    with col_chart1:
        st.subheader("🍩 Rasio Sentimen Pengguna")
        sentiment_counts = df['sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['Sentimen', 'Jumlah']
        
        color_map = {'Positif': '#58CC02', 'Netral': '#FFC800', 'Negatif': '#FF4B4B'}
        
        fig_donut = px.pie(
            sentiment_counts, 
            values='Jumlah', 
            names='Sentimen', 
            hole=0.5,
            color='Sentimen',
            color_discrete_map=color_map
        )
        fig_donut.update_traces(textinfo='percent+label', marker=dict(line=dict(color='#0f172a', width=2)))
        fig_donut.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    with col_chart2:
        st.subheader("⭐ Distribusi Rating Bintang (1 - 5)")
        rating_counts = df['score'].value_counts().sort_index().reset_index()
        rating_counts.columns = ['Rating', 'Jumlah']
        
        fig_rating = px.bar(
            rating_counts, 
            x='Rating', 
            y='Jumlah',
            text='Jumlah',
            color='Rating',
            color_continuous_scale=['#FF4B4B', '#FF8C00', '#FFC800', '#78C800', '#58CC02']
        )
        fig_rating.update_traces(textposition='outside')
        fig_rating.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            xaxis=dict(tickmode='linear', tick0=1, dtick=1),
            showlegend=False
        )
        st.plotly_chart(fig_rating, use_container_width=True)
