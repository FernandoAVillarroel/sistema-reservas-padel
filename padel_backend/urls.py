from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from courts.views import CourtViewSet, CourtScheduleViewSet, PricingViewSet
from bookings.views import BookingViewSet, BookingHistoryViewSet

# Configurar el router de DRF
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'courts', CourtViewSet, basename='court')
router.register(r'schedules', CourtScheduleViewSet, basename='schedule')
router.register(r'pricings', PricingViewSet, basename='pricing')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'booking-history', BookingHistoryViewSet, basename='booking-history')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
