from django.db import models
from django.contrib.auth.models import User

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    numero_serie = models.CharField(max_length=50, blank=True, null=True)
    fecha_instalacion = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)

    # 🔹 relación con usuarios: un dispositivo puede tener varios usuarios, y un usuario puede tener varios dispositivos
    usuarios = models.ManyToManyField(User, related_name="dispositivos_asignados", blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.modelo})"


class Mantenimiento(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='mantenimientos')
    fecha_hora = models.DateTimeField()
    tipo_evento = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_evento} - {self.dispositivo.nombre}"


class Muestra(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='muestras')
    fecha_hora = models.DateTimeField()
    contenedor_id = models.CharField(max_length=50, blank=True, null=True)
    volumen_ml = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipo_muestra = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Muestra {self.id} - {self.tipo_muestra}"


class RegistroEstado(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='registros')
    fecha_hora = models.DateTimeField()
    nivel_bateria = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    en_linea = models.BooleanField(default=True)
    ultima_conexion = models.DateTimeField(blank=True, null=True)
    codigo_error = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Estado {self.fecha_hora} - {self.dispositivo.nombre}"