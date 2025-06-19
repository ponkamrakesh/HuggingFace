from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class PredictionRequest(BaseModel):
    features: List[str]

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/predict")
def predict(request: PredictionRequest):
    result = {}
    for feature in request.features:
        result[feature] = f"🔥 AI predicts: value for {feature}"
    return {"predictions": result}
