import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(135deg,#0B1120,#111827,#1E293B);
        color:white;
    }

    section[data-testid="stSidebar"]{
        background:#111827;
    }

    section[data-testid="stSidebar"] *{
        color:white !important;
    }

    div[data-testid="stMetric"]{
        background:#1E293B;
        border:1px solid #334155;
        border-radius:18px;
        padding:18px;
        box-shadow:0 0 15px rgba(0,200,255,.15);
    }

    div[data-testid="stMetric"]:hover{
        border:1px solid #38BDF8;
        transform:scale(1.02);
    }

    /* Metric Label */
    div[data-testid="stMetricLabel"]{
        color:#E2E8F0 !important;
        font-size:16px;
        font-weight:600;
    }

    /* Metric Value */
    div[data-testid="stMetricValue"]{
        color:white !important;
        font-size:34px;
        font-weight:bold;
    }

    h1,h2,h3{
        color:white !important;
    }

    p{
        color:#CBD5E1 !important;
    }

    .stButton>button{
        background:#0EA5E9;
        color:white;
        border:none;
        border-radius:12px;
        font-weight:bold;
    }

    .stButton>button:hover{
        background:#0284C7;
        color:white;
    }

    hr{
        border-color:#334155;
    }

    </style>
    """, unsafe_allow_html=True)