from django.urls import path
from . import views

urlpatterns = [
    path('compras_segunda_mano/', views.compras_segunda_mano, name='compras_segunda_mano'),
]