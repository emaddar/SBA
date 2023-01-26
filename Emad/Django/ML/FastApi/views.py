from django.shortcuts import render

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

    return render(request, 'result.html', {
                                            'GrAppv':GrAppv,
                                            
    })