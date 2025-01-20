from .models import Experience, Honour
from rest_framework import serializers


class ExperienceSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")

    class Meta:
        model = Experience
        fields = [
            "institution", "location", "about",
            "start_date", "end_date", "type"
        ]


class HonourSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="get_type_display")

    class Meta:
        model = Honour
        fields = [
            "title", "about", "sub_about",
            "banner", "issue_date", "certification_no",
            "type"
        ]
