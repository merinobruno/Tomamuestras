from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dispositivo, Muestra, Mantenimiento, RegistroEstado
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def dashboard(request):
    # Si el usuario es superusuario, ve todos los dispositivos
    if request.user.is_superuser:
        dispositivos = Dispositivo.objects.all()
    else:
        dispositivos = request.user.dispositivos_asignados.all()

    dispositivo_id = request.GET.get('dispositivo')
    dispositivo = dispositivos.filter(id=dispositivo_id).first() if dispositivo_id else None

    if dispositivo:
        # Mostrar datos del dispositivo seleccionado
        muestras = Muestra.objects.filter(dispositivo=dispositivo)
        mantenimientos = Mantenimiento.objects.filter(dispositivo=dispositivo)
        registros = RegistroEstado.objects.filter(dispositivo=dispositivo)
    else:
        # Mostrar totales globales (solo de sus dispositivos)
        muestras = Muestra.objects.filter(dispositivo__in=dispositivos)
        mantenimientos = Mantenimiento.objects.filter(dispositivo__in=dispositivos)
        registros = RegistroEstado.objects.filter(dispositivo__in=dispositivos)

    # Contador de dispositivos activos
    activos_count = dispositivos.filter(estado="Activo").count()

    context = {
        'dispositivo': dispositivo,
        'dispositivos': dispositivos,
        'muestras': muestras,
        'mantenimientos': mantenimientos,
        'registros': registros,
        'activos_count': activos_count,
    }
    return render(request, 'dashboard.html', context)


def deseleccionar_dispositivo(request):
    if 'dispositivo_id' in request.session:
        del request.session['dispositivo_id']
    return redirect('dashboard')