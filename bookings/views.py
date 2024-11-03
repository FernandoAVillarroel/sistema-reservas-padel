from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import Booking, BookingHistory
from .serializers import (
    BookingSerializer, BookingCreateSerializer, 
    BookingListSerializer, BookingHistorySerializer
)


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar reservas
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['court', 'date', 'status', 'user']
    search_fields = ['player_name', 'player_phone', 'notes']
    ordering_fields = ['date', 'start_time', 'created_at']
    
    def get_queryset(self):
        """
        Filtrar reservas según el rol del usuario
        """
        user = self.request.user
        if user.role in ['admin', 'manager']:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return BookingCreateSerializer
        elif self.action == 'list':
            return BookingListSerializer
        return BookingSerializer
    
    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        """
        Confirmar una reserva (solo para managers y admins)
        """
        booking = self.get_object()
        
        if request.user.role not in ['admin', 'manager']:
            return Response(
                {'error': 'No tienes permisos para confirmar reservas'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        if booking.status != 'pending':
            return Response(
                {'error': 'Solo se pueden confirmar reservas pendientes'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        old_status = booking.status
        booking.status = 'confirmed'
        booking.confirmed_at = timezone.now()
        booking.save()
        
        # Registrar en historial
        BookingHistory.objects.create(
            booking=booking,
            user=request.user,
            action='Confirmada',
            old_status=old_status,
            new_status=booking.status,
            notes='Reserva confirmada por el encargado'
        )
        
        return Response({
            'message': 'Reserva confirmada exitosamente',
            'booking': BookingSerializer(booking).data
        })
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """
        Cancelar una reserva
        """
        booking = self.get_object()
        
        # Verificar permisos
        if booking.user != request.user and request.user.role not in ['admin', 'manager']:
            return Response(
                {'error': 'No tienes permisos para cancelar esta reserva'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        if booking.status == 'cancelled':
            return Response(
                {'error': 'Esta reserva ya está cancelada'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        old_status = booking.status
        booking.status = 'cancelled'
        booking.cancelled_at = timezone.now()
        booking.save()
        
        # Registrar en historial
        BookingHistory.objects.create(
            booking=booking,
            user=request.user,
            action='Cancelada',
            old_status=old_status,
            new_status=booking.status,
            notes=request.data.get('notes', 'Reserva cancelada')
        )
        
        return Response({
            'message': 'Reserva cancelada exitosamente',
            'booking': BookingSerializer(booking).data
        })
    
    @action(detail=False, methods=['get'])
    def my_bookings(self, request):
        """
        Obtener las reservas del usuario actual
        """
        bookings = Booking.objects.filter(user=request.user)
        serializer = BookingListSerializer(bookings, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        """
        Obtener reservas pendientes (solo para managers y admins)
        """
        if request.user.role not in ['admin', 'manager']:
            return Response(
                {'error': 'No tienes permisos para ver reservas pendientes'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        bookings = Booking.objects.filter(status='pending')
        serializer = BookingListSerializer(bookings, many=True)
        return Response(serializer.data)


class BookingHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet de solo lectura para el historial de reservas
    """
    queryset = BookingHistory.objects.all()
    serializer_class = BookingHistorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['booking', 'user']
