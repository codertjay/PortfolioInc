from rest_framework.viewsets import ModelViewSet

from users.permissions import IsWebsiteOwner


class ProjectViewSetAPIView(ModelViewSet):
    permission_classes = [IsWebsiteOwner]
    lookup_field = 'id'
    # serializer_class = 
