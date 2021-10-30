import requests
from django.db import models

from users.models import User

# Create your models here.

MembershipType = (
    ('Free', 'Free'),
    ('Standard', 'Standard'),
    ('Premium', 'Premium'),
    ('Professional', 'Professional'),
)


class CurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        return 100




class MembershipManager(models.Manager):
    def get_membership_type(self, membership_type):
        membership = self.filter(membership_type=membership_type)
        if membership:
            return membership.first()
        return None

    def get_membership_plan_id(self, membership_plan_id):
        membership = self.filter(membership_plan_id=membership_plan_id)
        if membership:
            return membership.first()
        return None


class Membership(models.Model):
    name = models.CharField(max_length=20)
    membership_type = models.CharField(
        choices=MembershipType, default='Free', max_length=50)
    membership_plan_id = models.CharField(max_length=40, blank=True, null=True)
    info = models.TextField()
    objects = MembershipManager()

    def __str__(self):
        return self.membership_type


class UserMembershipSubscriptionManager(models.Manager):

    def get_user_subscription(self):
        pass


class UserMembershipSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer_code = models.CharField(max_length=100, blank=True, null=True)
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    customer_reference = models.CharField(
        max_length=100, blank=True, null=True)
    objects = UserMembershipSubscriptionManager()

    def __str__(self):
        return f'{self.user.first_name} -- {self.user.last_name} -- {self.membership.membership_type}'
