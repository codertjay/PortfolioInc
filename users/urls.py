from django.urls import path
from .views import ContactUserView



app_name = 'user'
urlpatterns = [
    path('contactuser/', ContactUserView.as_view(), name='contact_user'),
]
