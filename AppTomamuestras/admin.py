from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import Dispositivo


# ==============================
#    CUSTOM ADMIN SITE
# ==============================
class CustomAdminSite(admin.AdminSite):
    site_header = "Panel de Administración"
    site_title = "Administración"
    index_title = "Dashboard del Sistema"

    class Media:
        css = {
            "all": ("admin/custom_admin.css",)
        }

custom_admin_site = CustomAdminSite(name="custom_admin")


# ==============================
#    USER ADMIN PERSONALIZADO
# ==============================
class CustomUserChangeForm(forms.ModelForm):
    dispositivos_asignados = forms.ModelMultipleChoiceField(
        queryset=Dispositivo.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = User
        fields = [
            "username", "first_name", "last_name", "email",
            "is_staff", "is_active", "dispositivos_asignados"
        ]


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    show_full_history = False

    def has_history_permission(self, request, obj=None):
        return False

    fieldsets = (
        ("", {
            "classes": ("wide",),
            "fields": (
                "username",
                "first_name",
                "last_name",
                "email",
                "is_staff",
                "is_active",
            ),
        }),
    )

    add_fieldsets = (
        ("", {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2",
                "first_name", "last_name", "email",
                "is_staff", "is_active",
            ),
        }),
    )

    list_display = ("username", "is_staff", "is_active")



# Registrar usuario en admin personalizado
custom_admin_site.register(User, CustomUserAdmin)


# ==============================
#    DISPOSITIVO ADMIN
# ==============================
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'modelo', 'estado')
    search_fields = ('nombre', 'modelo', 'numero_serie')

    fieldsets = (
        ("", {
            "classes": ("wide",),
            "fields": (
                "nombre",
                "ubicacion",
                "modelo",
                "numero_serie",
                "fecha_instalacion",
                "estado",
                "usuarios",
            )
        }),
    )

    filter_horizontal = ('usuarios',)

    show_full_history = False

    def has_history_permission(self, request, obj=None):
        return False


custom_admin_site.register(Dispositivo, DispositivoAdmin)
