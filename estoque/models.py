from django.db import models

class Produtos(models.Model):
    produto = models.CharField('Nome', max_length=100)
    quantidade = models.DecimalField('quantidade',max_digits=10000, decimal_places=2)
    preco = models.DecimalField('preco',max_digits=10000, decimal_places=2)
    