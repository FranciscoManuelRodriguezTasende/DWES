from django.db import models
from django.contrib.auth.models import User

# PERFIL (Relación 1:1 con el Usuario del sistema)
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    es_arbitro = models.BooleanField(default=False)
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.usuario.username

# EQUIPO
class Equipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=100)
    fundacion = models.IntegerField(help_text="Año de fundación")
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

# JUGADOR
class Jugador(models.Model):
    POSICIONES = [
        ('POR', 'Portero'),
        ('DEF', 'Defensa'),
        ('MED', 'Centrocampista'),
        ('DEL', 'Delantero'),
    ]
    nombre = models.CharField(max_length=100)
    dorsal = models.IntegerField()
    posicion = models.CharField(max_length=3, choices=POSICIONES)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")

    def __str__(self):
        return f"{self.nombre} ({self.equipo.nombre})"

# ESTADIO
class Estadio(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre

# PARTIDO
class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_local")
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_visitante")
    estadio = models.ForeignKey(Estadio, on_delete=models.PROTECT)
    fecha = models.DateField()
    jornada = models.IntegerField()
    jugadores = models.ManyToManyField(Jugador, through='Participacion')

    class Meta:
        ordering = ['-fecha']
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"

# PARTICIPACIÓN (Tabla intermedia N:M)
class Participacion(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    goles = models.IntegerField(default=0)
    minutos_jugados = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['jugador', 'partido'], name='unique_jugador_partido')
        ]

    def __str__(self):
        return f"{self.jugador.nombre} en {self.partido}"