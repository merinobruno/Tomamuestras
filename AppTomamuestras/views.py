from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Dispositivo, Muestra, Mantenimiento, RegistroEstado
from django.views.decorators.cache import cache_control
from .forms import MuestraForm, MantenimientoForm, RegistroEstadoForm
from django.http import HttpResponseForbidden


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def dashboard(request):
    if request.user.is_superuser:
        dispositivos = Dispositivo.objects.all()
    else:
        dispositivos = request.user.dispositivos_asignados.all()

    dispositivo_id = request.GET.get('dispositivo')
    dispositivo = dispositivos.filter(id=dispositivo_id).first() if dispositivo_id else None

    if dispositivo:
        muestras = Muestra.objects.filter(dispositivo=dispositivo)
        mantenimientos = Mantenimiento.objects.filter(dispositivo=dispositivo)
        registros = RegistroEstado.objects.filter(dispositivo=dispositivo)
    else:
        muestras = Muestra.objects.filter(dispositivo__in=dispositivos)
        mantenimientos = Mantenimiento.objects.filter(dispositivo__in=dispositivos)
        registros = RegistroEstado.objects.filter(dispositivo__in=dispositivos)

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


def verificar_permiso(request, dispositivo):
    return request.user.is_superuser or dispositivo in request.user.dispositivos_asignados.all()



# ---------------------------------------------------
#               CREAR MUESTRA
# ---------------------------------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def crear_muestra(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if not verificar_permiso(request, dispositivo):
        return HttpResponseForbidden()

    if request.method == "POST":
        form = MuestraForm(request.POST, dispositivo_id=dispositivo_id)
        if form.is_valid():
            m = form.save(commit=False)
            m.dispositivo = dispositivo
            m.save()
            return redirect(f'/dashboard/?dispositivo={dispositivo_id}')
    else:
        form = MuestraForm(dispositivo_id=dispositivo_id)

    return render(request, "formularios/muestra_form.html", {
        "form": form,
        "titulo": "Nueva Muestra"
    })



# ---------------------------------------------------
#           CREAR MANTENIMIENTO
# ---------------------------------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def crear_mantenimiento(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if not verificar_permiso(request, dispositivo):
        return HttpResponseForbidden()

    if request.method == "POST":
        form = MantenimientoForm(request.POST, dispositivo_id=dispositivo_id)
        if form.is_valid():
            mt = form.save(commit=False)
            mt.dispositivo = dispositivo
            mt.save()
            return redirect(f'/dashboard/?dispositivo={dispositivo_id}')
    else:
        form = MantenimientoForm(dispositivo_id=dispositivo_id)

    return render(request, "formularios/generico_form.html", {
        "form": form,
        "titulo": "Nuevo Mantenimiento"
    })



# ---------------------------------------------------
#           CREAR REGISTRO DE ESTADO
# ---------------------------------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def crear_registro(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if not verificar_permiso(request, dispositivo):
        return HttpResponseForbidden()

    if request.method == "POST":
        form = RegistroEstadoForm(request.POST, dispositivo_id=dispositivo_id)
        if form.is_valid():
            r = form.save(commit=False)
            r.dispositivo = dispositivo
            r.save()
            return redirect(f'/dashboard/?dispositivo={dispositivo_id}')
    else:
        form = RegistroEstadoForm(dispositivo_id=dispositivo_id)

    return render(request, "formularios/generico_form.html", {
        "form": form,
        "titulo": "Nuevo Registro de Estado"
    })



# ---------------------------------------------------
#           ELIMINAR REGISTROS
# ---------------------------------------------------
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def eliminar_muestra(request, pk):
    muestra = get_object_or_404(Muestra, pk=pk)
    if not verificar_permiso(request, muestra.dispositivo):
        return redirect('dashboard')

    dispositivo_id = muestra.dispositivo.id
    muestra.delete()
    return redirect(f'/dashboard/?dispositivo={dispositivo_id}')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def eliminar_mantenimiento(request, pk):
    mantenimiento = get_object_or_404(Mantenimiento, pk=pk)
    if not verificar_permiso(request, mantenimiento.dispositivo):
        return redirect('dashboard')

    dispositivo_id = mantenimiento.dispositivo.id
    mantenimiento.delete()
    return redirect(f'/dashboard/?dispositivo={dispositivo_id}')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def eliminar_registro(request, pk):
    registro = get_object_or_404(RegistroEstado, pk=pk)
    if not verificar_permiso(request, registro.dispositivo):
        return redirect('dashboard')

    dispositivo_id = registro.dispositivo.id
    registro.delete()
    return redirect(f'/dashboard/?dispositivo={dispositivo_id}')
