from rest_framework import serializers

from website_layout.models import Layout


class LayoutViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layout
        fields = [
            'primary_color',
            'secondary_color',
            'logo',
            'image',
            'about',
        ]
