from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
