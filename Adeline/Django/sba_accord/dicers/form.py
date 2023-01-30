from django import forms

class ApiForm(forms.Form):
    State = forms.CharField(initial='CA')
    NAICS = forms.CharField(initial="0")
    ApprovalFY = forms.IntegerField(initial=1997)
    Term = forms.IntegerField(initial=240)
    NoEmp = forms.IntegerField(initial=6)
    NewExist = forms.IntegerField(initial=1)
    CreateJob= forms.IntegerField(initial=0)
    FranchiseCode = forms.IntegerField(initial=1)
    UrbanRural = forms.IntegerField(initial=0)
    RevLineCr = forms.CharField(initial="Y")
    LowDoc = forms.CharField(initial="N")
    GrAppv = forms.IntegerField(initial =250000)
    Categorie_NAICS = forms.CharField(initial="Other")

