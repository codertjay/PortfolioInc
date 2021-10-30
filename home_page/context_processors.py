from blog.models import Post
from blog.models import blogCategory
from membership.models import Membership
from website.models import TagChoice, WebsiteTemplate
from .models import HomePageService, HomePageTestimonial


def add_variable_to_context(request):
    Free = Membership.objects.get_membership_type(membership_type='Free')
    Standard = Membership.objects.get_membership_type(membership_type='Standard')
    Premium = Membership.objects.get_membership_type(membership_type='Premium')
    Professional = Membership.objects.get_membership_type(membership_type='Professional')
    service = HomePageService.objects.all()
    testimonial = HomePageTestimonial.objects.all()
    portfolio_template = WebsiteTemplate.objects.all()

    older_posts = Post.objects.all().order_by('-id')[:3]
    latest_posts = Post.objects.all()[:3]
    latest_post_footer = Post.objects.all().order_by('view_count')[:2]
    about_website = "PortfolioInc is all about crating Portfolio " \
                    "website for individual with low or no cost We love the web and care deeply for how users interact with a digital product. We power " \
                    "" \
                    "businesses and individuals to create better looking web projects around the world"

    return {
        'latest_posts': latest_posts,
        'older_posts': older_posts,
        'about_website': about_website,
        'instagram_url': 'https://instagram.com/codertjay',
        'twitter_url': 'https://twitter.com/codertjay',
        'facebook_url': 'https://instagram.com/codertjay',
        'linkedin_url': 'https://www.linkedin.com/in/favour-afenikhena-877254178/',
        'email': 'portfolio@gmail.com',
        'phone_number': '2348061715291',
        'service': service,
        'home_page_testimonial': testimonial,
        'portfolio_template': portfolio_template,
        'website_name': 'PortfolioInc',
        'tag_choice': TagChoice,
        'Free': Free,
        'Standard': Standard,
        'Premium': Premium,
        'Professional': Professional,
        'blogCategory': blogCategory,
        'latest_post_footer': latest_post_footer,
    }
