import pandas as pd
from sklearn.model_selection import train_test_split

datafull= pd.read_csv('Final.csv',delimiter=';')
datafull_set= pd.DataFrame(data=datafull)

X, y = datafull_set['Title'], datafull_set['Category']
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0,test_size=0.25)
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("punkt")
nltk.download("stopwords")

def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("spanish"))
    filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words]
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    return " ".join(stemmed_tokens)

X_preprocessed = [preprocess_text(text) for text in X_train]

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_transformed = vectorizer.fit_transform(X_preprocessed)

from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()
classifier.fit(X_transformed, y_train)




X_test_preprocessed = [preprocess_text(text) for text in X_test]
X_test_transformed = vectorizer.transform(X_test_preprocessed)

y_pred = classifier.predict(X_test_transformed)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

test='data quality analyst'


X_preprocessed = [preprocess_text(test)]
X_transformed = vectorizer.transform(X_preprocessed)
predic=classifier.predict(X_transformed)

print(predic)