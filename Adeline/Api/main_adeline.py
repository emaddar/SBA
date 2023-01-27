from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel
import pickle
import pandas as pd

pickle_in = open('random_forest_model.pkl', 'rb') 
forest_model =pickle.load(pickle_in)

app= FastAPI()

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
    

@app.post("/predict")

def predict(data : request_body):
    # nouvelle données sur lesquelles on fait  la prédiction
    # new_data = [[
    #     data.State ,
    #     data.NAICS  ,
    #     data.ApprovalFY, 
    #     data.Term ,
    #     data.NoEmp ,
    #     data.NewExist ,
    #     data.CreateJob ,
    #     data.FranchiseCode, 
    #     data.UrbanRural   ,
    #     data.RevLineCr  ,
    #     data.LowDoc  ,
    #     data.GrAppv ,
    #     data.Categorie_NAICS, 
    #             ]]
    new_data=pd.DataFrame(dict(data),index = [0])

    class_idx = forest_model.predict(new_data)[0]
    return {'class' : class_idx}