from rest_framework import serializers
from .models import Booking, BookingHistory
from courts.serializers import CourtListSerializer
from users.serializers import UserSerializer


class BookingHistorySerializer(serializers.ModelSerializer):
    """
    Serializer para el historial de reservas
    """
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    
    class Meta:
        model = BookingHistory
        fields = ['id', 'booking', 'user', 'user_name', 'action', 'old_status', 
                  'new_status', 'notes', 'created_at']
        read_only_fields = ['id', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer para las reservas
    """
    court_detail = CourtListSerializer(source='court', read_only=True)
    user_detail = UserSerializer(source='user', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    history = BookingHistorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'user', 'user_detail', 'court', 'court_detail', 'date', 
                  'start_time', 'end_time', 'duration', 'price', 'payment_method', 
                  'payment_method_display', 'payment_proof', 'status', 'status_display', 
                  'notes', 'player_name', 'player_phone', 'created_at', 'updated_at', 
                  'confirmed_at', 'cancelled_at', 'history']
        read_only_fields = ['id', 'created_at', 'updated_at', 'confirmed_at', 'cancelled_at']


class BookingCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para crear reservas
    """
    class Meta:
        model = Booking
        fields = ['court', 'date', 'start_time', 'end_time', 'duration', 'price', 
                  'payment_method', 'payment_proof', 'notes', 'player_name', 'player_phone']
    
    def validate(self, attrs):
        # Validar que no haya conflictos de horarios
        court = attrs.get('court')
        date = attrs.get('date')
        start_time = attrs.get('start_time')
        end_time = attrs.get('end_time')
        
        # Verificar que la hora de inicio sea antes que la hora de fin
        if start_time >= end_time:
            raise serializers.ValidationError({
                "start_time": "La hora de inicio debe ser anterior a la hora de fin."
            })
        
        # Verificar disponibilidad
        conflicting_bookings = Booking.objects.filter(
            court=court,
            date=date,
            status__in=['pending', 'confirmed']
        ).filter(
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        
        if conflicting_bookings.exists():
            raise serializers.ValidationError({
                "detail": "Ya existe una reserva en este horario."
            })
        
        return attrs
    
    def create(self, validated_data):
        # Asignar el usuario del request
        validated_data['user'] = self.context['request'].user
        booking = Booking.objects.create(**validated_data)
        
        # Crear entrada en el historial
        BookingHistory.objects.create(
            booking=booking,
            user=self.context['request'].user,
            action='Creada',
            new_status=booking.status,
            notes='Reserva creada'
        )
        
        return booking


class BookingListSerializer(serializers.ModelSerializer):
    """
    Serializer simplificado para listar reservas
    """
    court_name = serializers.CharField(source='court.name', read_only=True)
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'court', 'court_name', 'user', 'user_name', 'date', 
                  'start_time', 'end_time', 'price', 'status', 'status_display']
