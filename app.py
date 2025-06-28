from fastapi import FastAPI, HTTPException
import pandas as pd
import numpy as np
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.get("/")
async def root():
    return {"message": "MTY Data Platform Demo is running 🚀"}

@app.post("/predict")
async def predict(data: InputData):
    # Replace this dummy logic with your real model logic
    features = np.array([[data.feature1, data.feature2, data.feature3]])
    prediction = features.sum(axis=1)[0]  # dummy example: sum of features
    return {
        "input": data.dict(),
        "prediction": prediction,
    }
