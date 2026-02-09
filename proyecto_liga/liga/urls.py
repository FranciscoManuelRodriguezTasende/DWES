from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipoViewSet, JugadorViewSet

# 1. Creamos el router
router = DefaultRouter()

# 2. Registramos los recursos de tu liga
router.register(r'equipos', EquipoViewSet, basename='equipo')
router.register(r'jugadores', JugadorViewSet, basename='jugador')

# 3. Las URLs de la API ahora las gestiona el router
urlpatterns = [
    path('', include(router.urls)),
]