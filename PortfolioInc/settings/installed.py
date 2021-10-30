# Application definition
LOCAL_APPS = [
    'home_page',
    'profile',
    'blog',
    'comment',
    'users',
    'membership'

]

WEBSITE_API = [
    'website',
    'website_project',
    'website_resume',
    'website_service',
    'website_skill',
    'website_testimonial',
]

THIRD_PARTY_APPS = [

    # third part packages
    'markdown_deux',
    'pagedown',
    'crispy_forms',
    'colorful',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # rest framework
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

    # subdomains
    'django_hosts',
    'corsheaders',
    # 'upload_validator',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += LOCAL_APPS
INSTALLED_APPS += THIRD_PARTY_APPS
INSTALLED_APPS += WEBSITE_API
