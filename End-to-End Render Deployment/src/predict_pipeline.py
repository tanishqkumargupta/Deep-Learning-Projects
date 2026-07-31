import pickle
import pandas as pd


class PredictPipeline:

    def __init__(self):
        with open("artifacts/model.pkl", "rb") as file:
            self.model = pickle.load(file)

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction