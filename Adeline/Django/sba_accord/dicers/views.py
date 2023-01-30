from django.shortcuts import render
from .form import ApiForm
import requests 
import json

def consumer(request):
    # header = dictionnaire accept contnt copié coller de l'api mais ne pas oublié de mettre les guillement au clé

    form = ApiForm(request.POST or None)
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            data = json.dumps(form.cleaned_data)

            reponse = requests.post('http://127.0.0.1:8000/predict', data=data)
            info = reponse.text
            return render(request, 'formulaire.html', context={'form' : form, 'info' : info} )
    context = {'form' : form}
    return render(request, 'formulaire.html', context=context )