from rest_framework import serializers
from .models import Project


class TagSerializer(serializers.RelatedField):
    """
    Transform the representation and reduces the dimensions(nestedness)

    from-- tags: [{ "name": "ux"}, { "name": "frontend"}] 
    to-- tags: ["ux", "frontend"] 
    """

    def to_representation(self, value):
        return value.name


class ToolSerializer(serializers.RelatedField):
    """
    Transform the representation and reduces the dimensions(nestedness)

    from-- tools: [{ "name": "VS Code"}, { "name": "Workbench"}] 
    to-- tools: ["VS Code", "Workbench"]
    """

    def to_representation(self, value):
        return value.name


class ImageSerializer(serializers.RelatedField):
    """
    Transform the representation and reduces the dimensions(nestedness)
    """
    def to_representation(self, value):
        return value.url.url


class ProjectSerializerList(serializers.ModelSerializer):
    """
    Used to display brief information about a project
    """
    tags = TagSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="project:detail")

    class Meta:
        model = Project
        fields = ["url", "title", "created",
                  "description", "thumbnail", "tags"]


class ProjectSerializerDetail(serializers.ModelSerializer):
    """
    Used to display all information about a project and (3 other products)
    """
    tools = ToolSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="project:detail")
    other_projects = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, read_only=True)

    # Resolve the actual value from (choices = CONST)
    domain = serializers.CharField(source="get_domain_display")
    role = serializers.CharField(source="get_role_display")
    type = serializers.CharField(source="get_type_display")

    class Meta:
        model = Project
        fields = ["url", "title", "description", "created", "thumbnail", "tags", "tools", "images",
                  "domain", "role", "type", "client", "live_url", "figma_url", "github_url", "other_projects"]

    def get_other_projects(self, object):
        "Extract top 3 latest projects, excluding the current one"
        serializer = ProjectSerializerList(Project.objects.exclude(
            id=object.id)[:3], many=True, context={'request': self.context["request"]})
        return serializer.data
