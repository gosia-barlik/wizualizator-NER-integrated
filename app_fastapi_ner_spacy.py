import uvicorn
from fastapi import FastAPI
from flask_cors import CORS, cross_origin
from fastapi.middleware.cors import CORSMiddleware
from model_ner_spacy import NERspaCyLinkQueryModel, NERspaCyTextQueryModel, NERspaCyLinkModel, NERspaCyTextModel
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

model_link = NERspaCyLinkModel()
model_text = NERspaCyTextModel()

@app.post('/ner_link/')
def predict(data: NERspaCyLinkQueryModel):
    data = data.dict()
    return model_link.get_entities(data['text'])

@app.post('/ner_text/')
def predict(data: NERspaCyTextQueryModel):
    data = data.dict()
    return model_text.get_entities(data['text'])

app.mount("/", StaticFiles(directory="public", html = True), name="static")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8002)