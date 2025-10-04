from django.shortcuts import render, get_object_or_404
from pedido.models import Pedidos
from .models import Pizzaria

def pedidos(request, id):
	pizzaria = get_object_or_404(Pizzaria, id=id)
	pedidos = Pedidos.objects.filter(pizzaria=pizzaria)

	return render(request, "pizzaria/pedidos.html", {"pedidos": pedidos, "pizzaria": pizzaria})