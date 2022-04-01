from django import forms
from .models import Produtos
class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = [
                'produto',
                'quantidade', 
                'preco'
        ]
        #fields = '___all___'aparecer todos os campos
       # exclude = ['produto'] excluir 1 e aparecer os outros