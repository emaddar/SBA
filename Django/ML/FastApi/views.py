# python manage.py runserver 7000
# https://github.com/jeremy-vangansberg/medical_cost

from django.shortcuts import render
import json

# Create your views here.
# from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')



def result(request):

    GrAppv = request.GET['GrAppv']                       #0
    State = request.GET['State']                               #1
    NAICS = request.GET['NAICS']                 #2
    ApprovalFY = request.GET['ApprovalFY']   #3
    Term = request.GET['Term']               #4
    NoEmp = request.GET['NoEmp']                 #5
    NewExist = request.GET['NewExist']                     #6
    CreateJob = request.GET['CreateJob']               #7
    FranchiseCode = request.GET['FranchiseCode']                       #8
    UrbanRural = request.GET['UrbanRural']                           #9
    RevLineCr = request.GET['RevLineCr']                                 #10
    LowDoc = request.GET['LowDoc']  


    import requests

    # Define the input parameters
    data = {
        "State": State,
        "NAICS": NAICS,
        "ApprovalFY": ApprovalFY,
        "Term": Term,
        "NoEmp": NoEmp,
        "NewExist": NewExist,
        "CreateJob": CreateJob,
        "FranchiseCode": FranchiseCode,
        "UrbanRural":  UrbanRural,
        "RevLineCr": RevLineCr,
        "LowDoc": LowDoc,
        "GrAppv": GrAppv
    }

    # Send the POST request
    response_RFR = requests.post("https://fastapi-rfr.onrender.com/predict", json=data)
    response_XGB = requests.post("https://fastapi-xgb.onrender.com/predict", json=data)
    response_logisreg = requests.post("https://log-reg-sba2.onrender.com/predict", json=data)


    if response_RFR.json()['prediction'] == 'P I F':
        response_RFR_result =  'Acceptance credit'
    else :
        response_RFR_result =  'Not acceptance credit'


    if response_XGB.json()['prediction']== "1":
        response_XGB_result = 'Acceptance credit'
    else : 
        response_XGB_result = 'Not acceptance credit'

    
    if response_logisreg.json()['prediction'] == 'P I F':
        response_logisreg_result =  'Acceptance credit'
    else :
        response_logisreg_result =  'Not acceptance credit'


    return render(request, 'result.html', {
                                            'response_RFR':response_RFR_result,
                                            'proba_RFR':round(response_RFR.json()['probability'][1]*100,2),
                                            'probaNon_RFR': round(response_RFR.json()['probability'][0]*100,2),

                                            'response_XGB':response_XGB_result,
                                            'proba_XGB':round(response_XGB.json()['probability'][1]*100,2),
                                            'probaNon_XGB': round(response_XGB.json()['probability'][0]*100,2),
                                            

                                            'response_logisreg':response_logisreg_result,
                                            'proba_logisreg':round(response_logisreg.json()['probability'][1]*100,2),
                                            'probaNon_logisreg': round(response_logisreg.json()['probability'][0]*100,2),

    })