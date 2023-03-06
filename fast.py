import pickle
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware




pickle_in = open('xg_reg.pkl', 'rb') 
modelRandomForest = pickle.load(pickle_in)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict/")

async def predict(
    
    duration_ms:int = 190027,
    danceability : float = 0.779,
   
    energy : float = 0.3830,
    
    loudness : float = -14.817,
    speechiness :float = 0,
    acousticness : float = 0.794,
    instrumentalness:float = 0.00001,
    liveness: float = 0.11,
    valence:float = 0.6830,
    tempo:float = 103.983
    
):
    data = {
   "duration_ms" : duration_ms,
    "danceability" : danceability,
   
    "energy" : energy,
  
    "loudness" : loudness,
    "speechiness" :speechiness,
    "acousticness" : acousticness,
    "instrumentalness":instrumentalness,
    "liveness": liveness,
    "valence" : valence,
    "tempo" :tempo
    
    
    }
    pred=pd.DataFrame(dict(data),index = [0])


    class_pred = modelRandomForest.predict(pred)[0]
    
    return {"Class":float(class_pred)}
    
   