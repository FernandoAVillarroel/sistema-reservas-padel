# Sistema de Gestión de Turnos para Canchas de Pádel

**Desarrollado por:** Fernando Agustín Villarroel  
**Ubicación:** Santiago del Estero, Argentina  
**Contacto:** [LinkedIn](https://www.linkedin.com/in/fernando-villarroel-a635a431b/) | agustinvillarroel17@gmail.com

---

## 💡 Motivación del Proyecto

Este sistema nació después de identificar las dificultades que tienen los complejos de canchas de pádel en Santiago del Estero para gestionar reservas eficientemente. La mayoría aún depende de métodos manuales como cuadernos, planillas de Excel o grupos de WhatsApp, lo que genera:

- ❌ Conflictos de horarios y reservas duplicadas
- ❌ Dificultad para rastrear pagos y comprobantes
- ❌ Falta de histórico y reportes
- ❌ Mala experiencia para los clientes

Comencé este proyecto como una solución personal para aprender Django REST Framework en profundidad, pero al analizar el potencial comercial decidí desarrollarlo como un sistema robusto y profesional, listo para implementarse en canchas reales.

El sistema está diseñado específicamente para el mercado argentino, con soporte para métodos de pago locales (transferencia, efectivo, Mercado Pago) y adaptado a las necesidades particulares de gestión de complejos deportivos.

---

Sistema completo de gestión de turnos adaptado para dispositivos móviles, donde los usuarios pueden reservar canchas de pádel y los encargados pueden aprobar reservas por transferencia.

## 🏗️ Tecnologías Utilizadas

### Backend
- **Python** con **Django 5.2.8**
- **Django REST Framework** para API REST
- **PyMySQL** para conexión con MySQL
- **django-filter** para filtrado avanzado
- **django-cors-headers** para CORS

### Base de Datos
- **MySQL**

### Frontend (Próximamente)
- **JavaScript**
- **Vue.js**
- **CSS**
- **Tailwind CSS**

## 📋 Características

### Usuarios
- ✅ Sistema de autenticación (login/logout)
- ✅ Tres roles: Administrador, Encargado, Cliente
- ✅ Registro de usuarios
- ✅ Gestión de perfil

### Canchas
- ✅ Gestión de canchas de pádel
- ✅ Horarios configurables por día
- ✅ Sistema de precios por horario
- ✅ Canchas techadas/destechadas
- ✅ Control de iluminación

### Reservas
- ✅ Crear reservas con validación de disponibilidad
- ✅ Aprobar/rechazar reservas (Encargados)
- ✅ Cancelar reservas
- ✅ Múltiples métodos de pago (Transferencia, Efectivo, Tarjeta, Mercado Pago)
- ✅ Subir comprobante de pago
- ✅ Historial completo de cambios
- ✅ Estados: Pendiente, Confirmada, Cancelada, Completada

## 🚀 Instalación y Configuración

### Prerrequisitos
```bash
- Python 3.8+
- MySQL 5.7+
- pip
```

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd padel-booking-system
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar base de datos MySQL
Crear la base de datos en MySQL:
```sql
CREATE DATABASE padel_booking CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Editar `padel_backend/settings.py` con tus credenciales de MySQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'padel_booking',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario
```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor de desarrollo
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`
Panel de administración: `http://localhost:8000/admin`

## 📡 API Endpoints

### Autenticación
- `POST /api/users/login/` - Login
- `POST /api/users/logout/` - Logout
- `GET /api/users/me/` - Obtener usuario actual

### Usuarios
- `GET /api/users/` - Listar usuarios
- `POST /api/users/` - Crear usuario
- `GET /api/users/{id}/` - Detalle de usuario
- `PUT /api/users/{id}/` - Actualizar usuario
- `DELETE /api/users/{id}/` - Eliminar usuario

### Canchas
- `GET /api/courts/` - Listar canchas
- `POST /api/courts/` - Crear cancha
- `GET /api/courts/{id}/` - Detalle de cancha
- `PUT /api/courts/{id}/` - Actualizar cancha
- `DELETE /api/courts/{id}/` - Eliminar cancha
- `GET /api/courts/{id}/available_slots/?date=YYYY-MM-DD` - Horarios disponibles

### Horarios de Canchas
- `GET /api/schedules/` - Listar horarios
- `POST /api/schedules/` - Crear horario
- `GET /api/schedules/{id}/` - Detalle de horario
- `PUT /api/schedules/{id}/` - Actualizar horario
- `DELETE /api/schedules/{id}/` - Eliminar horario

### Precios
- `GET /api/pricings/` - Listar precios
- `POST /api/pricings/` - Crear precio
- `GET /api/pricings/{id}/` - Detalle de precio
- `PUT /api/pricings/{id}/` - Actualizar precio
- `DELETE /api/pricings/{id}/` - Eliminar precio

### Reservas
- `GET /api/bookings/` - Listar reservas
- `POST /api/bookings/` - Crear reserva
- `GET /api/bookings/{id}/` - Detalle de reserva
- `PUT /api/bookings/{id}/` - Actualizar reserva
- `DELETE /api/bookings/{id}/` - Eliminar reserva
- `POST /api/bookings/{id}/confirm/` - Confirmar reserva (Encargado)
- `POST /api/bookings/{id}/cancel/` - Cancelar reserva
- `GET /api/bookings/my_bookings/` - Mis reservas
- `GET /api/bookings/pending/` - Reservas pendientes (Encargado)

### Historial de Reservas
- `GET /api/booking-history/` - Listar historial
- `GET /api/booking-history/{id}/` - Detalle de historial

## 🗂️ Estructura del Proyecto

```
padel-booking-system/
├── padel_backend/          # Configuración principal del proyecto
│   ├── settings.py         # Configuración de Django
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # WSGI config
├── users/                 # App de usuarios
│   ├── models.py          # Modelo User personalizado
│   ├── serializers.py     # Serializers de usuarios
│   ├── views.py           # Vistas/ViewSets
│   └── admin.py           # Configuración del admin
├── courts/                # App de canchas
│   ├── models.py          # Modelos Court, CourtSchedule, Pricing
│   ├── serializers.py     # Serializers de canchas
│   ├── views.py           # Vistas/ViewSets
│   └── admin.py           # Configuración del admin
├── bookings/              # App de reservas
│   ├── models.py          # Modelos Booking, BookingHistory
│   ├── serializers.py     # Serializers de reservas
│   ├── views.py           # Vistas/ViewSets
│   └── admin.py           # Configuración del admin
├── media/                 # Archivos subidos (comprobantes)
├── staticfiles/           # Archivos estáticos
├── manage.py             # Script de gestión de Django
├── requirements.txt       # Dependencias del proyecto
├── .gitignore            # Archivos ignorados por git
└── README.md             # Este archivo
```

## 🔐 Roles y Permisos

### Administrador
- Acceso completo al sistema
- Gestión de usuarios, canchas y reservas
- Acceso al panel de administración

### Encargado
- Ver todas las reservas
- Confirmar/rechazar reservas pendientes
- Gestionar canchas y horarios
- Ver comprobantes de pago

### Cliente
- Crear reservas
- Ver sus propias reservas
- Cancelar sus reservas
- Subir comprobantes de pago

## 📱 Próximos Pasos

- [ ] Desarrollar frontend con Vue.js
- [ ] Implementar sistema de notificaciones
- [ ] Agregar dashboard de estadísticas
- [ ] Sistema de recordatorios por email/SMS
- [ ] Integración con pasarelas de pago
- [ ] App móvil nativa

## 👥 Contribuciones

Este es un proyecto en desarrollo. Las contribuciones son bienvenidas.

## 📞 Contacto

Para consultas sobre el proyecto o propuestas comerciales:

**Fernando Agustín Villarroel**
- 📧 Email: agustinvillarroel17@gmail.com
- 💼 LinkedIn: [Fernando Villarroel](https://www.linkedin.com/in/fernando-villarroel-a635a431b/)
- 📍 Santiago del Estero, Argentina

---

## 🎓 Aprendizajes y Desafíos

Durante el desarrollo de este proyecto, enfrenté y resolví varios desafíos técnicos:

1. **Validación de disponibilidad**: Implementar un sistema que previene reservas duplicadas considerando rangos de tiempo superpuestos
2. **Sistema de precios dinámico**: Crear un modelo flexible que permite diferentes precios según horario y día
3. **Gestión de permisos**: Diseñar un sistema de roles que permite diferentes niveles de acceso (Admin/Encargado/Cliente)
4. **Historial de auditoría**: Implementar tracking completo de cambios en las reservas para transparencia
5. **API REST escalable**: Diseñar endpoints pensando en el consumo desde múltiples frontends (web, mobile)

## 📄 Licencia

Este proyecto es de código abierto.

## 🐛 Reporte de Bugs

Si encuentras algún bug o tienes sugerencias, por favor crea un issue en el repositorio.

## 📞 Contacto

Para consultas sobre el proyecto, puedes contactarnos a través del repositorio de GitHub.
