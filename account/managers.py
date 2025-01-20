from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError("Email must be set")

        user = self.model(email=self.normalize_email(email), **other_fields)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(_("Value of is_staff must be True"))

        if other_fields.get("is_superuser") is not True:
            raise ValueError(_("Value of is_superuser must be True"))

        return self.create_user(email, password, **other_fields)
