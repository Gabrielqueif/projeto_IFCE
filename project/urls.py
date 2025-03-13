"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import insumosviewset, estadosviewset, tabelaviewset


router = DefaultRouter()
router.register(r'items', insumosviewset)
router.register(r'items', estadosviewset)
router.register(r'items', tabelaviewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('homepage.urls')),
    path('api/', include(router.urls)),
]

