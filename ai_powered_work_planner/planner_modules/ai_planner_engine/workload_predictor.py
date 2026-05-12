import numpy as np
import joblib
import os


MODEL_PATH = "ml_models/workload_model.pkl"


class WorkloadPredictor:

    def __init__(self):
        if os.path.exists(MODEL_PATH):
            try:
                self.model = joblib.load(MODEL_PATH)
                print("✅ ML Model Loaded")
            except Exception as e:
                print("❌ Model load error:", str(e))
                self.model = None
        else:
            print("⚠ Model file not found, using fallback logic")
            self.model = None

    def predict(self, features):
        try:
            # =========================
            # SAFE FEATURE EXTRACTION
            # =========================
            total_hours = features.get("total_hours", 0)
            job_count = features.get("job_count", 0)
            avg_gap = features.get("avg_gap", 0)
            overlap_count = features.get("overlap_count", 0)

            feature_vector = np.array([[ 
                total_hours,
                job_count,
                avg_gap,
                overlap_count
            ]])

            print("📊 Model Input:", feature_vector)

            # =========================
            # USE ML MODEL IF AVAILABLE
            # =========================
            if self.model:
                score = self.model.predict(feature_vector)[0]
                print("🤖 Model Score:", score)

            else:
                # =========================
                # 🔥 FALLBACK LOGIC (VERY IMPORTANT)
                # =========================
                if total_hours < 20:
                    score = 0
                elif total_hours < 35:
                    score = 1
                else:
                    score = 2

                print("⚙ Using fallback score:", score)

            # =========================
            # CONVERT SCORE → LABEL
            # =========================
            if score == 0:
                return "Low"
            elif score == 1:
                return "Medium"
            else:
                return "High"

        except Exception as e:
            print(" PREDICTION ERROR:", str(e))
            return "Low"