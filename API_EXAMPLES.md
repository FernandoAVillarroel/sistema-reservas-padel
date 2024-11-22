# Ejemplos de Uso del API

## Autenticación

### Login
```bash
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "admin123"
  }'
```

**Respuesta exitosa:**
```json
{
  "message": "Login exitoso",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@padel.com",
    "first_name": "Admin",
    "last_name": "Sistema",
    "phone": "",
    "role": "admin",
    "is_active": true,
    "created_at": "2024-01-15 10:30:00",
    "updated_at": "2024-01-15 10:30:00"
  }
}
```

### Obtener usuario actual
```bash
curl http://localhost:8000/api/users/me/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

### Logout
```bash
curl -X POST http://localhost:8000/api/users/logout/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

---

## Usuarios

### Crear nuevo usuario (registro)
```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "nuevo_cliente",
    "email": "nuevo@example.com",
    "password": "segura123",
    "password2": "segura123",
    "first_name": "Pedro",
    "last_name": "Martínez",
    "phone": "3815559999",
    "role": "customer"
  }'
```

### Listar usuarios
```bash
curl http://localhost:8000/api/users/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

---

## Canchas

### Listar todas las canchas (público)
```bash
curl http://localhost:8000/api/courts/
```

**Respuesta:**
```json
[
  {
    "id": 1,
    "name": "Cancha 1",
    "description": "Cancha principal techada con iluminación LED",
    "is_active": true,
    "is_covered": true,
    "has_lighting": true
  },
  {
    "id": 2,
    "name": "Cancha 2",
    "description": "Cancha al aire libre con iluminación",
    "is_active": true,
    "is_covered": false,
    "has_lighting": true
  }
]
```

### Ver detalle de una cancha con horarios y precios
```bash
curl http://localhost:8000/api/courts/1/
```

**Respuesta:**
```json
{
  "id": 1,
  "name": "Cancha 1",
  "description": "Cancha principal techada con iluminación LED",
  "is_active": true,
  "is_covered": true,
  "has_lighting": true,
  "created_at": "2024-01-15 10:30:00",
  "updated_at": "2024-01-15 10:30:00",
  "schedules": [
    {
      "id": 1,
      "court": 1,
      "day_of_week": 0,
      "day_name": "Lunes",
      "opening_time": "08:00:00",
      "closing_time": "23:00:00",
      "slot_duration": 60
    }
  ],
  "pricings": [
    {
      "id": 1,
      "court": 1,
      "start_time": "08:00:00",
      "end_time": "18:00:00",
      "price": "8000.00",
      "is_active": true
    },
    {
      "id": 2,
      "court": 1,
      "start_time": "18:00:00",
      "end_time": "23:00:00",
      "price": "12000.00",
      "is_active": true
    }
  ]
}
```

### Crear cancha (requiere autenticación)
```bash
curl -X POST http://localhost:8000/api/courts/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "name": "Cancha 4",
    "description": "Nueva cancha techada",
    "is_covered": true,
    "has_lighting": true,
    "is_active": true
  }'
```

### Filtrar canchas
```bash
# Canchas techadas
curl "http://localhost:8000/api/courts/?is_covered=true"

# Canchas activas con iluminación
curl "http://localhost:8000/api/courts/?is_active=true&has_lighting=true"

# Buscar por nombre
curl "http://localhost:8000/api/courts/?search=Cancha%201"
```

---

## Reservas

### Crear una reserva
```bash
curl -X POST http://localhost:8000/api/bookings/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "court": 1,
    "date": "2024-01-20",
    "start_time": "18:00",
    "end_time": "19:00",
    "duration": 60,
    "price": 12000.00,
    "payment_method": "transfer",
    "player_name": "Juan Pérez",
    "player_phone": "3815551234",
    "notes": "Reserva para partido amistoso"
  }'
```

**Respuesta exitosa:**
```json
{
  "id": 1,
  "user": 3,
  "user_detail": {
    "id": 3,
    "username": "cliente1",
    "email": "cliente1@padel.com",
    "first_name": "María",
    "last_name": "González"
  },
  "court": 1,
  "court_detail": {
    "id": 1,
    "name": "Cancha 1",
    "description": "Cancha principal techada con iluminación LED"
  },
  "date": "2024-01-20",
  "start_time": "18:00:00",
  "end_time": "19:00:00",
  "duration": 60,
  "price": "12000.00",
  "payment_method": "transfer",
  "payment_method_display": "Transferencia",
  "payment_proof": null,
  "status": "pending",
  "status_display": "Pendiente",
  "notes": "Reserva para partido amistoso",
  "player_name": "Juan Pérez",
  "player_phone": "3815551234",
  "created_at": "2024-01-15 15:30:00",
  "updated_at": "2024-01-15 15:30:00",
  "confirmed_at": null,
  "cancelled_at": null,
  "history": [
    {
      "id": 1,
      "booking": 1,
      "user": 3,
      "user_name": "María González",
      "action": "Creada",
      "old_status": "",
      "new_status": "pending",
      "notes": "Reserva creada",
      "created_at": "2024-01-15 15:30:00"
    }
  ]
}
```

### Listar mis reservas
```bash
curl http://localhost:8000/api/bookings/my_bookings/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

### Ver reservas pendientes (manager/admin)
```bash
curl http://localhost:8000/api/bookings/pending/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

### Confirmar una reserva (manager/admin)
```bash
curl -X POST http://localhost:8000/api/bookings/1/confirm/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

**Respuesta:**
```json
{
  "message": "Reserva confirmada exitosamente",
  "booking": {
    "id": 1,
    "status": "confirmed",
    "status_display": "Confirmada",
    "confirmed_at": "2024-01-15 16:00:00"
  }
}
```

### Cancelar una reserva
```bash
curl -X POST http://localhost:8000/api/bookings/1/cancel/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "notes": "Cliente canceló por lluvia"
  }'
```

### Subir comprobante de pago
```bash
curl -X PATCH http://localhost:8000/api/bookings/1/ \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -F "payment_proof=@/ruta/a/comprobante.jpg"
```

### Filtrar reservas
```bash
# Por fecha
curl "http://localhost:8000/api/bookings/?date=2024-01-20" \
  -H "Cookie: sessionid=YOUR_SESSION_ID"

# Por cancha
curl "http://localhost:8000/api/bookings/?court=1" \
  -H "Cookie: sessionid=YOUR_SESSION_ID"

# Por estado
curl "http://localhost:8000/api/bookings/?status=confirmed" \
  -H "Cookie: sessionid=YOUR_SESSION_ID"

# Por usuario
curl "http://localhost:8000/api/bookings/?user=3" \
  -H "Cookie: sessionid=YOUR_SESSION_ID"

# Búsqueda por nombre o teléfono
curl "http://localhost:8000/api/bookings/?search=Juan" \
  -H "Cookie: sessionid=YOUR_SESSION_ID"

# Combinado
curl "http://localhost:8000/api/bookings/?date=2024-01-20&status=confirmed&court=1" \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

---

## Horarios y Precios

### Crear horario para una cancha
```bash
curl -X POST http://localhost:8000/api/schedules/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "court": 1,
    "day_of_week": 0,
    "opening_time": "08:00",
    "closing_time": "23:00",
    "slot_duration": 60
  }'
```

### Listar horarios de una cancha
```bash
curl "http://localhost:8000/api/schedules/?court=1" \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

### Crear precio
```bash
curl -X POST http://localhost:8000/api/pricings/ \
  -H "Content-Type: application/json" \
  -H "Cookie: sessionid=YOUR_SESSION_ID" \
  -d '{
    "court": 1,
    "start_time": "08:00",
    "end_time": "18:00",
    "price": 8000.00,
    "is_active": true
  }'
```

### Listar precios de una cancha
```bash
curl "http://localhost:8000/api/pricings/?court=1" \
  -H "Cookie: sessionid=YOUR_SESSION_ID"
```

---

## Códigos de Respuesta HTTP

- `200 OK` - Solicitud exitosa
- `201 Created` - Recurso creado exitosamente
- `204 No Content` - Solicitud exitosa sin contenido
- `400 Bad Request` - Error en los datos enviados
- `401 Unauthorized` - No autenticado
- `403 Forbidden` - Sin permisos
- `404 Not Found` - Recurso no encontrado
- `500 Internal Server Error` - Error del servidor

---

## Paginación

Por defecto, las listas están paginadas (20 items por página):

```bash
# Primera página
curl http://localhost:8000/api/bookings/

# Segunda página
curl http://localhost:8000/api/bookings/?page=2

# Cambiar tamaño de página
curl "http://localhost:8000/api/bookings/?page_size=50"
```

**Respuesta paginada:**
```json
{
  "count": 45,
  "next": "http://localhost:8000/api/bookings/?page=2",
  "previous": null,
  "results": [
    // ... array de reservas
  ]
}
```

---

## Notas Importantes

1. **Autenticación**: La mayoría de endpoints requieren autenticación mediante sesión
2. **CSRF**: Para operaciones POST/PUT/DELETE desde el navegador, incluir CSRF token
3. **Permisos**: Algunos endpoints solo están disponibles para managers/admins
4. **Validaciones**: El sistema valida automáticamente conflictos de horarios
5. **Timestamps**: Todas las fechas están en formato ISO 8601 con zona horaria de Argentina
