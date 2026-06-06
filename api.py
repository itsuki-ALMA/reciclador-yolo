from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from ultralytics import YOLO
import shutil
import os

app = FastAPI()

model = YOLO("model/best.pt")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    
    filepath = f"uploads/{file.filename}"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = model(filepath)

    probs = results[0].probs

    classe = results[0].names[probs.top1]

    confianca = float(probs.top1conf)

    return {
        "classe": classe,
        "confianca": round(confianca * 100, 2)
    }