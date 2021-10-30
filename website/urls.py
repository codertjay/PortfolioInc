from rest_framework.routers import DefaultRouter

from website.views import WebsiteViewSetAPIView

app_name = 'website'

router = DefaultRouter()
router.register(r'', WebsiteViewSetAPIView, basename='website', )
urlpatterns = router.urls
