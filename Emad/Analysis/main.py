from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel
import pickle
import pandas as pd

pickle_in = open('RFR_Model.pkl', 'rb') 
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
    param1: object
    param2: object
    param3: int
    param4: int
    param5: int
    param6: float
    param7: int
    param8: int
    param9: int
    param10: object
    param11: object
    param12: float


@app.post("/predict")
def predict(params: ModelParams):

    pred = get_prediction(params.param1, 
                          params.param2,
                          params.param3,
                          params.param4,
                          params.param5,
                          params.param6,
                          params.param7,
                          params.param8,
                          params.param9,
                          params.param10,
                          params.param11,
                          params.param12
                          )

    return pred
