import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from preprocess.text_cleaner import clean_text

# Load dataset
df = pd.read_csv("data/SMSSpamCollection", sep='\t', names=['label', 'message'])

# Map labels
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})

# Clean messages
df['cleaned_message'] = df['message'].apply(clean_text)

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned_message'])
y = df['label_num']

# Save vectorizer
with open("vectorizer/tfidf.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train MultinomialNB
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

# Save NB model
with open("model/spam_nb.pkl", "wb") as f:
    pickle.dump(nb_model, f)

# Train RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Save RF model
with open("model/spam_rf.pkl", "wb") as f:
    pickle.dump(rf_model, f)

# Evaluate (optional)
nb_acc = accuracy_score(y_test, nb_model.predict(X_test))
rf_acc = accuracy_score(y_test, rf_model.predict(X_test))

print(f"Naive Bayes Accuracy: {nb_acc:.2f}")
print(f"Random Forest Accuracy: {rf_acc:.2f}")
