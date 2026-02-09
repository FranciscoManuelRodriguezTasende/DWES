from rest_framework.viewsets import ModelViewSet
from .models import Equipo, Jugador
from .serializers import EquipoSerializer, JugadorSerializer

# ModelViewSet maneja list, create, retrieve, update y destroy automáticamente
class EquipoViewSet(ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class JugadorViewSet(ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer