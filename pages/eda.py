import streamlit as st
import pandas as pd
import plotly.express as px
from src.themes import load_css
from src.utils import load_data, render_sidebar

st.set_page_config(page_title="EDA - Duolingo Sentiment", page_icon="📈", layout="wide")
load_css()
render_sidebar("🦉 Analisis Sentimen Duolingo")

st.title("📈 Exploratory Data Analysis (EDA)")
st.markdown("Analisis mendalam hubungan antar variabel ulasan dan pola sentimen pengguna.")

df = load_data()

if not df.empty:
    # Sidebar Filters for EDA
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown("### 🔍 Filter Data EDA")
    selected_sentiment = st.sidebar.multiselect(
        "Pilih Kategori Sentimen:",
        options=['Positif', 'Netral', 'Negatif'],
        default=['Positif', 'Netral', 'Negatif']
    )
    
    filtered_df = df[df['sentiment'].isin(selected_sentiment)]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Cross-Tabulation Rating Star vs Sentimen")
        crosstab = pd.crosstab(filtered_df['score'], filtered_df['sentiment']).reset_index()
        
        color_map = {'Positif': '#58CC02', 'Netral': '#FFC800', 'Negatif': '#FF4B4B'}
        
        fig_cross = px.bar(
            crosstab,
            x='score',
            y=[col for col in ['Positif', 'Netral', 'Negatif'] if col in crosstab.columns],
            title="Jumlah Sentimen per Tingkat Rating Bintang",
            labels={'score': 'Rating Star (1-5)', 'value': 'Jumlah Ulasan'},
            color_discrete_map=color_map,
            barmode='stack'
        )
        fig_cross.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            legend_title_text='Sentimen'
        )
        st.plotly_chart(fig_cross, use_container_width=True)

    with col2:
        st.subheader("📏 Distribusi Panjang Karakter Ulasan")
        filtered_df['char_length'] = filtered_df['content'].astype(str).str.len()
        
        fig_hist = px.histogram(
            filtered_df[filtered_df['char_length'] <= 500],
            x='char_length',
            color='sentiment',
            nbins=40,
            title="Distribusi Panjang Karakter Ulasan (<= 500 Karakter)",
            color_discrete_map=color_map,
            opacity=0.75,
            barmode='overlay'
        )
        fig_hist.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            xaxis_title="Panjang Karakter",
            yaxis_title="Frekuensi Ulasan"
        )
        st.plotly_chart(fig_hist, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📌 Persentase Sentimen per Bintang Rating")

    perc_df = pd.crosstab(filtered_df['score'], filtered_df['sentiment'], normalize='index') * 100
    perc_df = perc_df.round(1).reset_index()

    fig_perc = px.bar(
        perc_df,
        x='score',
        y=[col for col in ['Positif', 'Netral', 'Negatif'] if col in perc_df.columns],
        title="Proporsi (%) Sentimen pada Tiap Rating Bintang",
        labels={'score': 'Rating Star', 'value': 'Persentase (%)'},
        color_discrete_map=color_map,
        barmode='relative'
    )
    fig_perc.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#cbd5e1')
    )
    st.plotly_chart(fig_perc, use_container_width=True)
