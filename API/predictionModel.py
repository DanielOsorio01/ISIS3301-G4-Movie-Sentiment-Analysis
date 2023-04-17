from joblib import load

class Model:

    def __init__(self,columns):
        self.model = load("../modelo.jolib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result
