# events/models.py
from django.db import models
from django.urls import reverse
from django.conf import settings # If you want to link to users as organizers

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(blank=True, null=True)
    venue = models.CharField(max_length=255)
    organizer = models.CharField(max_length=150, blank=True) # Or ForeignKey to User/Organization model
    # organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='organized_events')
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'pk': self.pk})