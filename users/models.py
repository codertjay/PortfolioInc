import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', ]
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)

    def verify_mail(self):
        if not self.verified:
            self.verified = True
            self.save()
            return True
        return True


class ContactUser(models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    contact_subject = models.CharField(max_length=200)
    contact_message = models.TextField()
    to_email = models.EmailField()


class ContactAdmin(models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    contact_subject = models.CharField(max_length=200)
    contact_message = models.TextField()
