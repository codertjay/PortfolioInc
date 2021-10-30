from django.db import models
from website.models import Website


class Layout(models.Model):
    website = models.OneToOneField(Website, on_delete=models.CASCADE)
    primary_color = models.CharField(max_length=10)
    secondary_color = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='layout')
    image = models.ImageField(upload_to='layout')
    about = models.TextField(blank=True, null=True, max_length=1000)
