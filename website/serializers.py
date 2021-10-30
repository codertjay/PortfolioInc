from rest_framework import serializers

from website.models import Website


class WebsiteViewSetSerializer(serializers.ModelSerializer):
    domain = serializers.CharField(max_length=50, required=False)
    user = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Website
        fields = [
            'user', 'subdomain', 'domain', 'template'
        ]
