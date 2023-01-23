## uvicorn main:app --reload

import fastapi
import uvicorn
from joblib import load
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

try:
    SBA_data = pd.read_csv('/home/apprenant/Documents/archive/SBAnational.csv')
except:
    SBA_data = pd.read_csv('C:/Users/emada/Downloads/loan_project (1)/SBAnational.csv')
    
loaded_model = load('random_forest_model.joblib')

# Creation d'une nouvelle instance FastAPI
app = FastAPI()

# Définir une class pour réaliser des réquetes
class request_body(BaseModel):
    State : object
    NAICS : object 
    ApprovalFY : int
    Term : int
    NoEmp : int
    NewExist : float
    CreateJob : int
    FranchiseCode : int
    UrbanRural : int  
    RevLineCr : object 
    LowDoc : object 
    GrAppv : float
    Categorie_NAICS : object

# Definition du chemin du point de determination (API)
@app.post("/predict") #local : http://127.0.0.1:8000/predict

# Définition de la fonction de prédiction
def predict(data : request_body):
    #nouvelle données sur lesquelles on fait  la prédiction
    new_data = [[
        data.State ,
        data.NAICS  ,
        data.ApprovalFY, 
        data.Term ,
        data.NoEmp ,
        data.NewExist ,
        data.CreateJob ,
        data.FranchiseCode, 
        data.UrbanRural   ,
        data.RevLineCr  ,
        data.LowDoc  ,
        data.GrAppv ,
        data.Categorie_NAICS, 
                ]]
    # Prédiction
    class_idx = loaded_model.predict(new_data)[0]

    return {'class' : SBA_data.target[class_idx]}
