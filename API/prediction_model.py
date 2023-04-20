import pickle
import joblib as jb

class PredictionModel:
    def __init__(self):
        self.model = pickle.load(open('modelo_1.pkl', 'rb'))
        
    def make_prediction(self, data):
        result = self.model.predict(data)
        return result