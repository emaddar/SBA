from fastapi import FastAPI
from model import predict
from pydantic import BaseModel


class Textin(BaseModel):
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

class Prediction(BaseModel):
    acoord_pret = "str"
    
app=FastAPI()

@app.get("/predict",response_model=Prediction)
async def root_predict(playload: Textin):
    to_return = predict(playload)
    return{"accord_pret":to_return}