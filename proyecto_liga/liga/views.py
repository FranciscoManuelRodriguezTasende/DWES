from rest_framework.viewsets import ModelViewSet #
from .models import Equipo, Jugador, Estadio, Competicion, Estadistica, Partido
from .serializers import (
    EquipoSerializer, JugadorSerializer, EstadioSerializer,
    EstadisticaSerializer, PartidoSerializer
)

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