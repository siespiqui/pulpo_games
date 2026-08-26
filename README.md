# Pulpo Games 🐙🎮

Repositorio oficial del proyecto **Pulpo Games**, desarrollado como parte de las actividades académicas de la ficha **3321349** del Servicio Nacional de Aprendizaje (**SENA**). Este sistema está construído como una aplicación web modular utilizando Django.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.14.3
* **Framework Web:** Django (versión 6.1)
* **Base de datos:** SQLite3
* **Control de versiones:** Git y GitHub

---

## 📂 Estructura del Proyecto

El proyecto está organizado en las siguientes aplicaciones de Django para gestionar los distintos módulos de la plataforma:

* `almacenamiento/` - Gestión de almacenamiento y stock.
* `compras/` - Registro y control de compras de productos.
* `compras_segunda_mano/` - Módulo para artículos usados o de segunda mano.
* `inventario/` - Control general del inventario (videojuegos, consolas, TCG, etc.).
* `mantenimiento/` - Registro de soporte y mantenimiento de equipos.
* `proteccion_datos/` - Políticas y manejo de datos de los usuarios.
* `proveedores/` - Gestión de proveedores de la tienda.
* `reservas/` - Apartado para la reserva de productos.
* `reseñas/` - Opiniones y valoraciones de los usuarios.
* `seguridad_confidencialidad/` - Módulos de seguridad y acceso.
* `usuarios/` - Gestión de cuentas, roles y perfiles.

---

## 🚀 Guía de Instalación y Configuración (Paso a Paso)

Sigue estos pasos en tu terminal (CMD, PowerShell o Bash) para clonar el proyecto y ponerlo a marchar en tu equipo local:

### 1. Clonar el repositorio
Abre tu terminal en la carpeta donde quieras guardar el proyecto y ejecuta:
```bash
git clone [https://github.com/siespiqui/pulpo.git](https://github.com/siespiqui/pulpo.git)
cd pulpo
(Nota: Si el código fuente principal se encuentra dentro de una subcarpeta, navega a ella según corresponda).

2. Crear y activar un entorno virtual
Es una buena práctica aislar las dependencias del proyecto:

Bash
python -m venv venv
En Windows:

Bash
venv\Scripts\activate
En macOS / Linux:

Bash
source venv/bin/activate
3. Aplicar las migraciones de la base de datos
Configura la base de datos local ejecutando:

Bash
python manage.py makemigrations
python manage.py migrate
4. Crear un superusuario (Opcional, para entrar al panel de administración)
Bash
python manage.py createsuperuser
(Sigue los pasos en pantalla para asignarle un nombre de usuario, correo y contraseña).

5. Ejecutar el servidor de desarrollo
Bash
python manage.py runserver
Una vez hecho esto, abre tu navegador web de preferencia y entra a http://127.0.0.1:8000/ para ver la aplicación funcionando.

👥 Autores y Colaboradores
Proyecto desarrollado de forma colaborativa para la ficha 3321349 (SENA 2026):

Simón Esteban Pineda Quiroga (siespiqui)

Daniels2311 (Daniels2311)

José Manuel Espitia Romero (espitiaromerojosemanuel91-wq)
