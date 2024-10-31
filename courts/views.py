from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Court, CourtSchedule, Pricing
from .serializers import (
    CourtSerializer, CourtListSerializer, 
    CourtScheduleSerializer, PricingSerializer
)


class CourtViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar canchas
    """
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'is_covered', 'has_lighting']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CourtListSerializer
        return CourtSerializer
    
    @action(detail=True, methods=['get'])
    def available_slots(self, request, pk=None):
        """
        Obtener horarios disponibles para una cancha en una fecha específica
        """
        court = self.get_object()
        date = request.query_params.get('date')
        
        if not date:
            return Response(
                {'error': 'Se requiere el parámetro date (YYYY-MM-DD)'},
                status=400
            )
        
        # Aquí irá la lógica para calcular slots disponibles
        # Por ahora retornamos un placeholder
        return Response({
            'court': court.name,
            'date': date,
            'available_slots': []
        })


class CourtScheduleViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar horarios de canchas
    """
    queryset = CourtSchedule.objects.all()
    serializer_class = CourtScheduleSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['court', 'day_of_week']


class PricingViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar precios
    """
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['court', 'is_active']
