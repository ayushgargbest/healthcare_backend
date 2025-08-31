from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'email', 'phone', 'experience_years', 'consultation_fee')
    list_filter = ('specialization', 'experience_years', 'created_at')
    search_fields = ('name', 'email', 'specialization')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)