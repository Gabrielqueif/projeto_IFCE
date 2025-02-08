from django.urls import path
from homepage import views

app_name = 'lista'

urlpatterns = [
    path('', views.lista, name='lista')
]
