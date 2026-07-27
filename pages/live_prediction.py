import streamlit as st
import pandas as pd
import plotly.express as px
from src.themes import load_css
from src.utils import preprocess_text, render_sidebar

st.set_page_config(page_title="Live Prediction - Duolingo Sentiment", page_icon="🧪", layout="wide")
load_css()
render_sidebar("🦉 Analisis Sentimen Duolingo")

st.title("🧪 Live Sentiment Prediction")
st.markdown("Uji coba masukan teks ulasan baru secara real-time untuk memprediksi sentimen (Positif, Netral, Negatif).")

col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.subheader("✍️ Input Teks Ulasan Pengguna")
    
    sample_texts = [
        "Aplikasi ini sangat membantu saya belajar bahasa Jepang dari nol, fitur streak bikin semangat!",
        "Fitur baterai baru ini parah banget, cepat habis dan bikin malas belajar!",
        "Update barunya biasa saja, ada beberapa bug tapi masih bisa digunakan.",
        "Suka banget sama Duolingo gratis dan tanpa iklan sama sekali!"
    ]
    
    selected_sample = st.selectbox("Atau pilih contoh ulasan:", ["-- Ketik Sendiri --"] + sample_texts)
    
    default_text = "" if selected_sample == "-- Ketik Sendiri --" else selected_sample
    
    user_input = st.text_area("Masukkan teks ulasan Duolingo:", value=default_text, height=140, placeholder="Contoh: Fitur nyawa baru ini bikin belajar bahasa jadi susah...")
    
    btn_predict = st.button("🔮 Prediksi Sentimen", use_container_width=True)

if btn_predict and user_input.strip():
    cleaned = preprocess_text(user_input)
    
    # Mock inference logic based on keywords for demonstration
    pos_keywords = ['bagus', 'suka', 'keren', 'membantu', 'semangat', 'mantap', 'terbaik', 'gratis', 'seru', 'bantu']
    neg_keywords = ['parah', 'buruk', 'jelek', 'kecewa', 'sulit', 'susah', 'rugi', 'habis', 'benci', 'bug', 'crash', 'ngeselin', 'gagal']
    
    pos_score = sum(1 for w in pos_keywords if w in cleaned)
    neg_score = sum(1 for w in neg_keywords if w in cleaned)
    
    if pos_score > neg_score:
        sentiment_res = "Positif"
        confidence = min(0.65 + (pos_score * 0.1), 0.96)
        color = "#58CC02"
        badge_class = "badge-positive"
    elif neg_score > pos_score:
        sentiment_res = "Negatif"
        confidence = min(0.65 + (neg_score * 0.1), 0.95)
        color = "#FF4B4B"
        badge_class = "badge-negative"
    else:
        sentiment_res = "Netral"
        confidence = 0.72
        color = "#FFC800"
        badge_class = "badge-neutral"
        
    probs = {
        "Positif": confidence if sentiment_res == "Positif" else (1 - confidence) / 2,
        "Netral": confidence if sentiment_res == "Netral" else (1 - confidence) / 2,
        "Negatif": confidence if sentiment_res == "Negatif" else (1 - confidence) / 2
    }
    
    # Normalize
    total_p = sum(probs.values())
    probs = {k: v / total_p for k, v in probs.items()}

    with col_right:
        st.subheader("🎯 Hasil Prediksi Model")
        
        st.markdown(f"""
        <div style="background: rgba(30, 41, 59, 0.8); padding: 1.5rem; border-radius: 16px; border: 1px solid {color}; text-align: center;">
            <p style="font-size: 1rem; color: #94a3b8; margin-bottom: 0.5rem;">HASIL KLASIFIKASI</p>
            <h2 style="color: {color} !important; border: none; font-size: 2.2rem !important; margin: 0;">
                <span class="{badge_class}">{sentiment_res.upper()}</span>
            </h2>
            <p style="font-size: 1.1rem; color: #e2e8f0; margin-top: 0.8rem;">
                Tingkat Kepercayaan: <b>{probs[sentiment_res]*100:.1f}%</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📊 Distribusi Probabilitas Sentimen")
        
        prob_df = pd.DataFrame([{"Sentimen": k, "Probabilitas (%)": round(v*100, 1)} for k, v in probs.items()])
        
        fig_p = px.bar(
            prob_df,
            x="Probabilitas (%)",
            y="Sentimen",
            orientation="h",
            text="Probabilitas (%)",
            color="Sentimen",
            color_discrete_map={'Positif': '#58CC02', 'Netral': '#FFC800', 'Negatif': '#FF4B4B'}
        )
        fig_p.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#cbd5e1'),
            xaxis=dict(range=[0, 100]),
            showlegend=False
        )
        st.plotly_chart(fig_p, use_container_width=True)

        with st.expander("🔍 Pipeline Preprocessing Teks"):
            st.write("**Teks Asli:**", user_input)
            st.write("**Hasil Preprocessing (Clean):**", cleaned)
