from django.urls import path
from .views import HomePageView, FaqView, AboutView, TestimonialView, ContactView, PricingView, \
    subscribe_user, OfferView

app_name = 'home_page'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('#/subscribe/', subscribe_user, name='subscribe'),
    path('#/offer/', OfferView.as_view(), name='offer'),
    path('#/faq/', FaqView.as_view(), name='faq'),
    path('#/about/', AboutView.as_view(), name='about'),
    path('#/testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('#/contact/', ContactView.as_view(), name='contact'),
    path('#/pricing/', PricingView.as_view(), name='price'),
]
