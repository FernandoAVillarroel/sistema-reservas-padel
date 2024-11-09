"""
Script para crear datos iniciales de prueba
Ejecutar con: python manage.py shell < setup_initial_data.py
"""

from django.contrib.auth import get_user_model
from courts.models import Court, CourtSchedule, Pricing
from datetime import time

User = get_user_model()

# Crear usuarios de prueba
print("Creando usuarios...")

# Admin
admin, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@padel.com',
        'first_name': 'Admin',
        'last_name': 'Sistema',
        'role': 'admin',
        'is_staff': True,
        'is_superuser': True
    }
)
if created:
    admin.set_password('admin123')
    admin.save()
    print("✓ Admin creado")

# Encargado
manager, created = User.objects.get_or_create(
    username='encargado',
    defaults={
        'email': 'encargado@padel.com',
        'first_name': 'Juan',
        'last_name': 'Pérez',
        'phone': '3815551234',
        'role': 'manager',
        'is_staff': True
    }
)
if created:
    manager.set_password('encargado123')
    manager.save()
    print("✓ Encargado creado")

# Cliente
customer, created = User.objects.get_or_create(
    username='cliente1',
    defaults={
        'email': 'cliente1@padel.com',
        'first_name': 'María',
        'last_name': 'González',
        'phone': '3815555678',
        'role': 'customer'
    }
)
if created:
    customer.set_password('cliente123')
    customer.save()
    print("✓ Cliente creado")

# Crear canchas
print("\nCreando canchas...")

court1, created = Court.objects.get_or_create(
    name='Cancha 1',
    defaults={
        'description': 'Cancha principal techada con iluminación LED',
        'is_covered': True,
        'has_lighting': True,
        'is_active': True
    }
)
if created:
    print("✓ Cancha 1 creada")

court2, created = Court.objects.get_or_create(
    name='Cancha 2',
    defaults={
        'description': 'Cancha al aire libre con iluminación',
        'is_covered': False,
        'has_lighting': True,
        'is_active': True
    }
)
if created:
    print("✓ Cancha 2 creada")

court3, created = Court.objects.get_or_create(
    name='Cancha 3',
    defaults={
        'description': 'Cancha techada premium',
        'is_covered': True,
        'has_lighting': True,
        'is_active': True
    }
)
if created:
    print("✓ Cancha 3 creada")

# Crear horarios para las canchas
print("\nCreando horarios...")

days = [0, 1, 2, 3, 4, 5, 6]  # Lunes a Domingo

for court in [court1, court2, court3]:
    for day in days:
        schedule, created = CourtSchedule.objects.get_or_create(
            court=court,
            day_of_week=day,
            defaults={
                'opening_time': time(8, 0),
                'closing_time': time(23, 0),
                'slot_duration': 60
            }
        )
        if created:
            print(f"✓ Horario creado para {court.name} - día {day}")

# Crear precios
print("\nCreando precios...")

# Precios de día (8:00 - 18:00)
for court in [court1, court2, court3]:
    pricing_day, created = Pricing.objects.get_or_create(
        court=court,
        start_time=time(8, 0),
        end_time=time(18, 0),
        defaults={
            'price': 8000.00,
            'is_active': True
        }
    )
    if created:
        print(f"✓ Precio de día creado para {court.name}")
    
    # Precios de noche (18:00 - 23:00)
    pricing_night, created = Pricing.objects.get_or_create(
        court=court,
        start_time=time(18, 0),
        end_time=time(23, 0),
        defaults={
            'price': 12000.00,
            'is_active': True
        }
    )
    if created:
        print(f"✓ Precio de noche creado para {court.name}")

print("\n" + "="*50)
print("¡Datos iniciales creados exitosamente!")
print("="*50)
print("\nCredenciales de acceso:")
print("-" * 50)
print("ADMIN:")
print("  Usuario: admin")
print("  Contraseña: admin123")
print("\nENCARGADO:")
print("  Usuario: encargado")
print("  Contraseña: encargado123")
print("\nCLIENTE:")
print("  Usuario: cliente1")
print("  Contraseña: cliente123")
print("-" * 50)
