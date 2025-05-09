from django.contrib import admin
from .models import Event
from django.utils.html import format_html
from django.db import models # Import models for formfield_for_dbfield

# Register Event
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'venue', 'start_datetime', 'end_datetime', 
        'organizer', 'created_at', 'updated_at', 'get_image_thumbnail'
    )
    list_filter = (
        'start_datetime', 'end_datetime', 'created_at', 'updated_at',
        'organizer' # This will be a text filter based on unique organizer names
    )
    search_fields = ('name', 'description', 'venue', 'organizer')

    # Date hierarchy for quick navigation by date
    date_hierarchy = 'start_datetime'

    # Customize form fields layout using fieldsets
    fieldsets = (
        (None, {
            'fields': ('name', 'image'),
        }),
        ('Event Details', {
            'fields': ('description', 'venue', 'organizer'),
            'classes': ('collapse',), # Make this section collapsible
            'description': 'Core information about the event.'
        }),
        ('Timing', {
            'fields': ('start_datetime', 'end_datetime'),
            'description': 'Specify the start and end dates and times for the event.'
        }),
    )

    # Override formfield_for_dbfield to use custom widgets for TextFields
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'description':
            kwargs['widget'] = admin.widgets.AdminTextareaWidget(
                attrs={'rows': 10, 'cols': 80} # Adjust rows/cols as needed
            )
        # Optional: If you want to use a custom datetime picker in admin
        # if isinstance(db_field, models.DateTimeField):
        #     kwargs['widget'] = admin.widgets.AdminSplitDateTime
            # Or a more advanced custom widget like django-datetime-widget if installed
        return super().formfield_for_dbfield(db_field, **kwargs)

    # Custom method to display image thumbnail in list_display
    def get_image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "No Image"
    get_image_thumbnail.short_description = 'Image'

    # Example of custom actions (if you add an 'is_active' field to your Event model)
    # actions = ['make_active', 'make_inactive']

    # def make_active(self, request, queryset):
    #     queryset.update(is_active=True)
    # make_active.short_description = "Mark selected events as active"

    # def make_inactive(self, request, queryset):
    #     queryset.update(is_active=False)
    # make_inactive.short_description = "Mark selected events as inactive"

    # To improve organizer filtering if it becomes a ForeignKey to User/Organization
    # def get_list_filter(self, request):
    #     filters = list(self.list_filter)
    #     if isinstance(self.model._meta.get_field('organizer'), models.ForeignKey):
    #         # Replace simple text filter with a more powerful filter for ForeignKey
    #         filters = [f for f in filters if f != 'organizer'] + ['organizer'] # Assuming 'organizer' is the field name
    #     return filters