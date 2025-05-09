# experiences/admin.py
from django.contrib import admin
from .models import ExperienceCategory, Experience

@admin.register(ExperienceCategory)
class ExperienceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # Automatically populate slug from name

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'duration_hours', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'created_at')
    search_fields = ('title', 'description', 'location_details')
    list_editable = ('is_active', 'price') # Allows editing these fields directly in the list view