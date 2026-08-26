from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def seguridad_confidencialidad(request):
    return HttpResponse("Hello world!")
