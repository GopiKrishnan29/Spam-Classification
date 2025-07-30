import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    """
    Cleans the input text by performing lowercasing, removal of non-alphanumeric
    characters, stopword removal, and stemming.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove email addresses, URLs, and non-alphanumeric characters
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # Tokenize
    words = text.split()

    # Remove stopwords and apply stemming
    filtered = [stemmer.stem(word) for word in words if word not in stop_words]

    # Return cleaned text
    return ' '.join(filtered)