from django.urls import path
from . import views

urlpatterns = [
    path('almacenamiento/', views.almacenamiento, name='almacenamiento'),
]