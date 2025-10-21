from django.contrib import admin
from .models import Dispositivo, Mantenimiento, Muestra, RegistroEstado

# Register your models here.
@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "modelo", "ubicacion", "estado")
    search_fields = ("nombre", "modelo", "numero_serie")
    list_filter = ("estado",)
    filter_horizontal = ("usuarios",)  # permite seleccionar usuarios fácilmente

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ("dispositivo", "tipo_evento", "fecha_hora")
    list_filter = ("tipo_evento",)

@admin.register(Muestra)
class MuestraAdmin(admin.ModelAdmin):
    list_display = ("dispositivo", "tipo_muestra", "fecha_hora", "estado")
    list_filter = ("tipo_muestra", "estado")

@admin.register(RegistroEstado)
class RegistroEstadoAdmin(admin.ModelAdmin):
    list_display = ("dispositivo", "fecha_hora", "nivel_bateria", "en_linea")
    list_filter = ("en_linea",)