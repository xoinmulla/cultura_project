from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Experience, ExperienceCategory

class ExperienceListView(ListView):
    model = Experience
    template_name = 'experiences/experience_list.html'
    context_object_name = 'experiences'
    queryset = Experience.objects.filter(is_active=True).order_by('-created_at') # Show active experiences, newest first

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ExperienceCategory.objects.all()
        return context

class ExperienceDetailView(DetailView):
    model = Experience
    template_name = 'experiences/experience_detail.html'
    context_object_name = 'experience'

    def get_queryset(self):
        # Ensure only active experiences can be viewed directly by PK,
        # or adjust if you want to allow viewing inactive ones via direct link
        return super().get_queryset().filter(is_active=True)

class ExperienceCategoryListView(ListView):
    model = Experience
    template_name = 'experiences/experience_category.html'
    context_object_name = 'experiences'

    def get_queryset(self):
        self.category = get_object_or_404(ExperienceCategory, slug=self.kwargs['category_slug'])
        return Experience.objects.filter(category=self.category, is_active=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = ExperienceCategory.objects.all() # For displaying all categories in navigation
        return context