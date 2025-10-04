from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from cliente.models import Cliente
from pizzaria.models import Pizzaria, Pizza

User = get_user_model()

def cliente(request):
	error = ""

	if request.method == "POST":
		nome = request.POST.get('nome')
		email = request.POST.get('email')
		numeroWhatsapp = request.POST.get('numero')
		senha = request.POST.get('senha')

		try:
			user = User.objects.create_user(
				username=nome,
				email=email,
				password=senha,
				is_user=True
			)

			Cliente.objects.create(
				user=user,
				numeroWhatsapp=numeroWhatsapp
			)

			return redirect("login_cliente")
		except IntegrityError:
			error = "Esta conta já existe!"

	return render(request, "cadastro/cliente.html", {"error": error})


def pizzaria(request):
	error = ""

	if request.method == "POST":
		nomePizzaria = request.POST.get('nomePizzaria')
		cep = request.POST.get('cep')
		email = request.POST.get('email')
		numeroWhatsapp = request.POST.get('numeroWhatsapp')
		senha = request.POST.get('senha')

		try:
			user = User.objects.create_user(
				is_pizzaria = True,
				username=nomePizzaria,
				email=email,
				password=senha
			)

			Pizzaria.objects.create(
				user=user,
				cep=cep,
				numeroWhatsapp=numeroWhatsapp
			)

			return redirect("cadastro_pizza", id=user.id)

		except IntegrityError:
			error = "Essa conta já existe!"

	return render(request, "cadastro/pizzaria.html", {"error": error})


def pizza(request, id):
	pizzaria = get_object_or_404(Pizzaria, user_id=id)

	if request.method == "POST":
		nomePizza = request.POST.get('nomePizza')
		precoPizza = request.POST.get('precoPizza')
		button = request.POST.get('button')

		Pizza.objects.create(
			pizzaria=pizzaria,
			nomePizza=nomePizza,
			precoPizza=precoPizza
		)

		if button == "finalizar":
			return redirect("login_pizzaria")

	return render(request, "cadastro/pizza.html", {"pizzaria_id": id})
