import re
from nltk.stem import PorterStemmer

# Custom stopwords
stopwords = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
    'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
    'to', 'was', 'were', 'will', 'with', 'you', 'your', 'this', 'but',
    'or', 'if', 'they', 'i', 'we', 'us', 'not', 'do', 'can'
}

# Stemmer
stemmer = PorterStemmer()

# Preprocessing function
def preprocess_text_custom(text):
    text = text.lower()
    text = re.sub(r"^subject:", "", text)
    text = re.sub(r"\d+", " num ", text)  # Replace digits with "num"
    text = re.sub(r"[^a-z\s]", "", text)  # Remove punctuation
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stopwords]
    return " ".join(words)
