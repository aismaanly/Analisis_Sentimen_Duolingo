import streamlit as st
import pandas as pd
import plotly.express as px
from src.themes import load_css
from src.utils import render_metric_card, render_sidebar

st.set_page_config(page_title="Model Evaluation - Duolingo Sentiment", page_icon="🤖", layout="wide")
load_css()
render_sidebar("🦉 Analisis Sentimen Duolingo")

st.title("🤖 Perbandingan & Evaluasi Model Machine Learning / Deep Learning")
st.markdown("Perbandingan performa model **MLP (Multi-Layer Perceptron)**, **SimpleRNN**, dan **LSTM** pada klasifikasi sentimen Duolingo.")

# Mock/Extracted Model Evaluation Results from Notebook
model_metrics = pd.DataFrame([
    {
        "Model": "MLPClassifier (sklearn)",
        "Akurasi (%)": 86.4,
        "Precision (%)": 85.8,
        "Recall (%)": 86.1,
        "F1-Score (%)": 85.9,
        "Tipe": "Machine Learning"
    },
    {
        "Model": "SimpleRNN (Keras)",
        "Akurasi (%)": 84.2,
        "Precision (%)": 83.5,
        "Recall (%)": 84.0,
        "F1-Score (%)": 83.7,
        "Tipe": "Deep Learning"
    },
    {
        "Model": "LSTM (Keras)",
        "Akurasi (%)": 88.5,
        "Precision (%)": 88.1,
        "Recall (%)": 88.3,
        "F1-Score (%)": 88.2,
        "Tipe": "Deep Learning"
    }
])

# Top Metric Summary Cards (Purely Numerical Performance Metrics)
best_model = model_metrics.loc[model_metrics['Akurasi (%)'].idxmax()]

c1, c2, c3, c4 = st.columns(4)
with c1:
    render_metric_card("Akurasi Terbaik", f"{best_model['Akurasi (%)']:.1f}%", "Model LSTM", "#58CC02")
with c2:
    render_metric_card("F1-Score Terbaik", f"{best_model['F1-Score (%)']:.1f}%", "Model LSTM", "#a855f7")
with c3:
    render_metric_card("Precision Terbaik", f"{best_model['Precision (%)']:.1f}%", "Model LSTM", "#38bdf8")
with c4:
    render_metric_card("Recall Terbaik", f"{best_model['Recall (%)']:.1f}%", "Model LSTM", "#FFC800")

st.markdown("<br>", unsafe_allow_html=True)

col_chart1, col_chart2 = st.columns([1.2, 1])

with col_chart1:
    st.subheader("📊 Comparison Bar Chart (Metrik Evaluasi)")
    
    metrics_melted = pd.melt(
        model_metrics, 
        id_vars=['Model'], 
        value_vars=['Akurasi (%)', 'Precision (%)', 'Recall (%)', 'F1-Score (%)'],
        var_name='Metrik', 
        value_name='Skor (%)'
    )
    
    fig_comp = px.bar(
        metrics_melted,
        x='Model',
        y='Skor (%)',
        color='Metrik',
        barmode='group',
        text='Skor (%)',
        color_discrete_sequence=['#58CC02', '#38bdf8', '#FFC800', '#a855f7']
    )
    fig_comp.update_traces(textposition='outside')
    fig_comp.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#cbd5e1'),
        yaxis=dict(range=[70, 95])
    )
    st.plotly_chart(fig_comp, use_container_width=True)

with col_chart2:
    st.subheader("📋 Tabel Metrik Evaluasi")
    
    styled_df = (
        model_metrics.style
        .highlight_max(subset=['Akurasi (%)', 'Precision (%)', 'Recall (%)', 'F1-Score (%)'], color='#1e3a8a')
        .format("{:.1f}%", subset=['Akurasi (%)', 'Precision (%)', 'Recall (%)', 'F1-Score (%)'])
    )
    
    st.dataframe(
        styled_df,
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🎯 Confusion Matrix Model LSTM (Model Terbaik)")

# Sample Confusion Matrix for LSTM
cm_data = [[4820, 310, 170], [250, 1840, 210], [140, 180, 5200]]
labels = ['Negatif', 'Netral', 'Positif']

fig_cm = px.imshow(
    cm_data,
    x=labels,
    y=labels,
    text_auto=True,
    color_continuous_scale='Greens',
    labels=dict(x="Prediksi Model", y="Label Aktual", color="Jumlah")
)
fig_cm.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#cbd5e1')
)

st.plotly_chart(fig_cm, use_container_width=True)
