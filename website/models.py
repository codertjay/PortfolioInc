import uuid

from django.conf import settings
from django.db import models

from portfolioinc_template.models import WebsiteTemplate

User = settings.AUTH_USER_MODEL


class Website(models.Model):
    """
    Website Created By the user : The user has  access of creating  multiple user
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subdomain = models.SlugField(unique=True)
    domain = models.SlugField(unique=True, blank=True, null=True)
    template = models.OneToOneField(WebsiteTemplate, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.template
