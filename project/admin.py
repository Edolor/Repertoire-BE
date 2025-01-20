from django.contrib import admin
from .models import Project, Tag, Tool, Image


class ToolsInline(admin.TabularInline):
    model = Tool
    extras = 1

class TagsInline(admin.TabularInline):
    model = Project.tags.through
    extras = 1


class ImageInline(admin.TabularInline):
    model = Image
    extras = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TagsInline, ToolsInline, ImageInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
