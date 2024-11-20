# Estructura de la Base de Datos

## Diagrama de Relaciones

```
┌─────────────────┐
│     User        │
├─────────────────┤
│ id (PK)         │
│ username        │
│ email           │
│ password        │
│ first_name      │
│ last_name       │
│ phone           │
│ role            │◄──────────┐
│ is_active       │           │
│ created_at      │           │
│ updated_at      │           │
└─────────────────┘           │
         │                    │
         │ 1:N                │ N:1
         │                    │
         ▼                    │
┌─────────────────┐           │
│    Booking      │           │
├─────────────────┤           │
│ id (PK)         │           │
│ user_id (FK)    │───────────┘
│ court_id (FK)   │───────┐
│ date            │       │
│ start_time      │       │
│ end_time        │       │
│ duration        │       │
│ price           │       │
│ payment_method  │       │
│ payment_proof   │       │
│ status          │       │
│ notes           │       │
│ player_name     │       │
│ player_phone    │       │
│ created_at      │       │
│ updated_at      │       │
│ confirmed_at    │       │
│ cancelled_at    │       │
└─────────────────┘       │
         │                │
         │ 1:N            │ N:1
         │                │
         ▼                ▼
┌─────────────────┐  ┌─────────────────┐
│BookingHistory   │  │     Court       │
├─────────────────┤  ├─────────────────┤
│ id (PK)         │  │ id (PK)         │
│ booking_id (FK) │  │ name            │
│ user_id (FK)    │  │ description     │
│ action          │  │ is_active       │
│ old_status      │  │ is_covered      │
│ new_status      │  │ has_lighting    │
│ notes           │  │ created_at      │
│ created_at      │  │ updated_at      │
└─────────────────┘  └─────────────────┘
                              │
                     ┌────────┴────────┐
                     │ 1:N             │ 1:N
                     ▼                 ▼
            ┌─────────────────┐  ┌─────────────────┐
            │ CourtSchedule   │  │    Pricing      │
            ├─────────────────┤  ├─────────────────┤
            │ id (PK)         │  │ id (PK)         │
            │ court_id (FK)   │  │ court_id (FK)   │
            │ day_of_week     │  │ start_time      │
            │ opening_time    │  │ end_time        │
            │ closing_time    │  │ price           │
            │ slot_duration   │  │ is_active       │
            └─────────────────┘  └─────────────────┘
```

## Tablas Detalladas

### 1. users_user
**Descripción**: Usuarios del sistema con autenticación

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INT (PK) | Identificador único |
| username | VARCHAR(150) | Nombre de usuario único |
| email | VARCHAR(254) | Email del usuario |
| password | VARCHAR(128) | Contraseña hasheada |
| first_name | VARCHAR(150) | Nombre |
| last_name | VARCHAR(150) | Apellido |
| phone | VARCHAR(20) | Teléfono |
| role | VARCHAR(10) | Rol: admin, manager, customer |
| is_active | BOOLEAN | Usuario activo |
| is_staff | BOOLEAN | Acceso al admin |
| is_superuser | BOOLEAN | Superusuario |
| created_at | DATETIME | Fecha de creación |
| updated_at | DATETIME | Última actualización |

**Índices**:
- PRIMARY KEY (id)
- UNIQUE (username)
- UNIQUE (email)
- INDEX (role)

---

### 2. courts_court
**Descripción**: Canchas de pádel disponibles

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INT (PK) | Identificador único |
| name | VARCHAR(100) | Nombre de la cancha |
| description | TEXT | Descripción |
| is_active | BOOLEAN | Cancha activa |
| is_covered | BOOLEAN | Cancha techada |
| has_lighting | BOOLEAN | Tiene iluminación |
| created_at | DATETIME | Fecha de creación |
| updated_at | DATETIME | Última actualización |

**Índices**:
- PRIMARY KEY (id)
- INDEX (is_active)
- INDEX (name)

---

### 3. courts_courtschedule
**Descripción**: Horarios de operación de las canchas

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INT (PK) | Identificador único |
| court_id | INT (FK) | Cancha asociada |
| day_of_week | INT | Día (0=Lun, 6=Dom) |
| opening_time | TIME | Hora de apertura |
| closing_time | TIME | Hora de cierre |
| slot_duration | INT | Duración turno (min) |

**Índices**:
- PRIMARY KEY (id)
- FOREIGN KEY (court_id) → courts_court(id)
- UNIQUE (court_id, day_of_week)
- INDEX (day_of_week)

---

### 4. courts_pricing
**Descripción**: Precios por horario de las canchas

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INT (PK) | Identificador único |
| court_id | INT (FK) | Cancha asociada |
| start_time | TIME | Hora inicio |
| end_time | TIME | Hora fin |
| price | DECIMAL(10,2) | Precio |
| is_active | BOOLEAN | Precio activo |

**Índices**:
- PRIMARY KEY (id)
- FOREIGN KEY (court_id) → courts_court(id)
- INDEX (court_id, start_time)
- INDEX (is_active)

---

### 5. bookings_booking
**Descripción**: Reservas de canchas

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INT (PK) | Identificador único |
| user_id | INT (FK) | Usuario que reserva |
| court_id | INT (FK) | Cancha reservada |
| date | DATE | Fecha de la reserva |
| start_time | TIME | Hora inicio |
| end_time | TIME | Hora fin |
| duration | INT | Duración (minutos) |
| price | DECIMAL(10,2) | Precio total |
| payment_method | VARCHAR(10) | transfer, cash, card, mp |
| payment_proof | VARCHAR(100) | Ruta al comprobante |
| status | VARCHAR(10) | pending, confirmed, cancelled, completed |
| notes | TEXT | Notas adicionales |
| player_name | VARCHAR(200) | Nombre del jugador |
| player_phone | VARCHAR(20) | Teléfono del jugador |
| created_at | DATETIME | Fecha de creación |
| updated_at | DATETIME | Última actualización |
| confirmed_at | DATETIME | Fecha de confirmación |
| cancelled_at | DATETIME | Fecha de cancelación |

**Índices**:
- PRIMARY KEY (id)
- FOREIGN KEY (user_id) → users_user(id)
- FOREIGN KEY (court_id) → courts_court(id)
- UNIQUE (court_id, date, start_time)
- INDEX (date, status)
- INDEX (user_id)
- INDEX (status)

---

### 6. bookings_bookinghistory
**Descripción**: Historial de cambios en las reservas

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INT (PK) | Identificador único |
| booking_id | INT (FK) | Reserva asociada |
| user_id | INT (FK) | Usuario que hizo el cambio |
| action | VARCHAR(50) | Acción realizada |
| old_status | VARCHAR(10) | Estado anterior |
| new_status | VARCHAR(10) | Estado nuevo |
| notes | TEXT | Notas del cambio |
| created_at | DATETIME | Fecha del cambio |

**Índices**:
- PRIMARY KEY (id)
- FOREIGN KEY (booking_id) → bookings_booking(id)
- FOREIGN KEY (user_id) → users_user(id)
- INDEX (booking_id)
- INDEX (created_at)

---

## Enumeraciones

### user.role
- `admin`: Administrador del sistema
- `manager`: Encargado de las canchas
- `customer`: Cliente que reserva

### booking.status
- `pending`: Pendiente de aprobación
- `confirmed`: Confirmada por el encargado
- `cancelled`: Cancelada
- `completed`: Completada (ya pasó)

### booking.payment_method
- `transfer`: Transferencia bancaria
- `cash`: Efectivo
- `card`: Tarjeta de crédito/débito
- `mp`: Mercado Pago

### courtschedule.day_of_week
- `0`: Lunes
- `1`: Martes
- `2`: Miércoles
- `3`: Jueves
- `4`: Viernes
- `5`: Sábado
- `6`: Domingo

---

## Reglas de Negocio

1. **Unicidad de Reservas**: No puede haber dos reservas confirmadas para la misma cancha en el mismo horario
2. **Validación de Horarios**: Las reservas deben estar dentro del horario de operación de la cancha
3. **Estados de Reserva**: 
   - Nuevas reservas se crean con estado `pending`
   - Solo managers/admins pueden cambiar a `confirmed`
   - Usuarios pueden cancelar sus propias reservas
4. **Historial Automático**: Cada cambio de estado genera una entrada en BookingHistory
5. **Precios**: El precio de la reserva se determina según el horario y la cancha
6. **Slots**: Los turnos se dividen según `slot_duration` configurado por cancha
