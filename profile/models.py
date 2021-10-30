from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse

from users.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    motto = models.CharField(blank=True, null=True, max_length=100)
    main_skill = models.CharField(blank=True, null=True, max_length=100)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    def get_portfolio_absolute_url(self):
        return reverse('portfolio:portfolio', kwargs={'username': self.user.username})

    def __str__(self):
        return f'{self.user.username} -  {self.user.first_name} - {self.user.last_name} '


def post_save_user_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    user_profile, created = Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_user_profile_create, sender=settings.AUTH_USER_MODEL)
