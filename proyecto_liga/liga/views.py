from rest_framework.viewsets import ModelViewSet #
from .models import Equipo, Jugador, Estadio, Competicion, Estadistica, Partido
from .serializers import (
    EquipoSerializer, JugadorSerializer, EstadioSerializer,
    EstadisticaSerializer, PartidoSerializer
)
from rest_framework.filters import SearchFilter, OrderingFilter  #
from django_filters.rest_framework import DjangoFilterBackend  #
from .filters import EquipoFilter
from rest_framework.decorators import action #
from rest_framework.response import Response #
from rest_framework import status #


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

    @action(detail=True, methods=['post'])  # Acción por objeto
    def fichar_jugador(self, request, pk=None):
        # 1. Obtenemos el equipo actual (el de la URL)
        equipo = self.get_object()
        holaquetalestas
        # 2. Validamos la entrada con el serializer manual
        serializer = FicharJugadorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Devuelve 400 si no hay ID

        jugador_id = serializer.validated_data['jugador_id']

        # 3. Buscamos al jugador
        try:
            jugador = Jugador.objects.get(id=jugador_id)
        except Jugador.DoesNotExist:
            return Response(
                {"error": "El jugador no existe"},
                status=status.HTTP_404_NOT_FOUND
            )

        # 4. Lógica de negocio: ¿Ya está en este equipo?
        if jugador.equipo == equipo:
            return Response(
                {"error": "El jugador ya pertenece a este equipo"},
                status=status.HTTP_409_CONFLICT
            )

        # 5. Ejecutamos la acción
        jugador.equipo = equipo
        jugador.save()

        return Response(
            {"mensaje": f"Jugador {jugador.nombre} fichado correctamente por el {equipo.nombre}"},
            status=status.HTTP_200_OK
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