from django.contrib import admin
from . models import Patient, Appointment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('username', 'card_number', 'gender')
    list_filter = ('level', 'gender',)
    search_fields = ('card_number',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date', 'time')
    list_filter = ('approved', 'approved',)
    search_fields = ('doctor', 'patient')
