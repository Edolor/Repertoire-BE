from django.db import models
from uuid import uuid4
from django.utils import timezone
from datetime import date
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from gdstorage.storage import GoogleDriveStorage


gd_storage = GoogleDriveStorage()


def validate_date(value):
    """
    Ensures the project build date is not in the future
    """
    if value > date.today():
        raise ValidationError(_("Date must be today or in the past"))


class Project(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True,
                          unique=True, editable=False)
    title = models.CharField(
        max_length=200, blank=False, null=False, unique=True)
    description = models.TextField(blank=False, null=False)
    created = models.DateField(
        blank=False, null=False, validators=[validate_date])
    client = models.CharField(
        max_length=100, default="None", blank=False, null=False)
    thumbnail = models.ImageField(upload_to="projects", blank=False, storage=gd_storage)

    DOMAIN_CHOICES = (
        ("wb", "Web development"),
        ("ds", "Data science"),
        ("uix", "UI/UX design"),
        ("ml", "Machine learning"),
        ("cs", "Cyber security"),
        ("rd", "Random project"),
    )
    domain = models.CharField(
        max_length=3, blank=False, null=False, choices=DOMAIN_CHOICES)

    ROLE_CHOICES = (
        ("fd", "Frontend developer"),
        ("bd", "Backend developer"),
        ("fs", "Fullstack developer"),
        ("uix", "UI/UX designer"),
        ("ds", "Data scientist"),
        ("sd", "Software developer"),
    )
    role = models.CharField(max_length=3, default="bd",
                            blank=False, null=False, choices=ROLE_CHOICES)

    TYPE_CHOICES = (
        ("js", "Joint project"),
        ("so", "Solo")
    )
    type = models.CharField(max_length=3, default="so",
                            blank=False, null=False, choices=TYPE_CHOICES)

    live_url = models.URLField(blank=True)
    figma_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    date_created = models.DateTimeField(
        default=timezone.now)  # Date added to model

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def save(self):
        """Handle resizing of thumbnail"""
        # if self.thumbnail:
        #     img = Img.open(self.thumbnail)
        #     # if img.height > 800 or img.width > 600:
        #     output_size = (800, 600)
        #     img.thumbnail(output_size)  # Maintains aspect ratio
        #     # img.save(self.thumbnail.path)

        #     # Save the resized image to a BytesIo object
        #     # image_io = BytesIO()

        #     self.thumbnail = img

        super().save()


class Tag(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    project = models.ManyToManyField(Project, related_name="tags")

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tools")

    def __str__(self):
        return f"{self.name} - {self.project.title}"


class Image(models.Model):
    url = models.ImageField(upload_to="projects", storage=gd_storage)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"{self.project.title} Image"
