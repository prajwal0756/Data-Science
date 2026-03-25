from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

model = pickle.load(open("churn_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prob = model.predict_proba(df)[0][1]

    # apply your optimized threshold
    prediction = 1 if prob > 0.3 else 0

    return {
        "churn_probability": float(prob),
        "churn_prediction": int(prediction)
    }