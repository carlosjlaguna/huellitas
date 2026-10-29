from django.shortcuts import render

def home_view(request):
    # Vista pública para Visitantes y usuarios generales
    return render(request, 'usuarios/home.html')

def login_view(request):
    # Lógica de inicio de sesión
    return render(request, 'usuarios/login.html')

def register_view(request):
    # Lógica de registro de nuevos usuarios
    return render(request, 'usuarios/registro.html')
