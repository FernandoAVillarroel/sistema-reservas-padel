# Guía de Instalación Rápida

## Paso 1: Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd padel-booking-system
```

## Paso 2: Instalar dependencias
```bash
pip install -r requirements.txt
```

## Paso 3: Configurar MySQL

### Opción A: Crear base de datos manualmente
```sql
CREATE DATABASE padel_booking CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'padel_user'@'localhost' IDENTIFIED BY 'tu_contraseña';
GRANT ALL PRIVILEGES ON padel_booking.* TO 'padel_user'@'localhost';
FLUSH PRIVILEGES;
```

### Opción B: Usar credenciales root (para desarrollo)
Editar `padel_backend/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'padel_booking',
        'USER': 'root',
        'PASSWORD': 'TU_PASSWORD_MYSQL',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Paso 4: Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

## Paso 5: Crear datos iniciales
```bash
python manage.py shell < setup_initial_data.py
```

Este script crea:
- 1 usuario administrador
- 1 usuario encargado  
- 1 usuario cliente
- 3 canchas de ejemplo
- Horarios (Lunes a Domingo, 8:00 - 23:00)
- Precios (día y noche)

## Paso 6: Ejecutar servidor
```bash
python manage.py runserver
```

## Accesos
- **API**: http://localhost:8000/api/
- **Admin**: http://localhost:8000/admin/

### Credenciales
**Admin:**
- Usuario: `admin`
- Contraseña: `admin123`

**Encargado:**
- Usuario: `encargado`
- Contraseña: `encargado123`

**Cliente:**
- Usuario: `cliente1`
- Contraseña: `cliente123`

## Verificar instalación

### Probar API
```bash
# Listar canchas (no requiere autenticación)
curl http://localhost:8000/api/courts/

# Login
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

## Solución de Problemas

### Error: No module named 'pymysql'
```bash
pip install pymysql --break-system-packages
```

### Error: MySQL connection refused
Verificar que MySQL esté corriendo:
```bash
# Ubuntu/Debian
sudo service mysql start

# macOS
mysql.server start
```

### Error: Access denied for user
Verificar credenciales en `settings.py` y que el usuario tenga permisos.

## Siguiente Paso
Una vez instalado, puedes:
1. Acceder al panel admin para gestionar datos
2. Probar los endpoints del API
3. Comenzar a desarrollar el frontend
