from django.contrib import messages
from django.contrib.sitemaps import Sitemap
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.template.loader import get_template
from django.urls import reverse
from django.views.generic.base import View

from PortfolioInc.settings import EMAIL_HOST_USER
from home_page.forms import SubscribeForm
from users.forms import ContactAdminForm
from users.models import ContactAdmin


def handler404(request, exception):
    response = render(request, '404.html', context={})
    response.status_code = 404
    return response


def handler500(request, exception):
    response = render(request, '500.html', context={})
    response.status_code = 500
    return response


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return [
            'home_page:home', 'home_page:subscribe', 'home_page:offer',
            'home_page:faq', 'home_page:about', 'home_page:testimonial',
            'home_page:contact', 'home_page:price', 'blog:blog_list',
            'account_login', 'account_signup',
        ]

    def location(self, item):
        return reverse(item)


class HomePageView(View):

    def get(self, request):
        return render(request, 'HomePage/index.html')


class OfferView(View):
    def get(self, request):
        return render(request, 'HomePage/offer.html')


class FaqView(View):

    def get(self, request):
        return render(request, 'HomePage/faq.html')


class AboutView(View):

    def get(self, request):
        return render(request, 'HomePage/about-us.html')


class PricingView(View):

    def get(self, request):
        return render(request, 'HomePage/pricing.html')


class TestimonialView(View):

    def get(self, request):
        return render(request, 'HomePage/testimonials.html')


class ContactView(View):

    def get(self, request):
        return render(request, 'HomePage/contact.html')

    def post(self, request):
        form = ContactAdminForm(request.POST)
        contact = ContactAdmin(
            contact_name=form['contact_name'].value(),
            contact_email=form['contact_email'].value(),
            contact_subject=form['contact_subject'].value(),
            contact_message=form['contact_message'].value()
        )
        if form.is_valid():
            contact.save()
            template = get_template('EmailTemplates/contact_admin.txt')
            context = {
                'contact_name': contact.contact_name,
                'contact_email': contact.contact_email,
                'contact_subject': contact.contact_subject,
                'contact_message': contact.contact_message
            }
            print('the for is valid')
            content = template.render(context)
            if context:
                send_mail(
                    contact.contact_subject,
                    content,
                    contact.contact_email,
                    [EMAIL_HOST_USER],
                    fail_silently=True,
                )
                print('sent the message', content)
                messages.success(request, 'Your message has being sent we would be in touch with you later ')
                return redirect('home_page:contact')
        print('there was an error sending your message')
        return redirect('home_page:contact')


def subscribe_user(request):
    form = SubscribeForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Subscribed to our mailing list ')
    else:
        messages.info(request, 'There was an error subscribing to our mailing list ')
    return redirect('home_page:home')



class AdsView(View):
    """Replace pub-0000000000000000 with your own publisher ID"""

    def get(self, request, *args, **kwargs):
        line = "google.com, pub-8515488467518904, DIRECT, f08c47fec0942fa0"
        return HttpResponse(line)


class BingXmlView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'BingSiteAuth.xml', content_type='text/xml')
