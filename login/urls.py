from django.urls import path
from . import views

urlpatterns = [
	path('cliente/', views.cliente, name="login_cliente"),
	path('pizzaria/', views.pizzaria, name="login_pizzaria")
]