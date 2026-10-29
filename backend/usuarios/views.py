from django.shortcuts import render

# VISTAS DE LA APLICACIÓN USUARIOS - HUELLITAS

def home_view(request):
    """
    Controlador para la vista principal de la plataforma.
    
    Parámetros:
        request (HttpRequest): Objeto que contiene los metadatos de la solicitud web.
        
    Retorna:
        HttpResponse: Renderiza la plantilla 'usuarios/home.html' con el catálogo inicial.
    """
    # Genera la página de bienvenida y catálogo público de mascotas
    return render(request, 'usuarios/home.html')

def login_view(request):
    """
    Controlador para la autenticación de usuarios del sistema.
    
    Parámetros:
        request (HttpRequest): Objeto de la solicitud web enviada por el cliente.
        
    Retorna:
        HttpResponse: Renderiza el formulario de inicio de sesión ('usuarios/login.html').
    """
    # Genera la vista de inicio de sesión para los diferentes roles (Adoptante, Gestor, Admin)
    return render(request, 'usuarios/login.html')

def registro_view(request):
    """
    Controlador para el registro de nuevos usuarios (Adoptantes).
    
    Parámetros:
        request (HttpRequest): Objeto de la solicitud web.
        
    Retorna:
        HttpResponse: Renderiza el formulario de registro ('usuarios/registro.html').
    """
    # Genera la vista de registro de cuentas nuevas en la plataforma Huellitas
    return render(request, 'usuarios/registro.html')