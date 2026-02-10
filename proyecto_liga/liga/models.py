from django.db import models

# 1. Relación 1:1 - Un Equipo tiene una Sede Oficial (Estadio)
class Estadio(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fundacion = models.IntegerField()
    # 1:1 Relación
    estadio = models.OneToOneField(Estadio, on_delete=models.SET_NULL, null=True, blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# 2. Relación 1:N - Un Jugador pertenece a un Equipo
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    dorsal = models.IntegerField()
    posicion = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")

# 3. Relación N:M - Competiciones (Liga, Copa, Champions)
class Competicion(models.Model):
    nombre = models.CharField(max_length=100)
    # Relación Muchos a Muchos simple
    equipos = models.ManyToManyField(Equipo, related_name="competiciones", blank=True)

# 4. Relación N:M con modelo intermedio (Through)
class Partido(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)

class Estadistica(models.Model):
    # Relación intermedia entre Jugador y Partido
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name="estadisticas")
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name="estadisticas")
    goles = models.IntegerField(default=0)
    minutos_jugados = models.IntegerField(default=0)