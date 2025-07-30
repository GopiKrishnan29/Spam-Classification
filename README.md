\# 📨 SMS Spam Classifier



A simple and interactive web app built with \*\*Streamlit\*\* to classify SMS messages as \*\*Spam\*\* or \*\*Ham (Not Spam)\*\* using \*\*Natural Language Processing (NLP)\*\*.



---



\## 🚀 Features



\- 🔘 \*\*Model Selection\*\*: Choose between `Naive Bayes` or `Random Forest` classifiers

\- 🌗 \*\*Theme Switcher\*\*: Light and Dark UI themes

\- ✏️ \*\*Text Input\*\*: Paste any SMS message

\- ✅ \*\*Instant Prediction\*\*: Classifies as `Spam` or `Ham`

\- 😄 \*\*Emoji Feedback\*\*: Clear visual output using icons and colors



---



\## 🧠 How it Works



This project uses a basic NLP pipeline:

\- Data: \[`SMSSpamCollection`](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection) from UCI

\- Preprocessing: Lowercase, remove punctuation, stopwords etc.

\- Vectorization: TF-IDF

\- Models: `Multinomial Naive Bayes` and `Random Forest`

\- UI: Built using `Streamlit`



⚠️ \*\*Note\*\*: This model is trained only on basic examples and performs best on messages containing clear indicators like money, free offers, and promotions (e.g. "WIN CASH NOW", "You’ve won ₹5000").



---



\## 📦 Folder Structure



Spam-Classifier-App/

│

├── app/

│ ├── utils.py # Theme styling + result display

│ └── config.py # Theme configs and model paths

│

├── model/

│ ├── train\_model.py # Model training and saving

│ ├── spam\_nb.pkl # Naive Bayes model

│ └── spam\_rf.pkl # Random Forest model

│

├── preprocess/

│ └── text\_cleaner.py # Preprocessing logic

│

├── vectorizer/

│ └── tfidf.pkl # TF-IDF vectorizer

│

├── data/

│ └── SMSSpamCollection # Original dataset

│

├── streamlit\_app.py # Entry point for Streamlit

├── requirements.txt # Dependencies

└── README.md # You're here!

❗ Limitations:

	-Trained on a basic dataset, this model is ideal for educational/demo purposes only.

	-May not detect advanced or subtle spam messages.

	-Accuracy can vary for informal or conversational texts.

