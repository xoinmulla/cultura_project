# events/forms.py
from django import forms
from .models import Event

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local' # Use browser's datetime picker

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'start_datetime',
            'end_datetime',
            'venue',
            'organizer', # If this were a ForeignKey, you might exclude it or handle it differently
            'image',
        ]
        widgets = {
            'start_datetime': DateTimeInput(),
            'end_datetime': DateTimeInput(),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Add bootstrap classes or other attributes to form fields
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control' # Example for bootstrap
            else:
                field.widget.attrs['class'] = 'form-control' # Example for bootstrap
            if field_name in ['start_datetime', 'end_datetime'] and self.instance.pk:
                 # Format datetime for 'datetime-local' input when editing
                if field.initial:
                    field.initial = field.initial.strftime('%Y-%m-%dT%H:%M')