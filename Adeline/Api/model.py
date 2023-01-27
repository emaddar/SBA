import pickle
import pandas as pd

model = pickle.load(open('random_forest_model.pkl','rb'))

cols = ['State', 'NAICS', 'ApprovalFY', 'Term', 'NoEmp', 'NewExist',
       'CreateJob', 'FranchiseCode', 'UrbanRural', 'RevLineCr', 'LowDoc',
       'GrAppv', 'Categorie_NAICS']
value = ["IN","45",1997,84,4,2.0,0,1,0,'N','Y',60000.0,"Retail trade"]


def predict():
    to_predict = dict(zip(cols,value))
    to_predict = pd.DataFrame(to_predict,index=[0])
    
 

print(model)