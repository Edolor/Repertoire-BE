from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """Used as a health checking endpoint for hosting provider."""

    def get(self, request):
        return Response({"Status": "Ok"}, status=status.HTTP_200_OK)
