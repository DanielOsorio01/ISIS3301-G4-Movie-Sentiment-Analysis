from cleanText import cleanText
import joblib as jb
import pandas as pd

"""
CLase que contiene el modelo de prediccion, este modelo para que funcione
debe importar el modelo entrenado, el vectorizador utilizado en el pipeline
del modelo y la clase que usamos para llevar las palabras a su raiz y eliminar
las palabras que no aportan informacion al modelo (cleanText).
"""

def make_prediction(data):
    model = jb.load(open('./data/prediccion_reviews.pkl', 'rb'))
    data = [data]
    data = pd.DataFrame({"review_es": data})
    result = model.predict(data["review_es"])
    return result