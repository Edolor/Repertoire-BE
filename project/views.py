from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ProjectSerializerList, ProjectSerializerDetail
from .models import Project
from .pagination import ProjectPagination
from rest_framework import filters


class ProjectList(ListAPIView):
    """
    View to list projects
    """
    serializer_class = ProjectSerializerList
    queryset = Project.objects.all()
    pagination_class = ProjectPagination
    search_fields = ["title", "description"]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        """
        Optionally restrict the returned products to a user by filtering
        against a 'tag' query parameter in the URL
        """
        queryset = Project.objects.all()
        tag = self.request.query_params.get("tag")

        if tag is not None:
            queryset = Project.objects.filter(tags__name=tag)

        return queryset

    def get_serializer_context(self):
        """
        Transform's absolute url for objects to relative url
        """
        result = super().get_serializer_context()
        result["request"] = None
        return result


class ProjectDetail(RetrieveAPIView):
    """
    View to display all details relating to a particular project
    """
    serializer_class = ProjectSerializerDetail
    queryset = Project.objects.all()

    def get_serializer_context(self):
        """
        Transform's absolute url for objects to relative url
        """
        result = super().get_serializer_context()
        result["request"] = None
        return result
