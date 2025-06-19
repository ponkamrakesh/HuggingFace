# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS settings so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body structure
class PredictionRequest(BaseModel):
    features: List[str]

# Dummy prediction logic
@app.post("/predict")
async def predict(request: PredictionRequest):
    selected = request.features
    predictions = {}

    for feature in selected:
        if feature == "Marks":
            predictions["Marks"] = "Predicted Score: 87%"
        elif feature == "Sales":
            predictions["Sales"] = "Expected Sales: ₹1.2L"
        elif feature == "Customer Retention":
            predictions["Customer Retention"] = "Retention Rate: 74%"
        elif feature == "Inventory":
            predictions["Inventory"] = "Reorder in: 5 days"
        elif feature == "Profit":
            predictions["Profit"] = "Estimated Profit: ₹45K"
        else:
            predictions[feature] = "No model yet"

    return {"predictions": predictions}
