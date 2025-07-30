# app/config.py

# Theme settings
LIGHT_THEME = {
    "backgroundColor": "#ffffff",
    "textColor": "#000000"
}

DARK_THEME = {
    "backgroundColor": "#0E1117",
    "textColor": "#FAFAFA"
}

DEFAULT_THEME = LIGHT_THEME

# Model and vectorizer paths
MODEL_PATH_NB = "model/spam_nb.pkl"
MODEL_PATH_RF = "model/spam_rf.pkl"
VECTORIZER_PATH = "vectorizer/tfidf.pkl"

