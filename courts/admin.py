from django.contrib import admin
from .models import Court, CourtSchedule, Pricing


class CourtScheduleInline(admin.TabularInline):
    model = CourtSchedule
    extra = 1


class PricingInline(admin.TabularInline):
    model = Pricing
    extra = 1


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'is_covered', 'has_lighting', 'created_at']
    list_filter = ['is_active', 'is_covered', 'has_lighting', 'created_at']
    search_fields = ['name', 'description']
    inlines = [CourtScheduleInline, PricingInline]
    readonly_fields = ['created_at', 'updated_at']


@admin.register(CourtSchedule)
class CourtScheduleAdmin(admin.ModelAdmin):
    list_display = ['court', 'day_of_week', 'opening_time', 'closing_time', 'slot_duration']
    list_filter = ['court', 'day_of_week']
    search_fields = ['court__name']


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ['court', 'start_time', 'end_time', 'price', 'is_active']
    list_filter = ['court', 'is_active']
    search_fields = ['court__name']
