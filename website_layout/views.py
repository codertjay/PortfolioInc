# Create your views here.
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsWebSiteUser
from website_layout.serializers import LayoutViewSetSerializer


class LayoutViewSetAPIView(ModelViewSet):
    """
    In here i have to validate the layout view set to prevent the user from creating multiple layout
    Note : The Can only create one layout for a website
    """
    permission_classes = [IsWebSiteUser]
    lookup_field = 'id'
    serializer_class = LayoutViewSetSerializer
