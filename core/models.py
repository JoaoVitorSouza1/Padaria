from django.db import models
class Padarias(models.Model):
    nome = models.CharField('Nome', max_length=100)
    endereco = models.CharField('Endereco', max_length=100)
    telefone = models.CharField('Telefone', max_length=12)
    
    