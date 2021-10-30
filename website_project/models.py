from django.db import models

from website.models import Website


class Project(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=200)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image

    def __str__(self):
        return f'{self.name} by{self.website.user}'


class ProjectItem(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project')
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=100)
    instagram = models.BooleanField(default=False)
    twitter = models.BooleanField(default=False)

    @property
    def imageURL(self):
        try:
            image = self.image.url
        except:
            image = ''
        return image

    def __str__(self):
        return f'{self.name[0:10]} by - {self.website.user}'
