from django.urls import path
from . import views

urlpatterns = [
    path('reseñas/', views.reseñas, name='reseñas'),
]