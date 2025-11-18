from django import forms
from .models import Muestra, Mantenimiento, RegistroEstado, Dispositivo

class BaseStyledForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "styled-input",
            })


class MuestraForm(BaseStyledForm):
    def __init__(self, *args, dispositivo_id=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Filtrar dispositivo
        if dispositivo_id:
            self.fields['dispositivo'].queryset = Dispositivo.objects.filter(id=dispositivo_id)

    class Meta:
        model = Muestra
        fields = "__all__"
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class MantenimientoForm(BaseStyledForm):
    def __init__(self, *args, dispositivo_id=None, **kwargs):
        super().__init__(*args, **kwargs)

        if dispositivo_id:
            self.fields['dispositivo'].queryset = Dispositivo.objects.filter(id=dispositivo_id)

    class Meta:
        model = Mantenimiento
        fields = "__all__"
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class RegistroEstadoForm(BaseStyledForm):
    def __init__(self, *args, dispositivo_id=None, **kwargs):
        super().__init__(*args, **kwargs)

        if dispositivo_id:
            self.fields['dispositivo'].queryset = Dispositivo.objects.filter(id=dispositivo_id)

    class Meta:
        model = RegistroEstado
        fields = "__all__"
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'ultima_conexion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
