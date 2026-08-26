from django.urls import path
from . import views

urlpatterns = [
    path('seguridad-confidencialidad/', views.seguridad_confidencialidad, name='seguridad_confidencialidad'),
]