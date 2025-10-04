from django.db import models
from cadastro.models import Custom

class Pizzaria(models.Model):
	user = models.OneToOneField(Custom, on_delete=models.CASCADE)
	cep = models.CharField(max_length=9, null=False, blank=False)
	numeroWhatsapp = models.CharField(max_length=20, null=False, blank=False)


class Pizza(models.Model):
	pizzaria = models.ForeignKey(Pizzaria, on_delete=models.CASCADE)
	nomePizza = models.CharField(max_length=200, null=False, blank=False)
	precoPizza = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)