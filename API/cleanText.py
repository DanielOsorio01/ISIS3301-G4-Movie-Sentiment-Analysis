import nltk
nltk.download('stopwords')
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import pandas as pd
from nltk.stem import SnowballStemmer

"""
Clase que se encarga de hacer la limpieza del texto, llevando las palabras a su raiz
y eliminando las palabras que no aportan informacion al modelo antes de ser vectorizado.
"""
class cleanText(BaseEstimator, TransformerMixin):
    # Constructor de la clase que inicializa las variables necesarias para la limpieza
    def __init__(self):
        # Define las palabras que no aportan informacion al modelo, en este caso las stopwords en espaniol
        self.stop_words = set(stopwords.words('spanish'))
        self.stop_words = list(self.stop_words)
        # Agrega algunas palabras que no estan en las stopwords pero que tampoco aportan informacion
        self.stop_words.extend([u'.', u'[', ']', u',', u';', u'', u')', u'),', u' ', u'('])
        # Define el stemmer que se encarga de llevar las palabras a su raiz
        self.snowball_stemmer = SnowballStemmer('spanish')

    def fit (self, X, y=None):
        return self
    
    def transform(self, X):
        return self.clean(X)
    
    # Metodo que se encarga de aplicar las transformaciones necesarias al texto de entrada
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        # Elimina las palabras que no aportan informacion al modelo y las lleva a su raiz
        df["review_es"] = df["review_es"].apply(lambda x: ' '.join([
            self.snowball_stemmer.stem(word.lower())
            for word in wordpunct_tokenize(x) 
            if (word.isalpha() and word.lower() not in self.stop_words)
            ]))
        return df
