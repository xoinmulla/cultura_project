"""
URL configuration for cultura_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# cultura_project/urls.py
# cultura_project/urls.py - CORRECT WAY
from django.contrib import admin
from django.urls import path, include # Make sure include is imported
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

# Ensure your app's urls.py exists and is correctly named, e.g., destinations.urls
# No need to directly import destinations.urls here usually

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # CORRECTED LINE for destinations:
    path('destinations/', include('destinations.urls')),

    # If you have other apps, include them similarly:
    path('events/', include('events.urls')),
    path('experiences/', include('experiences.urls', namespace='experiences')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)