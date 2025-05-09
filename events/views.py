# events/views.py
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Event
from .forms import EventForm # We'll create this form next

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html' # <app_name>/<model_name>_list.html
    context_object_name = 'events' # Name of the list in the template
    ordering = ['-start_datetime'] # Optional: order events by start date, newest first
    paginate_by = 10 # Optional: adds pagination

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html' # <app_name>/<model_name>_detail.html
    context_object_name = 'event' # Name of the single object in the template

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm # Use the custom form
    template_name = 'events/event_form.html' # <app_name>/<model_name>_form.html
    # success_url = reverse_lazy('events:event_list') # Redirect after successful creation

    # If you were using the ForeignKey for organizer and wanted to set it automatically:
    # def form_valid(self, form):
    #     form.instance.organizer = self.request.user # Assuming organizer is a ForeignKey to User
    #     return super().form_valid(form)

    # get_absolute_url in the model handles the redirect on success by default for CreateView and UpdateView

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm # Use the custom form
    template_name = 'events/event_form.html'
    # success_url = reverse_lazy('events:event_list') # Or use get_absolute_url from model

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html' # <app_name>/<model_name>_confirm_delete.html
    success_url = reverse_lazy('events:event_list') # Redirect to event list after deletion
    context_object_name = 'event'