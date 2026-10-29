# Proyecto Huellitas

# Huellitas - Plataforma de Adopción y Seguimiento de Mascotas

Sistema web integral para digitalizar y centralizar el proceso de adopción de mascotas y realizar el seguimiento posterior a la adopción.


## Fase Descendente de la Metodología en V

### 1. Análisis de Requisitos (Requirement Gathering)
- **Problema a resolver:** Los refugios o rescatistas gestionan las adopciones mediante formularios en papel, publicaciones o chats desordenados, perdiendo el rastreo de los animales adoptados.
- **Funcionalidades del Sistema:**
  * **Catálogo interactivo:** Filtros por especie (perro/gato), edad, tamaño y compatibilidad.
  * **Cuestionario de adopción:** Formulario dinámico para evaluar la aptitud del solicitante.
  * **Bitácora de seguimiento:** El adoptante sube fotos y reportes de salud periódicos.
  * **Panel de gestión:** Aprobación o rechazo de solicitudes con notas del rescatista.

### 2. Análisis del Sistema (System Analysis)
- **Comportamiento General:**
  1. El usuario **Visitante** explora el catálogo sin registrarse.
  2. Si quiere adoptar, se registra como **Usuario (Adoptante)** y envía una solicitud.
  3. El **Gestor (Rescatista/Refugio)** evalúa las respuestas y cambia el estado a *Aprobada* o *Rechazada*.
  4. Si se aprueba, la mascota pasa a estado *Adoptada* y se habilita el módulo de seguimiento.
  5. El **Administrador** gestiona cuentas, roles y métricas globales.

### 3. Diseño de Software / Arquitectura (Software Design)
- **Backend:** Python + Django (Manejo de rutas, lógica de adopción y seguridad).
- **Frontend:** Vite.js (Compilación rápida de interfaz y hojas de estilo).
- **Base de Datos:** MySQL 8.0 (Gestión relacional de datos de usuarios, mascotas y adopciones).
- **Contenedorización:** Docker & Docker Compose (Entorno aislado en puerto de host 3307 para MySQL).

### 4. Diseño de Módulos (Module Design)
El proyecto se divide en las siguientes aplicaciones dentro de Django:
- `usuarios`: Gestión de roles (**Administrador, Gestor, Usuario, Visitante**) y autenticación.
- `mascotas`: Registro de mascotas (nombre, especie, foto, vacunas, estado de salud).
- `adopciones`: Lógica de formularios de adopción y almacenamiento del historial de seguimiento.

### 5. Punto de Inflexión: Codificación (Coding)
Pase a la fase práctica: construcción del código fuente sobre la arquitectura en Docker y control de versiones en GitHub.


## Matriz de Roles y Privilegios

| Rol | Vistas / Funcionalidades Permitidas |
| :--- | :--- |
| **Visitante** | Ver catálogo público de mascotas, filtrar por especie/edad, ver formulario de registro. |
| **Usuario (Adoptante)** | Iniciar sesión, enviar solicitudes de adopción, ver estado de sus solicitudes, subir fotos de seguimiento. |
| **Gestor (Rescatista)** | Publicar/editar mascotas, revisar y aprobar/rechazar solicitudes, verificar bitácora de seguimiento. |
| **Administrador** | Acceso total al panel Django Admin, gestión global de usuarios, roles, métricas y base de datos. |


## Estructura del Proyecto

```text
huellitas/
├── backend/
│   ├── core/           # Configuración base de Django
│   ├── usuarios/       # Módulo de autenticación y roles
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/           # Aplicación frontend con Vite.js
├── docker-compose.yml  # Configuración de servicios Docker (Django + MySQL)
└── README.md


## Entregable: Infografía

A continuación se presenta la infografía resumen que plasma la metodología en V (fase descendente), el stack tecnológico y la matriz de roles del sistema Huellitas:
<img width="1600" height="2800" alt="infografia-m1" src="https://github.com/user-attachments/assets/05a37293-8eb7-4ea2-89de-a20d29aeedd9" />

También puedes descargar la versión en alta calidad en formato PDF haciendo clic abajo:
[infografia-m1-pdf.pdf](https://github.com/user-attachments/files/34158843/infografia-m1-pdf.pdf)
