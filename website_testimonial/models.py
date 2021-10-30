from django.db import models

# Create your models here.
from website.models import Website


class Testimonial(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50)
    image = models.ImageField()
    url = models.URLField(blank=True, null=True)
    detail = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image
