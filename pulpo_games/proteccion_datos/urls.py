from django.urls import path
from . import views

urlpatterns = [
    path('proteccion-datos/', views.proteccion_datos, name='proteccion_datos'),
]