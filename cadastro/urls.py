from django.urls import path
from . import views

urlpatterns = [
	path('cliente/', views.cliente, name="cadastro_cliente"),
	path('pizzaria/', views.pizzaria, name="cadastro_pizzaria"),
	path('pizzaria/<int:id>/pizza/', views.pizza, name="cadastro_pizza"),
]