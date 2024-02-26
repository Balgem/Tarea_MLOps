from fastapi import FastAPI
import uvicorn
import pickle
import pandas as pd


app = FastAPI()
model = pickle.load(open("model_reg.pkl", "rb"))

def model_pred(features):
    test_data = pd.DataFrame([features])
    prediction = model.predict(test_data)
    return float(prediction[0])

@app.get("/")
async def root():
    return {"message": "Prediction2"}

@app.get("/predict")
async def predict(
    TV: float,
    ):

    prediction = model.predict(
        [[TV]]
    )
    return {
            f"Cantidad de televisores vendidos por presupuesto en dolares en campaña de marketing: {prediction}."
        }

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

#venv\scripts\activate  
#uvicorn main:app --reload
#pip install pipreqs
#pip freeze > requirements.txt