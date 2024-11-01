from django.db import models
from django.conf import settings
from courts.models import Court


class Booking(models.Model):
    """
    Modelo para las reservas de canchas
    """
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('cancelled', 'Cancelada'),
        ('completed', 'Completada'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('transfer', 'Transferencia'),
        ('cash', 'Efectivo'),
        ('card', 'Tarjeta'),
        ('mp', 'Mercado Pago'),
    ]
    
    # Relaciones
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='bookings',
        verbose_name='Usuario'
    )
    court = models.ForeignKey(
        Court, 
        on_delete=models.CASCADE, 
        related_name='bookings',
        verbose_name='Cancha'
    )
    
    # Datos de la reserva
    date = models.DateField('Fecha')
    start_time = models.TimeField('Hora inicio')
    end_time = models.TimeField('Hora fin')
    duration = models.IntegerField('Duración (minutos)', default=60)
    
    # Precio y pago
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    payment_method = models.CharField('Método de pago', max_length=10, choices=PAYMENT_METHOD_CHOICES, blank=True)
    payment_proof = models.ImageField('Comprobante de pago', upload_to='payment_proofs/', blank=True, null=True)
    
    # Estado
    status = models.CharField('Estado', max_length=10, choices=STATUS_CHOICES, default='pending')
    
    # Información adicional
    notes = models.TextField('Notas', blank=True)
    player_name = models.CharField('Nombre del jugador', max_length=200, blank=True)
    player_phone = models.CharField('Teléfono del jugador', max_length=20, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    confirmed_at = models.DateTimeField('Fecha de confirmación', blank=True, null=True)
    cancelled_at = models.DateTimeField('Fecha de cancelación', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-date', '-start_time']
        unique_together = ['court', 'date', 'start_time']
    
    def __str__(self):
        return f"{self.court.name} - {self.date} {self.start_time} ({self.get_status_display()})"


class BookingHistory(models.Model):
    """
    Historial de cambios en las reservas
    """
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='history', verbose_name='Reserva')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Usuario')
    action = models.CharField('Acción', max_length=50)
    old_status = models.CharField('Estado anterior', max_length=10, blank=True)
    new_status = models.CharField('Estado nuevo', max_length=10, blank=True)
    notes = models.TextField('Notas', blank=True)
    created_at = models.DateTimeField('Fecha', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Historial de reserva'
        verbose_name_plural = 'Historial de reservas'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.booking} - {self.action}"
