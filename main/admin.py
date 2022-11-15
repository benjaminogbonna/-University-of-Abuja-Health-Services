from django.contrib import admin
from .models import Receptionist, Contact

admin.site.register(Receptionist)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date_sent')
    search_fields = ('name', 'email', 'subject')
