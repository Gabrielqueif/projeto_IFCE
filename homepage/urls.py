from django.urls import path
from homepage import views

Urlpath = [
    path("", views.lista, name='lista')
]
