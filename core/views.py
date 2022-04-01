from django.shortcuts import render
from django.http import HttpResponse
from multiprocessing import context 
from.models import Padarias


# Create your views here.
def index (request):
    padarias = Padarias.objects.all()
    print(padarias)
    for padaria in padarias:
        print(padaria.nome, padaria.endereco, padaria.telefone)
    template_name = 'index.html'
    context = {
       'nome':'UGB',
       'padarias':padarias
   }
    return render(request, template_name, context)
