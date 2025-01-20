from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Experience, Honour
from .serializers import (
    ExperienceSerializer,
    HonourSerializer
)


class AboutList(APIView):
    """
    Return all experiences(experience/education) and honours(awards/certifications)
    """

    def get(self, request):
        awards = Honour.objects.filter(type="a")
        certifications = Honour.objects.filter(type="c")

        experiences = Experience.objects.filter(type="w")
        education = Experience.objects.filter(type="e")

        awards_serializer = HonourSerializer(awards, many=True)
        certification_serializer = HonourSerializer(certifications, many=True)

        experiences_serializer = ExperienceSerializer(experiences, many=True)
        education_serializer = ExperienceSerializer(education, many=True)

        data = {
            "experiences": experiences_serializer.data,
            "awards": awards_serializer.data,
            "education": education_serializer.data,
            "certifications": certification_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)
