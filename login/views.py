from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def cliente(request):
	error = ""

	if request.method == "POST":
		email = request.POST.get('email')
		senha = request.POST.get('senha')

		user = authenticate(request, username=email, password=senha)

		if user is not None and user.is_user:
			login(request, user)
			return redirect("menu")
		else:
			error = "Email ou senha incorretos!"

	return render(request, "login/cliente.html", {"error": error})


def pizzaria(request):
	error = ""

	if request.method == "POST":
		email = request.POST.get('email')
		senha = request.POST.get('senha')

		user = authenticate(request, username=email, password=senha)

		if user is not None and user.is_pizzaria:
			login(request, user)
			return redirect("pedidos", id=user.pizzaria.id)
		else:
			error = "Email ou senha incorretos!"

	return render(request, "login/pizzaria.html", {"error": error})