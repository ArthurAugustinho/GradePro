from django.urls import path
from .views import formulario, resultado

app_name = 'calculadora'

urlpatterns = [
    path('', formulario, name='formulario'),
    path('resultado/', resultado, name='resultado')
]
