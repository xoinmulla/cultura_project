# destinations/models.py
from django.db import models
from django.urls import reverse

class Destination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200) # Could be more complex (e.g., GeoDjango PointField)
    historical_significance = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True) # Needs Pillow installed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destination_detail', kwargs={'pk': self.pk})