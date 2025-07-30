# 📨 SMS Spam Classifier

An interactive and minimal web app built with **Streamlit** to classify SMS messages as **Spam** or **Ham (Not Spam)** using **Machine Learning** and **Natural Language Processing (NLP)**.

---

## 🚀 Features

- 🔘 **Model Selection** – Toggle between `Naive Bayes` and `Random Forest`
- 🌗 **Theme Switcher** – Choose between Light and Dark mode
- 📝 **User Input** – Type or paste SMS text to classify
- ✅ **Prediction Display** – Clear result with emojis and color indicators
- 💬 **Real-time Feedback** – Instantly shows if the message is spam or safe

---

## 🧠 How It Works

This app uses a simple yet effective NLP pipeline:

- 📚 **Dataset**: [UCI SMSSpamCollection](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- 🧹 **Preprocessing**: Lowercase, remove punctuation, stopwords, etc.
- 📊 **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- 🧠 **Models Used**:
  - `Multinomial Naive Bayes`
  - `Random Forest`
- 🌐 **UI/UX**: Built with Streamlit, styled for clarity and accessibility

⚠️ **Note**:  
This model is trained on a **basic dataset** and performs best on common spam patterns like:
- "WIN CASH"
- "Get ₹5000 now"
- "Free offers"

It may not detect subtle or modern spam variations.

---

## 🗂 Folder Structure

<pre> Spam-Classifier-App/ │ ├── <b>app/</b> # Streamlit app logic │ ├── __init__.py │ ├── config.py # Theme colors and model paths │ └── utils.py # Theme styler and result displayer │ ├── <b>model/</b> # Model training and saved models │ ├── __init__.py │ ├── train_model.py # Train and save NB + RF │ ├── spam_nb.pkl # Naive Bayes model │ └── spam_rf.pkl # Random Forest model │ ├── <b>preprocess/</b> # Text cleaning logic │ ├── __init__.py │ └── text_cleaner.py # clean_text() function used before predict │ ├── <b>vectorizer/</b> # Vectorization for feature extraction │ ├── __init__.py │ └── tfidf.pkl # TF-IDF vectorizer used by both models │ ├── <b>data/</b> # Dataset directory │ └── SMSSpamCollection # UCI dataset (original file) │ ├── <b>streamlit_app.py</b> # Entry point to launch the app ├── <b>requirements.txt</b> # All dependencies (streamlit, sklearn, etc.) └── <b>README.md</b> # Project documentation (this file) </pre>
