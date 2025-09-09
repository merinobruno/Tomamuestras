from django.shortcuts import get_object_or_404, render
from AppTomamuestras.models import Dispositivo, Muestra, Mantenimiento, RegistroEstado

# Create your views here.

def dashboard(request):
    dispositivos = Dispositivo.objects.all()
    selected_id = request.GET.get('dispositivo')  # captura el dispositivo seleccionado
    dispositivo = None
    muestras = []
    mantenimientos = []
    registros = []

    if selected_id:
        dispositivo = get_object_or_404(Dispositivo, id=selected_id)
        muestras = Muestra.objects.filter(dispositivo=dispositivo)
        mantenimientos = Mantenimiento.objects.filter(dispositivo=dispositivo)
        registros = RegistroEstado.objects.filter(dispositivo=dispositivo)

    context = {
        'dispositivos': dispositivos,
        'dispositivo': dispositivo,
        'muestras': muestras,
        'mantenimientos': mantenimientos,
        'registros': registros,
    }
    return render(request, 'AppTomamuestras/dashboard.html', context)