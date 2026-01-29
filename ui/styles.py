import streamlit as st

def load_styles():
    st.markdown("""
    <style>
    /* ---------- APP BACKGROUND ---------- */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #F9FAFB;
    }

    /* ---------- HEADINGS ---------- */
    h1, h2, h3 {
        color: #E0F2FE !important;
        font-weight: 700;
    }

    /* ---------- TEXT ---------- */
    p, label {
        color: #F9FAFB !important;
    }

    /* ---------- INPUTS ---------- */
    textarea, input {
        background-color: #111827 !important;
        color: #F9FAFB !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 8px !important;
    }

    textarea::placeholder,
    input::placeholder {
        color: #9CA3AF !important;
    }

    /* ---------- SELECTBOX (IMPORTANT FIX) ---------- */
    div[data-baseweb="select"] > div {
        background-color: #111827 !important;
        color: #F9FAFB !important;
        border: 1px solid #38BDF8 !important;
        border-radius: 8px !important;
    }

    /* Dropdown options */
    ul[role="listbox"] li {
        background-color: #111827 !important;
        color: #F9FAFB !important;
    }

    ul[role="listbox"] li:hover {
        background-color: #1f2937 !important;
        color: #F9FAFB !important;
    }

    /* ---------- BUTTON ---------- */
    .stButton > button {
        background: linear-gradient(90deg, #38BDF8, #6366F1);
        color: #ffffff !important;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6em 1.4em;
        border: none;
    }

    .stButton > button:hover {
        opacity: 0.9;
    }

    /* ---------- TEXT AREA OUTPUT ---------- */
    .stTextArea textarea {
        font-family: Consolas, monospace;
        font-size: 14px;
    }

    /* ---------- REMOVE STREAMLIT FOOTER ---------- */
    footer {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)
