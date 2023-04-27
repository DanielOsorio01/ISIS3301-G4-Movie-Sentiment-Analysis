import pickle
from cleanText import cleanText
import joblib as jb

"""
CLase que contiene el modelo de prediccion, este modelo para que funcione
debe importar el modelo entrenado, el vectorizador utilizado en el pipeline
del modelo y la clase que usamos para llevar las palabras a su raiz y eliminar
las palabras que no aportan informacion al modelo (cleanText).
"""

class PredictionModel:
    # Constructor de la clase en el que se importa el modelo y el vectorizador, cleanText esta en los imports
    def __init__(self):
        self.model = pickle.load(open('./data/prediccion_reviews.pkl', 'rb'))
        self.vectorizer = jb.load('./data/count_vectorizer.pkl')
        
    # Metodo que se encarga de aplicar las transformaciones necesarias al texto de entrada y realiza la prediccion
    def make_prediction(self, data):
        result = self.model.predict(data)
        return result