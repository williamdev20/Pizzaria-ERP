from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from pizzaria.models import Pizzaria, Pizza
from pedido.models import Pedidos


@login_required(login_url="/login/cliente/")
def menu(request):
	pizzarias = Pizzaria.objects.all()

	return render(request, "cliente/menu.html", {"pizzarias": pizzarias})


@login_required(login_url="/login/cliente")
def pedir(request, id):
	pizzaria = get_object_or_404(Pizzaria, id=id)
	pizzas = Pizza.objects.filter(pizzaria=pizzaria)
	precoTotal = 0

	if request.method == "POST":
		primeiroSabor_id = request.POST.get('primeiroSabor')
		segundoSabor_id = request.POST.get('segundoSabor')
		cep = request.POST.get('cep')
		borda = request.POST.get('borda')
		button = request.POST.get('button')


		if primeiroSabor:
			pizza1 = Pizza.objects.get(id=primeiroSabor)
			precoTotal += pizza1.precoPizza
			primeiroSabor = pizza1.nomePizza

		if segundoSabor and segundoSabor != "":
			pizza2 = Pizza.objects.get(id=segundoSabor)
			precoTotal += pizza2.precoPizza
			precoTotal = precoTotal / 2
			segundoSabor = pizza2.nomePizza


		Pedidos.objects.create(
			pizzaria=pizzaria,
			primeiroSabor=primeiroSabor,
			segundoSabor=segundoSabor,
			cep=cep,
			borda=borda,
			precoTotal=precoTotal
		)


		if button == "confirmar":
			return redirect("confirmado", id=id)


	return render(request, "cliente/pedir.html", {"pizzaria_id": pizzaria.id, "pizzas": pizzas, "precoTotal": precoTotal})


def confirmado(request, id):
	pedido = get_object_or_404(Pedidos, id=id)
	return render(request, 'cliente/confirmado.html', {"precoTotal": pedido.precoTotal})