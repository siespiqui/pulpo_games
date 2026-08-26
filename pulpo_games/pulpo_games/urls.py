"""
URL configuration for pulpo_games project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('inventario/', include('inventario.urls')),
    path('mantenimiento/', include('mantenimiento.urls')),
    path('reservas/', include('reservas.urls')),
    path('compras/', include('compras.urls')),
    path('compras_segunda_mano/', include('compras_segunda_mano.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('reseñas/', include('reseñas.urls')),
    path('almacenamiento/', include('almacenamiento.urls')),
    path('proteccion-datos/', include('proteccion_datos.urls')),
    path('seguridad-confidencialidad/', include('seguridad_confidencialidad.urls')),
    path('admin/', admin.site.urls),
]