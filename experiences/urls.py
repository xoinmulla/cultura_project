# experiences/urls.py
from django.urls import path
from .views import ExperienceListView, ExperienceDetailView, ExperienceCategoryListView

app_name = 'experiences' # Optional: Define an app namespace

urlpatterns = [
    path('', ExperienceListView.as_view(), name='experience_list'),
    path('experience/<int:pk>/', ExperienceDetailView.as_view(), name='experience_detail'),
    path('category/<slug:category_slug>/', ExperienceCategoryListView.as_view(), name='experience_category'),
]