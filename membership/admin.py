from django.contrib import admin

from .models import UserMembershipSubscription, Membership

admin.site.register(UserMembershipSubscription)
admin.site.register(Membership)
