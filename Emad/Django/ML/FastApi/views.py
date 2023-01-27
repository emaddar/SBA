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
    response = requests.post("http://localhost:8000/predict", json=data)

    return render(request, 'result.html', {
                                            'response':response.json()['prediction'],
                                            'proba':round(response.json()['probability'][1]*100,2),
                                            
    })