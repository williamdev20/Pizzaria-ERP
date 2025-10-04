from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom(AbstractUser):
	username = models.CharField(
		max_length=200,
		unique=True,
		null=False,
		blank=False
	)
	email = models.EmailField(unique=True, null=False, blank=False)
	is_user = models.BooleanField(default=False)
	is_pizzaria = models.BooleanField(default=False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username"] # Depois pesquisar pq precisa dessa linha aqui
