from django.db import models
from django.utils import timezone
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

def validate_date(value):
    """
    Disallow future date for DateField
    """
    if value > date.today():
        return ValidationError(_("Date must be today or in the past"))


class Experience(models.Model):
    TYPE = (
        ("w", "work"),
        ("e", "education"),
    )

    type = models.CharField(max_length=1, blank=False, choices=TYPE)
    start_date = models.DateField(blank=False, validators=[validate_date])
    end_date = models.DateField(blank=True, null=True, validators=[
                                validate_date])  # Can be till present
    institution = models.CharField(max_length=150, blank=False)
    location = models.CharField(max_length=150, blank=False)
    about = models.CharField(max_length=150, blank=False)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_type_display().capitalize()} ::: {self.institution} - {self.about}"


class Honour(models.Model):
    TYPE = (
        ("a", "award"),
        ("c", "certification"),
    )

    type = models.CharField(max_length=1, blank=False, choices=TYPE)
    # Image of certification
    banner = models.ImageField(upload_to="about", blank=False, storage=gd_storage)
    title = models.CharField(max_length=150, blank=False)
    about = models.CharField(max_length=150, blank=False)
    issue_date = models.DateField(blank=False, validators=[validate_date])
    sub_about = models.CharField(max_length=150, blank=True)
    certification_no = models.CharField(max_length=150, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_type_display().capitalize()} ::: {self.title} - {self.about}"
