import streamlit as st
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import plotly.express as px
from src.themes import load_css
from src.utils import load_data, render_sidebar

try:
    from wordcloud import WordCloud
    HAS_WORDCLOUD = True
except ImportError:
    HAS_WORDCLOUD = False

st.set_page_config(page_title="Text Insights - Duolingo Sentiment", page_icon="🔤", layout="wide")
load_css()
render_sidebar("🦉 Analisis Sentimen Duolingo")

st.title("🔤 Text Insights & WordCloud")
st.markdown("Visualisasi kata kunci paling sering muncul pada ulasan Positif, Netral, dan Negatif.")

df = load_data()

if not df.empty:
    target_col = 'final_clean_text' if 'final_clean_text' in df.columns else 'clean_text'

    tab1, tab2, tab3 = st.tabs(["🟢 Sentimen Positif", "🟡 Sentimen Netral", "🔴 Sentimen Negatif"])

    def generate_wordcloud_and_ngram(sentiment_type, color_theme, colormap_name):
        subset = df[df['sentiment'] == sentiment_type][target_col].dropna()
        text_data = " ".join(subset.astype(str))
        
        col_left, col_right = st.columns([1, 1])
        
        with col_left:
            st.subheader(f"☁️ WordCloud - {sentiment_type}")
            if text_data.strip():
                if HAS_WORDCLOUD:
                    wc = WordCloud(
                        width=800, 
                        height=500, 
                        background_color='#0f172a',
                        colormap=colormap_name,
                        max_words=100
                    ).generate(text_data)
                    
                    fig, ax = plt.subplots(figsize=(10, 6))
                    fig.patch.set_facecolor('#0f172a')
                    ax.imshow(wc, interpolation='bilinear')
                    ax.axis('off')
                    st.pyplot(fig)
                else:
                    st.warning("Library 'wordcloud' belum terinstall. Menggunakan alternatif visualisasi frekuensi kata.")
            else:
                st.info("Teks tidak cukup untuk generate WordCloud.")

        with col_right:
            st.subheader(f"📊 Top 15 Kata Terbanyak - {sentiment_type}")
            words = [word for text in subset.astype(str) for word in text.split() if len(word) > 2]
            most_common = Counter(words).most_common(15)
            
            freq_df = pd.DataFrame(most_common, columns=['Kata', 'Frekuensi'])
            
            fig_bar = px.bar(
                freq_df, 
                x='Frekuensi', 
                y='Kata', 
                orientation='h',
                color_discrete_sequence=[color_theme],
                text='Frekuensi'
            )
            fig_bar.update_layout(
                yaxis=dict(autorange="reversed"),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#cbd5e1')
            )
            st.plotly_chart(fig_bar, use_container_width=True)

    with tab1:
        generate_wordcloud_and_ngram("Positif", "#58CC02", "Greens")

    with tab2:
        generate_wordcloud_and_ngram("Netral", "#FFC800", "YlOrBr")

    with tab3:
        generate_wordcloud_and_ngram("Negatif", "#FF4B4B", "Reds")
