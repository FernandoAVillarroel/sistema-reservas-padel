from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Modelo de usuario personalizado con campos adicionales
    """
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('manager', 'Encargado'),
        ('customer', 'Cliente'),
    ]
    
    phone = models.CharField('Teléfono', max_length=20, blank=True)
    role = models.CharField('Rol', max_length=10, choices=ROLE_CHOICES, default='customer')
    is_active = models.BooleanField('Activo', default=True)
    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
