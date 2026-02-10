from rest_framework import serializers
from .models import Equipo, Jugador, Estadio, Competicion, Estadistica, Partido

class EstadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadio
        fields = ['id', 'nombre', 'capacidad']

class PartidoSerializer(serializers.ModelSerializer): # <--- NUEVO
    class Meta:
        model = Partido
        fields = ['id', 'fecha', 'rival']

class EquipoSerializer(serializers.ModelSerializer):
    estadio_detalle = EstadioSerializer(source="estadio", read_only=True)
    estadio = serializers.PrimaryKeyRelatedField(
        queryset=Estadio.objects.all(),
        allow_null=True,
        required=False
    )
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'ciudad', 'estadio', 'estadio_detalle']

class JugadorSerializer(serializers.ModelSerializer):
    equipo_detalle = EquipoSerializer(source="equipo", read_only=True)
    equipo = serializers.PrimaryKeyRelatedField(queryset=Equipo.objects.all())
    class Meta:
        model = Jugador
        fields = ['id', 'nombre', 'dorsal', 'equipo', 'equipo_detalle']

class EstadisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadistica
        fields = ['id', 'jugador', 'partido', 'goles', 'minutos_jugados']

        class FicharJugadorSerializer(serializers.Serializer):
            jugador_id = serializers.IntegerField(help_text="ID del jugador que quieres fichar")