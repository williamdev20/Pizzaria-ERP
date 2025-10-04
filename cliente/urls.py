from django.urls import path
from . import views

urlpatterns = [
	path('menu/', views.menu, name="menu"),
	path('pedir/<int:id>', views.pedir, name="pedir"),
	path('confirmado/<int:id>', views.confirmado, name="confirmado")
]