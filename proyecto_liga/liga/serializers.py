from rest_framework import serializers
from .models import Equipo, Jugador

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        # Incluimos los campos definidos en tu modelo [cite: 61-64]
        fields = ['id', 'nombre', 'ciudad', 'fundacion', 'activo', 'created_at']
        # Marcamos como solo lectura los campos que genera el sistema
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True}
        }

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        # Incluimos los campos del modelo Jugador [cite: 79-87]
        fields = ['id', 'nombre', 'dorsal', 'posicion', 'equipo']