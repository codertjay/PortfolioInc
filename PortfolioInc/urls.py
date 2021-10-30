from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_auth.views import (
    LoginView, LogoutView
)

"""
Url pattern used for the default homepage for PortfolioInc
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls')),

]

api_url_patterns = [
    path('api/blog/', include('blog.api.urls')),
    path('api/comment/', include('comment.api.urls')),
    path('api/user/', include('users.urls')),
]

"""
Route to api used for creating website
"""
website_api_url_patterns = [
    path('api/v1/website/website/', include('website.urls')),
    path('api/v1/website/testimonial/', include('website_testimonial.urls')),
    path('api/v1/website/skill/', include('website_skill.urls')),
    path('api/v1/website/service/', include('website_service.urls')),
    path('api/v1/website/layout/', include('website_layout.urls')),
    path('api/v1/website/project/', include('website_project.urls')),
]

"""
Route to api Authentication
"""
authentication_url_patterns = [
    path('api/v1/auth/register/', include('rest_auth.registration.urls')),
    path('api/v1/auth/login/', LoginView.as_view()),
    path('api/v1/auth/logout/', LogoutView.as_view()),
]

urlpatterns += authentication_url_patterns
urlpatterns += website_api_url_patterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
