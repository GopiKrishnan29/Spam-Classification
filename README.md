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

