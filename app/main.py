from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionRequest(BaseModel):
    features: List[str]

@app.get("/", response_class=HTMLResponse)
def root():
    with open("home.html", "r") as f:
        return f.read()

@app.post("/predict")
def predict(request: PredictionRequest):
    result = {}
    for feature in request.features:
        result[feature] = f"✨ AI predicts: some value for {feature}"
    return {"predictions": result}
