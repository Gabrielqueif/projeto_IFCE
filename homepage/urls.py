from django.urls import path
from homepage import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('memorial/', views.memorial, name='memorial'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('lista/', views.listar_arquivos, name='lista'),
]
