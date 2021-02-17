from django.db import models
from django.utils import timezone

# Create your models here.
class Agendar(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    cidade = models.CharField(max_length=254)
    estado = models.CharField(max_length=200)
    celular = models.IntegerField()
    observações = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
## Teste
