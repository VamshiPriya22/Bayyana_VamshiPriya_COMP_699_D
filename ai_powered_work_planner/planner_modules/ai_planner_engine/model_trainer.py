import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

MODEL_PATH = "ml_models/workload_model.pkl"


class ModelTrainer:

    @staticmethod
    def train_model():
        # Dummy training dataset (can replace with real later)
        X = np.array([
            [10, 1, 2, 0],
            [20, 2, 1, 1],
            [40, 3, 0.5, 2],
            [60, 4, 0.2, 3]
        ])

        y = np.array([0, 1, 2, 3])  # workload score

        model = RandomForestRegressor()
        model.fit(X, y)

        os.makedirs("ml_models", exist_ok=True)
        joblib.dump(model, MODEL_PATH)

        return "Model trained successfully"