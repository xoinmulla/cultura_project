# destinations/admin.py
from django.contrib import admin
from .models import Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at', 'updated_at')
    search_fields = ('name', 'location', 'description')