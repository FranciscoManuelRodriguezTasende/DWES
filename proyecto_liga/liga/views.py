from rest_framework.viewsets import ModelViewSet #
from .models import Equipo, Jugador, Estadio, Competicion, Estadistica, Partido
from .serializers import (
    EquipoSerializer, JugadorSerializer, EstadioSerializer,
    EstadisticaSerializer, PartidoSerializer
)
from rest_framework.filters import SearchFilter, OrderingFilter  #
from django_filters.rest_framework import DjangoFilterBackend  #
from .filters import EquipoFilter


class EquipoViewSet(ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

    # Activamos los tres motores: Filtros, Búsqueda y Ordenación
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # 1. Filtros (simples y avanzados)
    filterset_class = EquipoFilter

    # 2. Búsqueda textual (Search)
    search_fields = ['nombre', 'ciudad']

    # 3. Ordenación (Ordering)
    ordering_fields = ['fundacion', 'nombre']
    ordering = ['nombre']  # Orden por defecto

class EstadioViewSet(ModelViewSet):
    queryset = Estadio.objects.all()
    serializer_class = EstadioSerializer

class EquipoViewSet(ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class JugadorViewSet(ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class PartidoViewSet(ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

class EstadisticaViewSet(ModelViewSet):
    queryset = Estadistica.objects.all()
    serializer_class = EstadisticaSerializer