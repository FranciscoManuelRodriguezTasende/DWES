from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EquipoViewSet, JugadorViewSet, EstadioViewSet,
    PartidoViewSet, EstadisticaViewSet # <--- ¡Asegúrate de que estén todas aquí!
)

router = DefaultRouter()
router.register(r'equipos', EquipoViewSet, basename='equipo')
router.register(r'jugadores', JugadorViewSet, basename='jugador')
router.register(r'estadios', EstadioViewSet, basename='estadio')
router.register(r'partidos', PartidoViewSet, basename='partido')
router.register(r'estadisticas', EstadisticaViewSet, basename='estadistica')

urlpatterns = [
    path('', include(router.urls)),
]