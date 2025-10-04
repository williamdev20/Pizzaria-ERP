from django.db import models
from cadastro.models import Custom

class Cliente(models.Model):
	user = models.OneToOneField(Custom, on_delete=models.CASCADE)
	numeroWhatsapp = models.CharField(max_length=200, null=False, blank=False)
