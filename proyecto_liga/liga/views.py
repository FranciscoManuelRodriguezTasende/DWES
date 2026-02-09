from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Equipo
from .serializers import EquipoSerializer


class EquipoListAPIView(APIView):
    # GET lista: Devuelve todos los equipos
    def get(self, request):
        equipos = Equipo.objects.all()
        # 'many=True' indica que estamos traduciendo una lista
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)

    # POST crear: Recibe JSON y lo guarda en la BD
    def post(self, request):
        serializer = EquipoSerializer(data=request.data)
        # DRF valida automáticamente tipos y campos obligatorios
        if serializer.is_valid():
            serializer.save()  # Guarda el objeto
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Si hay errores (ej: nombre repetido), devuelve un 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EquipoDetailAPIView(APIView):
    # GET detalle: Devuelve un único equipo por su ID
    def get(self, request, pk):
        equipo = get_object_or_404(Equipo, pk=pk)
        serializer = EquipoSerializer(equipo)
        return Response(serializer.data)