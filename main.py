from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline

app = FastAPI()

class TxtIn(BaseModel):
    txt: str

class PredictOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check":"OK"}

@app.post("/detect", response_model=PredictOut)
def pred(payload: TxtIn):
    lang = predict_pipeline(payload.txt)
    return{"language": lang}


