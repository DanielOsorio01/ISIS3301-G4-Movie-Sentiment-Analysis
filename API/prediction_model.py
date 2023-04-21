import pickle
from cleanText import cleanText
import joblib as jb

class PredictionModel:
    def __init__(self):
        self.model = pickle.load(open('./data/model.pkl', 'rb'))
        self.vectorizer = jb.load('./data/count_vectorizer.pkl')
        
    def make_prediction(self, data):
        result = self.model.predict(data)
        return result