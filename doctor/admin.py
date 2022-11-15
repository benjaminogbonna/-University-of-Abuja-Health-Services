from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'department')
    list_filter = ('department', 'gender',)
    search_fields = ('username',)
