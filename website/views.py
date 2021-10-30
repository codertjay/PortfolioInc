from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsWebsiteOwner
from .models import Website
from .serializers import WebsiteViewSetSerializer


class WebsiteViewSetAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsWebsiteOwner]
    lookup_field = 'id'
    serializer_class = WebsiteViewSetSerializer

    def get_queryset(self):
        queryset = Website.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
