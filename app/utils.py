# app/utils.py

import streamlit as st

def set_theme(theme_config):
    """Apply background and text styles for consistent visibility."""
    st.markdown(f"""
        <style>
            .stApp {{
                background-color: {theme_config['backgroundColor']};
                color: {theme_config['textColor']};
            }}
            textarea, input, select, .stButton > button,
            .stTextInput > div > div > input,
            .stTextArea textarea, .stRadio > div {{
                background-color: {theme_config['backgroundColor']} !important;
                color: {theme_config['textColor']} !important;
                border: 1px solid #999 !important;
            }}
            label, div, span {{
                color: {theme_config['textColor']} !important;
            }}
        </style>
    """, unsafe_allow_html=True)

def display_result(prediction):
    """Display result with emoji and color."""
    if prediction == 1:
        st.error("🚨 SPAM Message Detected!", icon="❌")
    else:
        st.success("✅ This is a HAM (Safe) Message", icon="✅")


