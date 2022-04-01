from re import template
from django.shortcuts import render
from .forms import ProdutosForm
# Create your views here.

def new_produto(request):
    print('metodo:',request.method)
    form = ProdutosForm()
    template_name = 'new_produto.html'
    context = {
        'produtos': form
    }
    return render(request, template_name, context)