from django.urls import path
from AppTomamuestras import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('deseleccionar/', views.deseleccionar_dispositivo, name='deseleccionar_dispositivo'),

]