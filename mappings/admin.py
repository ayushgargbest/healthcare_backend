from django.contrib import admin
from .models import PatientDoctorMapping

@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_date', 'is_active')
    list_filter = ('assigned_date', 'is_active', 'doctor__specialization')
    search_fields = ('patient__name', 'doctor__name')
    readonly_fields = ('assigned_date',)
    ordering = ('-assigned_date',)