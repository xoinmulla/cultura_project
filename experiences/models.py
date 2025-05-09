# experiences/models.py
from django.db import models
from django.urls import reverse
# from django.conf import settings

class ExperienceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Experience Categories"


class Experience(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ExperienceCategory, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    itinerary = models.TextField(blank=True, help_text="Outline of the experience.")
    duration_hours = models.DecimalField(max_digits=4, decimal_places=1, help_text="Duration in hours (e.g., 2.5)")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    guide_info = models.CharField(max_length=255, blank=True, help_text="Information about the guide, if applicable.")
    location_details = models.CharField(max_length=255, blank=True, help_text="Starting point or main location.")
    inclusions = models.TextField(blank=True)
    exclusions = models.TextField(blank=True)
    image = models.ImageField(upload_to='experience_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # guide = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='guided_experiences', limit_choices_to={'is_staff': True}) # Example if guides are users

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('experiences:experience_detail', kwargs={'pk': self.pk})