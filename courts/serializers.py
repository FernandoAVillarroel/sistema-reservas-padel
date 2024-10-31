from rest_framework import serializers
from .models import Court, CourtSchedule, Pricing


class CourtScheduleSerializer(serializers.ModelSerializer):
    """
    Serializer para los horarios de las canchas
    """
    day_name = serializers.CharField(source='get_day_of_week_display', read_only=True)
    
    class Meta:
        model = CourtSchedule
        fields = ['id', 'court', 'day_of_week', 'day_name', 'opening_time', 
                  'closing_time', 'slot_duration']
        read_only_fields = ['id']


class PricingSerializer(serializers.ModelSerializer):
    """
    Serializer para los precios de las canchas
    """
    class Meta:
        model = Pricing
        fields = ['id', 'court', 'start_time', 'end_time', 'price', 'is_active']
        read_only_fields = ['id']


class CourtSerializer(serializers.ModelSerializer):
    """
    Serializer para las canchas
    """
    schedules = CourtScheduleSerializer(many=True, read_only=True)
    pricings = PricingSerializer(many=True, read_only=True)
    
    class Meta:
        model = Court
        fields = ['id', 'name', 'description', 'is_active', 'is_covered', 
                  'has_lighting', 'created_at', 'updated_at', 'schedules', 'pricings']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CourtListSerializer(serializers.ModelSerializer):
    """
    Serializer simplificado para listar canchas
    """
    class Meta:
        model = Court
        fields = ['id', 'name', 'description', 'is_active', 'is_covered', 'has_lighting']
