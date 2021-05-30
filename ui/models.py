from django.db import models

# Create your models here.

class ShortenedUrl(models.Model):
    original_url = models.CharField(max_length=1000)
    shortened_string = models.CharField(max_length=7)
