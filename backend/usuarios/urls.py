from django.urls import path
from . import views

# RUTAS / PUNTOS DE ACCESO DE LA APLICACIÓN USUARIOS
# este archivo define los patrones de URL que enrutan
# cada petición del cliente hacia su respectiva vista en el archivo views.py

urlpatterns = [
    # Ruta para la página principal y catálogo de mascotas
    path('', views.home_view, name='home'),
    
    # Ruta para el formulario de inicio de sesión
    path('login/', views.login_view, name='login'),
    
    # Ruta para el formulario de registro de nuevos usuarios
    path('registro/', views.registro_view, name='registro'),
]