from django.urls import path
from . import views

urlpatterns = [
	path('pedidos/<int:id>', views.pedidos, name="pedidos"),
]