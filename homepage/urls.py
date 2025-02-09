from django.urls import path
from homepage import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('memorial/', views.memorial, name='memorial'),
    path('calculadora/', views.calculadora, name='calculadora'),
]
