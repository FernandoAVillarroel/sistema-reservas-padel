from django.db import models


class Court(models.Model):
    """
    Modelo para las canchas de pádel
    """
    name = models.CharField('Nombre', max_length=100)
    description = models.TextField('Descripción', blank=True)
    is_active = models.BooleanField('Activa', default=True)
    is_covered = models.BooleanField('Techada', default=False)
    has_lighting = models.BooleanField('Tiene iluminación', default=True)
    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    
    class Meta:
        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class CourtSchedule(models.Model):
    """
    Horarios de disponibilidad de las canchas
    """
    DAYS_OF_WEEK = [
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]
    
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='schedules', verbose_name='Cancha')
    day_of_week = models.IntegerField('Día de la semana', choices=DAYS_OF_WEEK)
    opening_time = models.TimeField('Hora de apertura')
    closing_time = models.TimeField('Hora de cierre')
    slot_duration = models.IntegerField('Duración del turno (minutos)', default=60)
    
    class Meta:
        verbose_name = 'Horario de cancha'
        verbose_name_plural = 'Horarios de canchas'
        ordering = ['court', 'day_of_week', 'opening_time']
        unique_together = ['court', 'day_of_week']
    
    def __str__(self):
        return f"{self.court.name} - {self.get_day_of_week_display()}"


class Pricing(models.Model):
    """
    Precios de las canchas por horario
    """
    court = models.ForeignKey(Court, on_delete=models.CASCADE, related_name='pricings', verbose_name='Cancha')
    start_time = models.TimeField('Hora inicio')
    end_time = models.TimeField('Hora fin')
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    is_active = models.BooleanField('Activo', default=True)
    
    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'
        ordering = ['court', 'start_time']
    
    def __str__(self):
        return f"{self.court.name} - ${self.price} ({self.start_time} - {self.end_time})"
