## uvicorn main:app --port 8002  --reload

from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel
import pickle
import pandas as pd

pickle_in = open('LogisREG.pkl', 'rb') 
clf =pickle.load(pickle_in)

def get_prediction(State, NAICS, ApprovalFY, Term, NoEmp, NewExist, CreateJob, FranchiseCode, UrbanRural, RevLineCr, LowDoc, GrAppv):
    x = [[State, NAICS, ApprovalFY, Term, NoEmp, NewExist, CreateJob, FranchiseCode, UrbanRural, RevLineCr, LowDoc, GrAppv]]
    df = pd.DataFrame(x, columns=['State', 'NAICS', 'ApprovalFY', 'Term', 'NoEmp', 'NewExist', 'CreateJob', 'FranchiseCode', 'UrbanRural', 'RevLineCr', 'LowDoc', 'GrAppv'])
    df = df.astype({'State': 'object', 'NAICS': 'object', 'UrbanRural': 'object', 'RevLineCr': 'object', 'LowDoc': 'object'})
    y = clf.predict(df)[0]
    prob = clf.predict_proba(df)[0].tolist()
    return {'prediction': str(y), 'probability': prob}



# initiate API
app = FastAPI()


# define model for post request.
class ModelParams(BaseModel):
    State: object
    NAICS: object
    ApprovalFY: int
    Term: int
    NoEmp: int
    NewExist: float
    CreateJob: int
    FranchiseCode: int
    UrbanRural: int
    RevLineCr: object
    LowDoc: object
    GrAppv: float


@app.post("/predict")
def predict(params: ModelParams):

    pred = get_prediction(params.State, 
                          params.NAICS,
                          params.ApprovalFY,
                          params.Term,
                          params.NoEmp,
                          params.NewExist,
                          params.CreateJob,
                          params.FranchiseCode,
                          params.UrbanRural,
                          params.RevLineCr,
                          params.LowDoc,
                          params.GrAppv
                          )

    return pred
