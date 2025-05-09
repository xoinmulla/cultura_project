# Generated by Django 5.1.7 on 2025-05-09 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Experience Categories',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('itinerary', models.TextField(blank=True, help_text='Outline of the experience.')),
                ('duration_hours', models.DecimalField(decimal_places=1, help_text='Duration in hours (e.g., 2.5)', max_digits=4)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('guide_info', models.CharField(blank=True, help_text='Information about the guide, if applicable.', max_length=255)),
                ('location_details', models.CharField(blank=True, help_text='Starting point or main location.', max_length=255)),
                ('inclusions', models.TextField(blank=True)),
                ('exclusions', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='experience_images/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='experiences.experiencecategory')),
            ],
        ),
    ]
