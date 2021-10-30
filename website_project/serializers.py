from rest_framework import serializers

from website_project.models import Project


class ProjectViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'primary_color',
            'secondary_color',
            'logo',
            'image',
            'about',
        ]
