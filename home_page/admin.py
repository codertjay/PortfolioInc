from django.contrib import admin

# Register your models here.
from .models import HomePageTestimonial,HomePageService,SubscribeUser


admin.site.register(HomePageTestimonial)
admin.site.register(HomePageService)
admin.site.register(SubscribeUser)
