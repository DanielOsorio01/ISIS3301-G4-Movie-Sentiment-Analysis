import nltk
nltk.download('stopwords')
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import pandas as pd
from nltk.stem import SnowballStemmer

class cleanText(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.stop_words = set(stopwords.words('spanish'))
        self.stop_words = list(self.stop_words)
        self.stop_words.extend([u'.', u'[', ']', u',', u';', u'', u')', u'),', u' ', u'('])
        self.snowball_stemmer = SnowballStemmer('spanish')

    def fit (self, X, y=None):
        return self
    
    def transform(self, X):
        return self.clean(X)
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df["review_es"] = df["review_es"].apply(lambda x: ' '.join([
            self.snowball_stemmer.stem(word.lower())
            for word in wordpunct_tokenize(x) 
            if (word.isalpha() and word.lower() not in self.stop_words)
            ]))
        return df
