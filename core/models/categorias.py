from django.db import models

class Categorias(models.Model):
    descricao = models.CharField(max_length=100)