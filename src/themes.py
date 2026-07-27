import streamlit as st

def load_css():
    """
    Injeksi CSS kustom dengan gaya Glassmorphism modern dan skema warna Vibrant Duolingo,
    terinspirasi dari arsitektur tema RAGsume (https://github.com/aismaanly/RAGsume).
    """
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        
        * {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        /* Gradient background untuk halaman utama */
        .stApp {
            background: linear-gradient(135deg, #0b1329 0%, #0f172a 40%, #062016 100%);
            background-attachment: fixed;
            color: #f1f5f9;
        }

        /* Container utama bergaya Glassmorphism */
        .block-container {
            background: rgba(15, 23, 42, 0.75);
            border-radius: 24px;
            padding: 2.5rem !important;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(88, 204, 2, 0.25);
            margin-top: 1.5rem;
            margin-bottom: 2rem;
        }

        /* Title utama dengan gradient Duolingo Green & Cyan */
        h1 {
            background: linear-gradient(135deg, #58CC02 0%, #22d3ee 50%, #a855f7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.8rem !important;
            font-weight: 800 !important;
            letter-spacing: -0.02em;
            margin-bottom: 0.8rem;
        }

        h2 {
            color: #f8fafc !important;
            border-bottom: 2px solid rgba(88, 204, 2, 0.4);
            padding-bottom: 0.5rem;
            font-weight: 700 !important;
            margin-top: 1.5rem;
        }

        h3 {
            color: #e2e8f0 !important;
            font-weight: 600 !important;
        }

        p, span, label, div {
            color: #cbd5e1;
        }

        /* Sidebar Glassmorphism */
        section[data-testid="stSidebar"] {
            background-color: rgba(11, 19, 41, 0.85) !important;
            border-right: 1px solid rgba(88, 204, 2, 0.2) !important;
            backdrop-filter: blur(20px);
        }

        /* Metric Cards Kustom */
        .metric-card {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.9) 100%);
            border-radius: 16px;
            padding: 1.25rem 1.5rem;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
            border-color: rgba(88, 204, 2, 0.5);
        }

        .metric-title {
            font-size: 0.875rem;
            font-weight: 600;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.25rem;
        }

        .metric-value {
            font-size: 2rem;
            font-weight: 800;
            color: #58CC02;
        }

        .metric-subtitle {
            font-size: 0.8rem;
            color: #64748b;
            margin-top: 0.25rem;
        }

        /* Badge Sentimen */
        .badge-positive {
            background-color: rgba(88, 204, 2, 0.2);
            color: #58CC02;
            border: 1px solid #58CC02;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-weight: 700;
        }

        .badge-neutral {
            background-color: rgba(255, 200, 0, 0.2);
            color: #FFC800;
            border: 1px solid #FFC800;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-weight: 700;
        }

        .badge-negative {
            background-color: rgba(255, 75, 75, 0.2);
            color: #FF4B4B;
            border: 1px solid #FF4B4B;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-weight: 700;
        }

        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: rgba(15, 23, 42, 0.6);
            padding: 0.4rem;
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: 10px;
            color: #94a3b8;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border: none;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, rgba(88, 204, 2, 0.25) 0%, rgba(34, 211, 238, 0.2) 100%) !important;
            color: #58CC02 !important;
            border: 1px solid rgba(88, 204, 2, 0.4) !important;
        }

        /* Button Styling */
        .stButton > button {
            background: linear-gradient(135deg, #58CC02 0%, #209602 100%);
            color: #ffffff;
            font-weight: 700;
            border: none;
            border-radius: 12px;
            padding: 0.6rem 1.5rem;
            box-shadow: 0 4px 15px rgba(88, 204, 2, 0.3);
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(88, 204, 2, 0.5);
            background: linear-gradient(135deg, #61e002 0%, #25a802 100%);
        }

        /* Header Hero Box */
        .hero-box {
            background: linear-gradient(135deg, rgba(88, 204, 2, 0.1) 0%, rgba(14, 165, 233, 0.1) 100%);
            border: 1px solid rgba(88, 204, 2, 0.3);
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            margin-bottom: 2rem;
        }

        .hero-subtitle {
            font-size: 1.15rem;
            color: #cbd5e1;
            font-weight: 500;
        }
    </style>
    """, unsafe_allow_html=True)
