from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Equipo


# Vista para LISTAR y CREAR equipos
class EquipoListAPIView(APIView):
    def get(self, request):
        # 1. Sacamos los datos de la base de datos
        equipos = Equipo.objects.all()
        # 2. Construimos el JSON a mano (como pide el Bloque 1)
        data = []
        for e in equipos:
            data.append({
                "id": e.id,
                "nombre": e.nombre,
                "ciudad": e.ciudad,
                "fundacion": e.fundacion
            })
        return Response(data)

    def post(self, request):
        # 1. Recibimos los datos que nos envían
        nombre = request.data.get('nombre')
        ciudad = request.data.get('ciudad')
        fundacion = request.data.get('fundacion')

        # 2. Creamos el equipo en la base de datos
        nuevo_equipo = Equipo.objects.create(
            nombre=nombre,
            ciudad=ciudad,
            fundacion=fundacion
        )

        # 3. Respondemos que se ha creado correctamente
        return Response({"mensaje": "Equipo creado"}, status=status.HTTP_201_CREATED)


# Vista para el DETALLE de un equipo específico
class EquipoDetailAPIView(APIView):
    def get(self, request, pk):
        # Buscamos el equipo por su ID o devolvemos error 404
        equipo = get_object_or_404(Equipo, pk=pk)
        data = {
            "id": equipo.id,
            "nombre": equipo.nombre,
            "ciudad": equipo.ciudad,
            "fundacion": equipo.fundacion
        }
        return Response(data)