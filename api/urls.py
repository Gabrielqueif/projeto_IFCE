from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import insumosviewset, estadosviewset, tabelaviewset 

router = DefaultRouter()
router.register(r'items', insumosviewset)
router.register(r'items', estadosviewset)
router.register(r'items', tabelaviewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

