# destinations/urls.py
from django.urls import path
from .views import DestinationListView, DestinationDetailView

urlpatterns = [
    # Ensure this line has name='destination_list'
    path('', DestinationListView.as_view(), name='destination_list'),
    path('<int:pk>/', DestinationDetailView.as_view(), name='destination_detail'),
]