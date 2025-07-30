# app/main.py

import streamlit as st
import pickle
from preprocess.text_cleaner import clean_text
from app.utils import set_theme, display_result
from app.config import (
    LIGHT_THEME,
    DARK_THEME,
    MODEL_PATH_NB,
    MODEL_PATH_RF,
    VECTORIZER_PATH
)

# Page config
st.set_page_config(page_title="Spam Classifier", page_icon="📨")

# Sidebar: Theme & Model selection
st.sidebar.title("⚙️ Settings")
theme_choice = st.sidebar.radio("Choose Theme", ["Light", "Dark"])
model_choice = st.sidebar.radio("Choose Model", ["Naive Bayes", "Random Forest"])

# Apply selected theme
theme_config = LIGHT_THEME if theme_choice == "Light" else DARK_THEME
set_theme(theme_config)

# Load selected model
model_path = MODEL_PATH_NB if model_choice == "Naive Bayes" else MODEL_PATH_RF
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

# Title & Instructions
st.title("📨 SMS Spam Classifier")
st.markdown("#### Hey there! Put your SMS below to check whether it's spam or not...")

# Input box
message = st.text_area("✏️ Enter your message:")

# Predict button
if st.button("Predict"):
    if not message.strip():
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(message)
        transformed = vectorizer.transform([cleaned])
        prediction = model.predict(transformed)[0]
        display_result(prediction)
