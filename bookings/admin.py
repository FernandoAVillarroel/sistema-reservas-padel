from django.contrib import admin
from .models import Booking, BookingHistory


class BookingHistoryInline(admin.TabularInline):
    model = BookingHistory
    extra = 0
    readonly_fields = ['user', 'action', 'old_status', 'new_status', 'notes', 'created_at']
    can_delete = False


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'court', 'user', 'date', 'start_time', 'end_time', 
                    'price', 'status', 'payment_method', 'created_at']
    list_filter = ['status', 'payment_method', 'court', 'date', 'created_at']
    search_fields = ['user__username', 'player_name', 'player_phone', 'notes']
    readonly_fields = ['created_at', 'updated_at', 'confirmed_at', 'cancelled_at']
    inlines = [BookingHistoryInline]
    
    fieldsets = (
        ('Información de la reserva', {
            'fields': ('user', 'court', 'date', 'start_time', 'end_time', 'duration')
        }),
        ('Información del jugador', {
            'fields': ('player_name', 'player_phone')
        }),
        ('Pago', {
            'fields': ('price', 'payment_method', 'payment_proof')
        }),
        ('Estado', {
            'fields': ('status', 'notes')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at', 'confirmed_at', 'cancelled_at')
        }),
    )


@admin.register(BookingHistory)
class BookingHistoryAdmin(admin.ModelAdmin):
    list_display = ['booking', 'user', 'action', 'old_status', 'new_status', 'created_at']
    list_filter = ['action', 'old_status', 'new_status', 'created_at']
    search_fields = ['booking__id', 'user__username', 'notes']
    readonly_fields = ['booking', 'user', 'action', 'old_status', 'new_status', 'notes', 'created_at']
