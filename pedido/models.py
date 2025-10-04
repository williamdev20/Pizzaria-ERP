from django.db import models
from pizzaria.models import Pizzaria

class Pedidos(models.Model):
	pizzaria = models.ForeignKey(Pizzaria, on_delete=models.CASCADE)
	primeiroSabor = models.CharField(max_length=200, null=False, blank=False)
	segundoSabor = models.CharField(max_length=200, null=False, blank=False)
	cep = models.CharField(max_length=9, null=False, blank=False)
	borda = models.CharField(max_length=200, null=False, blank=False)
	precoTotal = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)