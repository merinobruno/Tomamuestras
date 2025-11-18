from django.urls import path
from AppTomamuestras import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('deseleccionar/', views.deseleccionar_dispositivo, name='deseleccionar_dispositivo'),
    path("muestra/nueva/<int:dispositivo_id>/", views.crear_muestra, name="crear_muestra"),
    path("mantenimiento/nuevo/<int:dispositivo_id>/", views.crear_mantenimiento, name="crear_mantenimiento"),
    path("registro/nuevo/<int:dispositivo_id>/", views.crear_registro, name="crear_registro"),
    path("muestra/eliminar/<int:pk>/", views.eliminar_muestra, name="eliminar_muestra"),
    path("mantenimiento/eliminar/<int:pk>/", views.eliminar_mantenimiento, name="eliminar_mantenimiento"),
    path("registro/eliminar/<int:pk>/", views.eliminar_registro, name="eliminar_registro"),

]