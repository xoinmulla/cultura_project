# destinations/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Destination

class DestinationListView(ListView):
    model = Destination
    template_name = 'destinations/destination_list.html' # App-specific template
    context_object_name = 'destinations'
    paginate_by = 10 # Optional: for pagination

class DestinationDetailView(DetailView):
    model = Destination
    template_name = 'destinations/destination_detail.html'
    context_object_name = 'destination'